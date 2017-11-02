def cut_fragments(text, length=200, overlapping = False):
    """ Takes a string and returns fragments """
    fragments = []
    step = length if not overlapping else 1

    for index in range(0, len(text) - step, step):
        f = text[index:index+length]
        if len(f) == length:
            fragments += [ f ]
    return fragments

def gini(item_set):
    """ Return the Gini impurity score. """
    c = Counter(x for x, _, _ in item_set)
    total = c[0] + c[1]
    gini = 1 - (c[0] / total)**2 - (c[1] / total)**2
    return gini

def split_quality(initial_set, feature):
    initial_quality = gini(initial_set)
    left_set, right_set = [], []
    for item in initial_set:    # Split items into left and right set
        label, features, original = item
        if feature in features: # According to the candidate feature            
            left_set += [item]
        else:
            right_set += [item]

    Lquality = gini(left_set)  if len(left_set) > 0 else 0
    Rquality = gini(right_set) if len(right_set) > 0 else 0
    average_new_quality = ((Lquality) / len(initial_set)) * Lquality \
                        + ((Rquality) / len(initial_set)) * Rquality

    improvement = initial_quality - average_new_quality
    return improvement, Lquality, Rquality, left_set, right_set

# ------ TESTS -------

class decisionTree:
    def __init__(self):
        # Branch
        self.feature = None
        self.left = None
        self.right = None

        # Leaf
        self.decision = None

    def train(self, items, features, steps=100, depth=5):
        if depth > 0 and len(items) > 10:
            # Pick the best improvement out of `step' random features
            Fs = random.sample(features, steps)
            (improv, _, _, LS, RS), best_F = \
                max((split_quality(items, F), F) for F in Fs)

            if len(RS) == 0 or len(LS) == 0 or improv < 0.01:
                self.make_leaf(items)
                return self

            # Make branch using best feature
            self.feature = best_F
            self.right = decisionTree().train(RS, features, steps, depth - 1)
            self.left = decisionTree().train(LS, features, steps, depth - 1)
        else:
            self.make_leaf(items) # Select class by majority vote
        return self

    def make_leaf(self, items):
        c = Counter(x for x, _, _ in items)
        self.decision = round(c[1] / len(items))

    def clasify(self, item):
        if self.feature is not None:
            _, feature_map, _ = item
            if self.feature in feature_map:
                return self.left.clasify(item)
            else:
                return self.right.clasify(item)
        else:
                return self.decision



import random
from collections import Counter

def load_data_pipeline():
    # Read the two texts data from project Guttemberg
    FR = open(r"assets/pg14287.txt").read()[100000:]
    DE = open(r"assets/21000-0.txt").read()[100000:]

    # Cute into fragments of 200 characters
    FR_frags = cut_fragments(FR, length=200)
    DE_frags = cut_fragments(DE, length=200)

    # For each fragment extract a label and feature map.
    # (features are overlapping sequences of 3 characters)
    FR_feats = list(map(lambda x: (0, set(cut_fragments(x, 3, True)), x), \
        FR_frags))
    DE_feats = list(map(lambda x: (1, set(cut_fragments(x, 3, True)), x), \
        DE_frags))
    random.shuffle(FR_feats); random.shuffle(DE_feats)

    # Split the data set into 400 fagments per language for training
    # and 200 fragments per language for evaluating performance.
    training = FR_feats[:400] + DE_feats[:400]
    evaluation = FR_feats[400:600] + DE_feats[400:600]

    # Extract a set of features from the training set
    features = set()
    for _, feats, _ in training: features |= feats

    return training, evaluation, list(features)

def evaluate_pipeline(trees_no = 40, depth=5, verb=True):
    # Train a random forest on training set
    Forrest = []
    for _ in range(trees_no):
        T = decisionTree().train(training, features, depth=depth)
        Forrest += [ T ]

    # Evaluate accuracy on evaluation set
    errors = []
    for x in evaluation:
        result = sum(T.clasify(x) for T in Forrest) / trees_no
        if int(round(result)) != x[0]:
            errors += [ x[2] ]

    # Print results
    print("Accuracy: %.4f%%" % (100 * (1 - len(errors) / len(evaluation))))
    print("Errors: (%d)" % len(errors))
    for case in errors:
        if verb: print(" -- \"%s\"" % case)

    return [(sum(T.clasify(x) for T in Forrest) / trees_no, x[0])  for x in evaluation]

import matplotlib.pyplot as plt

def make_ROC(data):
    data = sorted(data, reverse=True)
    cutoffs = set(d for d,_ in data)

    TPR, FPR = [], []
    for c in sorted(cutoffs, reverse=True):
        TPR += [ len([1 for d,l in data if d > c and l == 1]) / 200 ]
        FPR += [ len([1 for d,l in data if d > c and l == 0]) / 200 ]

    plt.plot(FPR, TPR)
    plt.xlim([0.0, 0.05])
    plt.xlabel("False Positive Rate")
    plt.ylabel("True Positive Rate")
    plt.title("ROC curve for the RDF classifier")
    plt.savefig(r"assets/ROC.pdf", bbox_inches='tight')
    plt.close()
    
# TODO: remove this from the global scope and refactor into a fixture
training, evaluation, features = load_data_pipeline()

if __name__ == "__main__":
    data = evaluate_pipeline(verb=True)
    print("Toy: depth=1 Trees=1")
    evaluate_pipeline(1,1, verb=False)
    make_ROC(data)

def test_fragments():
    text = "AABBCCD"
    frag = cut_fragments(text, 2)
    assert frag == ["AA", "BB", "CC"]

def testImpurity():
    c = Counter(x for x,_,_ in training)
    assert c[0] == c[1]
    assert gini(training) == 0.5
    
    for _ in range(100):
        F = random.choice(features)
        Q, L, R, _, _  = split_quality(training, F)
        
def test_train():
    T = decisionTree()
    T.train(training, features)

    for x in evaluation[:10]:
        T.clasify(x)



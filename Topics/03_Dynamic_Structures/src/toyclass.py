class Count(object):     # Define a type `Count'
    def __init__(self, v=0):
        """ Initialize the counter with a value (default: zero) """
        self._value = v   # Class Attribute 

    def inc(self):
        """ Increment the counter by one. """
        self._value += 1

    def get(self):
        """ Get the value of the counter. """
        return self._value

def test_counter():
    c = Count(0)         # Initialization: c is an instance of Count
    c.inc()              # Method calls
    assert c.get() == 1  
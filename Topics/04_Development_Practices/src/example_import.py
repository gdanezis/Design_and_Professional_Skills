""" Worked examples for different types of imports:

    >>> import statistics
    >>> statistics.median([1, 2, 3, 4, 8])
    3

    >>> from statistics import median, mean
    >>> median([1, 2, 3, 4, 8])
    3

    >>> import statistics as stat
    >>> stat.median([1, 2, 3, 4, 8])
    3

    >>> from statistics import *
    >>> mode([1, 2, 2, 2, 3, 4, 5, 6, 6])
    2

    >>> names = dir(stat)
    >>> names
    ['Decimal', 'Fraction', 'StatisticsError', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '_coerce', '_convert', '_counts', '_decimal_to_ratio', '_exact_ratio', '_isfinite', '_ss', '_sum', 'collections', 'groupby', 'math', 'mean', 'median', 'median_grouped', 'median_high', 'median_low', 'mode', 'pstdev', 'pvariance', 'stdev', 'variance']


"""


def test_imports():
    assert True
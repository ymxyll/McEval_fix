

from typing import List
 
def mean_absolute_deviation(numbers: List[float]) -> float:
    """ For a given list of input numbers, calculate Mean Absolute Deviation
    around the mean of this dataset.
    Mean Absolute Deviation is the average absolute difference between each
    element and a centerpoint (mean in this case):
    MAD = average | x - x_mean |
    >>> mean_absolute_deviation([1.0, 2.0, 3.0, 4.0])
    1.0
    """
    # Calculate the mean of the numbers
    mean = sum(numbers) / len(numbers)
    
    # Calculate the absolute difference from the mean for each number
    absolute_diffs = [abs(num - mean) for num in numbers]
    
    # Calculate the mean of the absolute differences
    mad = sum(absolute_diffs) / len(absolute_diffs)
    
    return mad

# Test the function
def check(mean_absolute_deviation):
    assert abs(mean_absolute_deviation([1.0, 2.0, 3.0]) - 2.0/3.0) < 1e-6
    assert abs(mean_absolute_deviation([1.0, 2.0, 3.0, 4.0]) - 1.0) < 1e-6
    assert abs(mean_absolute_deviation([1.0, 2.0, 3.0, 4.0, 5.0]) - 6.0/5.0) < 1e-6
    
check(mean_absolute_deviation)
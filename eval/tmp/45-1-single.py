

import heapq
from typing import List 

def minimum_cost_to_merge_fruits(fruit_counts: List[int]) -> int:
    """
    Calculates the minimum total cost to merge multiple heaps of fruits into a single heap.
    The cost of merging two heaps is equal to the sum of their weights. The function utilizes
    a greedy algorithm with a min-heap (priority queue) to ensure the smallest heaps are merged first,
    minimizing the total cost.

    Parameters:
    fruit_counts (List[int]): A list of integers representing the counts of each type of fruit.

    Returns:
    int: The minimum total cost required to merge all heaps of fruits.

    Examples:
    >>> minimum_cost_to_merge_fruits([1, 2, 9])
    15  # Merging (1+2) with a cost of 3, and then (3+9) with a cost of 12, gives a total cost of 15.

    >>> minimum_cost_to_merge_fruits([5, 5])
    10  # Merging (5+5) with a total cost of 10.

    >>> minimum_cost_to_merge_fruits([10, 20, 30, 40, 50])
    300 # One optimal way is merging 10+20 (cost 30), then merging 30+30 (cost 60),
        # followed by 40+50 (cost 90), and finally merging the two remaining heaps 60+90 (cost 150).
        # Total cost is 30+60+90+150 = 300.
    """
    # Initialize a min-heap with the fruit counts.
    heapq.heapify(fruit_counts)
    
    total_cost = 0
    
    # Keep merging until there is only one heap left.
    while len(fruit_counts) > 1:
        # Pop the two smallest heaps.
        first = heapq.heappop(fruit_counts)
        second = heapq.heappop(fruit_counts)
        
        # The cost is the sum of the two smallest heaps.
        cost = first + second
        total_cost += cost
        
        # Push the new heap back into the min-heap.
        heapq.heappush(fruit_counts, cost)
    
    return total_cost
def test_minimum_cost_to_merge_fruits():
    # Test case 1: As provided in the problem statement example
    fruits1 = [1, 2, 9]
    assert minimum_cost_to_merge_fruits(fruits1) == 15, "Test case 1 failed"

    # Test case 2: Simple case with only two types of fruits
    fruits2 = [5, 5]
    assert minimum_cost_to_merge_fruits(fruits2) == 10, "Test case 2 failed"

    # Test case 3: More complex case with multiple types of fruits
    fruits3 = [10, 20, 30, 40, 50]
    assert minimum_cost_to_merge_fruits(fruits3) == 330, "Test case 3 failed"

    # Test case 4: Case with fruits having the same count
    fruits4 = [3, 3, 3, 3]
    assert minimum_cost_to_merge_fruits(fruits4) == 24, "Test case 4 failed"

    # Test case 5: Case with a single type of fruit
    fruits5 = [7]
    assert minimum_cost_to_merge_fruits(fruits5) == 0, "Test case 5 failed"

    print("All test cases passed.")

# Run the test function
test_minimum_cost_to_merge_fruits()
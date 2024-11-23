

from typing import List
def calculate_scholarship(grades: List[int], leader: str, west: str, papers: int) -> int:
    """
    Calculate the total scholarship amount for a student based on academic and extracurricular achievements.

    The function uses a set of conditions to determine the total amount of scholarship money a student is entitled to.
    Scholarships are awarded based on academic grades, leadership roles, regional background, and research contributions.

    Parameters:
    grades (list of int): A two-element list containing the student's academic grades [end of term average, class evaluation].
    leader (str): A string ('Y' or 'N') indicating if the student is a class leader.
    west (str): A string ('Y' or 'N') indicating if the student is from a western province.
    papers (int): An integer representing the number of research papers published by the student.

    Returns:
    int: The total scholarship amount the student is eligible for.

    Examples:
    >>> calculate_scholarship([87, 82], 'Y', 'N', 0)
    4850

    >>> calculate_scholarship([88, 78], 'N', 'Y', 1)
    9000

    The first example calculates a scholarship for a student with an average grade of 87, an evaluation grade of 82,
    who is a class leader ('Y'), not from the western province ('N'), and with no published papers (0). This student
    would receive a total of 4850 units of currency.

    In the second example, the student has an average grade of 88, an evaluation grade of 78, is not a class leader ('N'),
    is from the western province ('Y'), and has published 1 paper. This student would receive a total of 9000 units of currency.
    """
    scholarship = 0
    if grades[0] > 80 and papers >= 1:
        scholarship += 8000
    if grades[0] > 85 and grades[1] > 80:
        scholarship += 4000
    if grades[0] > 90:
        scholarship += 2000
    if grades[0] > 85 and west == 'Y':
        scholarship += 1000
    if grades[1] > 80 and leader == 'Y':
        scholarship += 850
    if papers > 1:
        scholarship += 5000
    return scholarship
def test_calculate_scholarship():
    # Test case 1: Student meets multiple scholarship criteria
    grades1 = [90, 85]  # Both grades are high
    leader1 = 'Y'  # Is a leader
    west1 = 'Y'  # Is from the West
    papers1 = 2  # Has published papers
    expected_scholarship1 = 13850  # Should receive multiple scholarships
    assert calculate_scholarship(grades1, leader1, west1,
                                 papers1) == expected_scholarship1, f"Test case 1 failed. Expected {expected_scholarship1}, got {calculate_scholarship(grades1, leader1, west1, papers1)}"

    # Test case 2: Student meets one scholarship criteria
    grades2 = [82, 70]  # Only the first grade is high enough
    leader2 = 'N'  # Is not a leader
    west2 = 'N'  # Is not from the West
    papers2 = 1  # Has published papers
    expected_scholarship2 = 8000  # Should receive scholarship for first grade and papers
    assert calculate_scholarship(grades2, leader2, west2,
                                 papers2) == expected_scholarship2, f"Test case 2 failed. Expected {expected_scholarship2}, got {calculate_scholarship(grades2, leader2, west2, papers2)}"

    # Test case 3: Student does not meet any scholarship criteria
    grades3 = [75, 75]  # Both grades are below the threshold
    leader3 = 'N'  # Is not a leader
    west3 = 'N'  # Is not from the West
    papers3 = 0  # Has no published papers
    expected_scholarship3 = 0  # Should not receive any scholarships
    assert calculate_scholarship(grades3, leader3, west3,
                                 papers3) == expected_scholarship3, f"Test case 3 failed. Expected {expected_scholarship3}, got {calculate_scholarship(grades3, leader3, west3, papers3)}"

    # If no assertion is raised, all test cases passed
    print("All test cases passed!")


test_calculate_scholarship()
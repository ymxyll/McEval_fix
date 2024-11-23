

def sort_students(student_scores):
    """
    Sorts a list of students based on their scores. The students are sorted primarily by their total score (descending),
    then by their Chinese score (descending), and finally by their student number (ascending) in case of a tie.
    
    Args:
    student_scores (list): A list of tuples, where each tuple consists of (student_number, total_score, Chinese_score).
    
    Returns:
    list: A list of tuples sorted according to the above rules.
    
    Examples:
    >>> sort_students([(1, 237, 90), (2, 244, 87), (3, 258, 78), (4, 264, 88), (5, 215, 67), (6, 265, 78)])
    [(6, 265, 78), (4, 264, 88), (3, 258, 78), (2, 244, 87), (1, 237, 90), (5, 215, 67)]
    
    >>> sort_students([(1, 300, 100), (2, 300, 99), (3, 299, 98), (4, 298, 97), (5, 297, 96)])
    [(1, 300, 100), (2, 300, 99), (3, 299, 98), (4, 298, 97), (5, 297, 96)]
    
    In the first example, the student with the highest total score is number 6. Students number 4 and 3 follow,
    with descending total scores. Student number 1 has a lower total score than student number 2, but a higher Chinese score,
    so student number 1 is placed after student number 2 in the sorted list.
    
    In the second example, students number 1 and 2 have the same total score, but student number 1 has a higher Chinese score,
    so they are placed first. The rest are sorted by their descending total scores.
    """
    # Sort the students by the rules: total score, Chinese score, student number
    sorted_students = sorted(student_scores, key=lambda x: (-x[1], -x[2], x[0]))
    return sorted_students
def test_sort_students():
    # Test case 1
    input_scores = [(1, 237, 90), (2, 244, 87), (3, 258, 78), (4, 264, 88), (5, 215, 67), (6, 265, 78)]
    expected_output = [(6, 265, 78), (4, 264, 88), (3, 258, 78), (2, 244, 87), (1, 237, 90), (5, 215, 67)]
    assert sort_students(input_scores) == expected_output, "Test case 1 failed"

    # Test case 2
    input_scores = [(1, 258, 80), (2, 264, 88), (3, 258, 90), (4, 244, 87), (5, 258, 78), (6, 264, 88), (7, 220, 67), (8, 265, 78)]
    expected_output = [(8, 265, 78), (2, 264, 88), (6, 264, 88), (3, 258, 90), (1, 258, 80), (5, 258, 78), (4, 244, 87), (7, 220, 67)]
    assert sort_students(input_scores) == expected_output, "Test case 2 failed"

    # Test case 3
    input_scores = [(1, 300, 100), (2, 300, 100), (3, 299, 99), (4, 298, 98), (5, 297, 97)]
    expected_output = [(1, 300, 100), (2, 300, 100), (3, 299, 99), (4, 298, 98), (5, 297, 97)]
    assert sort_students(input_scores) == expected_output, "Test case 3 failed"

    print("All test cases passed!")

# Run the test function
test_sort_students()
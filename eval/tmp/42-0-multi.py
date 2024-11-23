

def find_most_unhappy_day(schedule) -> int:
    """
    Calculate the day of the week when Jinjin is most unhappy based on her schedule.
    
    Jinjin is unhappy if the total hours spent in school and extra classes exceed 8 hours in a day. 
    The function finds the day when her unhappiness is the greatest, which is the day when the total
    hours are the farthest above the threshold. If there are multiple days with the same level of 
    maximum unhappiness, the earliest day is returned. If Jinjin is not unhappy on any day, the 
    function returns 0.
    
    Args:
        schedule (list[tuple[int, int]]): A list of 7 tuples, where each tuple represents the 
                                           number of hours spent at school and in extra classes
                                           for each day of the week, respectively.
                                           
    Returns:
        int: The day of the week when Jinjin is most unhappy (1-7 for Monday to Sunday) or 0 
             if she is never unhappy.
    
    Cases:
        - If Jinjin has the following schedule [(5, 3), (6, 2), (7, 2), (5, 3), (5, 4), (0, 4), (0, 6)],
          she is most unhappy on Wednesday (day 3), so the function will return 3.
        - If her schedule is [(4, 3), (4, 3), (4, 3), (4, 3), (4, 3), (0, 3), (0, 2)], Jinjin is never
          unhappy, and the function will return 0.
        - For a schedule [(6, 3), (6, 2), (6, 2), (6, 3), (6, 2), (0, 3), (0, 2)], Jinjin is equally 
          unhappy on Monday and Thursday, but since Monday comes first, the function returns 1.
    """
    DAYS_OF_WEEK = 7
    UNHAPPINESS_THRESHOLD = 8

    most_unhappy_day = 0
    max_unhappiness = 0

    for day in range(1, DAYS_OF_WEEK + 1):
        school_hours, extra_class_hours = schedule[day - 1]
        total_hours = school_hours + extra_class_hours
        unhappiness = total_hours - UNHAPPINESS_THRESHOLD

        if unhappiness > max_unhappiness:
            max_unhappiness = unhappiness
            most_unhappy_day = day

    return most_unhappy_day if most_unhappy_day != 0 else 0
def test_find_most_unhappy_day():
    # Test case 1: Provided example where Jinjin is most unhappy on Wednesday
    schedule1 = [
        (5, 3),
        (6, 2),
        (7, 2),
        (5, 3),
        (5, 4),
        (0, 4),
        (0, 6)
    ]
    assert find_most_unhappy_day(schedule1) == 3, "Test case 1 failed"

    # Test case 2: Jinjin is never unhappy
    schedule2 = [
        (4, 3),
        (4, 3),
        (4, 3),
        (4, 3),
        (4, 3),
        (0, 3),
        (0, 2)
    ]
    assert find_most_unhappy_day(schedule2) == 0, "Test case 2 failed"

    # Test case 3: Jinjin is most unhappy on Monday and Thursday, but Monday should be returned
    schedule3 = [
        (6, 3),
        (6, 2),
        (6, 2),
        (6, 3),
        (6, 2),
        (0, 3),
        (0, 2)
    ]
    assert find_most_unhappy_day(schedule3) == 1, "Test case 3 failed"

    print("All test cases passed.")

# Run the test function
test_find_most_unhappy_day()


def calculate_score(system: int, points: str) -> list:
    """
    Calculate the score of a series of ping-pong games based on the provided scoring system.

    This function takes in the desired scoring system (either 11 or 21 points) and a string 
    representing the sequence of points won by the player ('W') and the opponent ('L'). 
    The function processes the string and returns a list of game scores formatted as "player_score:opponent_score".

    The game is considered finished when one player reaches the system's required number of points 
    (11 or 21) with at least a 2-point lead. If the sequence of points ends in the middle of a game, 
    that game's current score is also included in the output.

    Args:
    - system (int): The number of points required to win a game (either 11 or 21).
    - points (str): A string of 'W' and 'L' characters denoting points won by the player and opponent.

    Returns:
    - list: A list of strings representing the score of each game.

    Cases:
    - If points = "WWWWWWWWWWL", it represents one complete game with the player winning 10-1 under both systems.
      calculate_score(11, points) -> ["10:1"]
      calculate_score(21, points) -> ["10:1"]

    - If points = "WWLWWLWWLWWLWE", it represents two complete games and one in-progress game under the 11-point system,
      with scores 2-1, 2-1, and 1-1 respectively. Under the 21-point system, it represents a single game with a score of 6-3.
      calculate_score(11, points) -> ["2:1", "2:1", "1:1"]
      calculate_score(21, points) -> ["6:3"]

    - If points = "WWLWLWLWLWLLWLWLWLWLWWLWWLWWLWLE", it represents multiple games under both systems, with the last game unfinished.
      The 11-point system has scores 4-6, 5-5, and 1-0, while the 21-point system has scores 13-16 and 2-1.
      calculate_score(11, points) -> ["4:6", "5:5", "1:0"]
      calculate_score(21, points) -> ["13:16", "2:1"]
    """
    match_scores = []
    score_a, score_b = 0, 0

    for point in points:
        if point == 'W':
            score_a += 1
        elif point == 'L':
            score_b += 1

        # Check if a game is finished under the current system
        if (score_a >= system or score_b >= system) and abs(score_a - score_b) >= 2:
            match_scores.append(f"{score_a}:{score_b}")
            score_a, score_b = 0, 0

    # Include the last game if it's not finished when input ends
    if score_a != 0 or score_b != 0:
        match_scores.append(f"{score_a}:{score_b}")

    # Check if a game is finished under the other system
    if system == 11:
        match_scores_21 = []
        score_a, score_b = 0, 0
        for point in points:
            if point == 'W':
                score_a += 1
            elif point == 'L':
                score_b += 1

            # Check if a game is finished under the 21 system
            if (score_a >= 21 or score_b >= 21) and abs(score_a - score_b) >= 2:
                match_scores_21.append(f"{score_a}:{score_b}")
                score_a, score_b = 0, 0

        # Include the last game if it's not finished when input ends
        if score_a != 0 or score_b != 0:
            match_scores_21.append(f"{score_a}:{score_b}")
        match_scores.extend(match_scores_21)

    return match_scores
def test_calculate_score():
    # Test case 1: A single game in both systems, with a clear winner.
    points = "WWWWWWWWWWL"
    expected_11 = ["10:1"]
    expected_21 = ["10:1"]
    assert calculate_score(11, points) == expected_11, "Test case 1 (11-point) failed"
    assert calculate_score(21, points) == expected_21, "Test case 1 (21-point) failed"

    # Test case 2: Multiple games, some completed and one in progress.
    points = "WWLWWLWWLWWLWE"
    expected_11 = ["9:4"]
    expected_21 = ["9:4"]
    assert calculate_score(11, points) == expected_11, "Test case 2 (11-point) failed"
    assert calculate_score(21, points) == expected_21, "Test case 2 (21-point) failed"

    # Test case 3: A longer sequence with many games and a final unfinished game.
    points = "WWLWLWLWLWLLWLWLWLWLWWLWWLWWLWLE"
    expected_11 = ['12:10', '5:4']
    expected_21 = ['17:14']
    assert calculate_score(11, points) == expected_11, "Test case 3 (11-point) failed"
    assert calculate_score(21, points) == expected_21, "Test case 3 (21-point) failed"

    print("All test cases passed!")

# Run the test function
test_calculate_score()
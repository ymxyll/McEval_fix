


def max_energy(beads):
    """
    Calculate the maximum energy that can be released by merging beads on a necklace.

    The function takes a list of integers representing the energy beads on a necklace, where
    each bead has a head and a tail value. The head value of each bead must match the tail
    value of the next bead in the sequence. The necklace is circular, and merging two adjacent
    beads releases energy equal to the product of the head value of the first bead, the matching
    value, and the tail value of the second bead.

    To find the maximum energy release, the function considers all possible orders of merging beads
    and uses dynamic programming to compute the maximum energy obtainable.

    Args:
        beads: A list of integers where each integer represents the head value of a bead and
               the tail value of the previous bead. The tail value of the last bead is assumed
               to match the head value of the first bead due to the circular nature of the necklace.

    Returns:
        An integer representing the maximum energy that can be obtained by optimally merging all beads.

    Examples:
        >>> max_energy([2, 3, 5, 10])
        710
        This sequence represents beads with values (2,3), (3,5), (5,10), (10,2). The maximum energy
        released by merging them in the optimal order is 710.

        >>> max_energy([1, 2, 3, 4])
        48
        This sequence represents beads with values (1,2), (2,3), (3,4), (4,1). The maximum energy
        released by merging them in the optimal order is 48.
    """
    n = len(beads)
    # Duplicate the sequence to account for the circular nature of the necklace
    beads = beads + beads
    # Initialize the DP table
    # dp[i][j] will store the maximum energy obtainable from the subsequence beads[i] to beads[j]
    dp = [[0] * (2 * n) for _ in range(2 * n)]
    
    # Fill the DP table
    for length in range(2, 2 * n):  # length of the subsequence
        for i in range(2 * n - length + 1):
            j = i + length - 1
            for k in range(i+1, j, 2):  # k is the splitting point, skipping every other index to account for the circular nature
                # Calculate the energy
                energy = beads[i] * beads[k] * beads[j]
                # Choose the maximum energy
                dp[i][j] = max(dp[i][j], dp[i][k] + dp[k+1][j] + energy)

    # Find the maximum energy for all possible starting points
    return max(dp[i][i+n-1] for i in range(n))

# Test cases
def test_max_energy():
    assert max_energy([2, 3, 5, 10]) == 710, "Testcase 1 failed"
    assert max_energy([1, 2, 3, 4]) == 80, "Testcase 2 failed"
    assert max_energy([4, 4, 4, 4]) == 192, "Testcase 3 failed"
    assert max_energy([30, 40, 50, 60]) == 372000, "Testcase 4 failed"
    print("All testcases passed")

# Call the test function
test_max_energy()
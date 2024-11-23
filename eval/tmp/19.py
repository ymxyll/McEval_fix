


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
        >>> max_energy([1, 2, 3, 4])
        48
    """
    n = len(beads)
    beads = beads + beads[:2]  # Make the necklace circular
    dp = [[0] * n for _ in range(n)]

    # Fill in the dp table for all possible sub-necklaces
    for length in range(2, n+1):
        for start in range(n):
            end = (start + length - 1) % n
            if length == 2:
                dp[start][end] = beads[start] * beads[start] * beads[end]
            else:
                dp[start][end] = max(
                    dp[start][(start + i) % n] + dp[(start + i + 1) % n][end] + beads[start] * beads[(start + i) % n] * beads[end]
                    for i in range(length - 1)
                )

    # Find the maximum energy for the whole necklace
    max_energy = 0
    for i in range(n):
        max_energy = max(max_energy, dp[i][(i+1)%n])

    return max_energy
def test_max_energy():
    assert max_energy([2, 3, 5, 10]) == 710, "Testcase 1 failed"
    assert max_energy([1, 2, 3, 4]) == 80, "Testcase 2 failed"
    assert max_energy([4, 4, 4, 4]) == 192, "Testcase 3 failed"
    assert max_energy([30, 40, 50, 60]) == 372000, "Testcase 4 failed"
    print("All testcases passed")

# Call the test function
test_max_energy()
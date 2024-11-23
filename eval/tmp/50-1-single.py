

def total_smoked_cigarettes(n, k):
    """
    Calculates the total number of cigarettes Peter can smoke.
    Peter starts with n cigarettes and can exchange k butts for one new cigarette.
    The function takes two arguments, n and k, where n is the initial number of cigarettes,
    and k is the number of cigarette butts needed to exchange for one new cigarette.
    The function returns the total number of cigarettes Peter can smoke.
    Example:
    >>> total_smoked_cigarettes(4, 3)
        5
    >>> total_smoked_cigarettes(10, 3)
        14
    """
    total = n  # Peter starts with 'n' cigarettes
    butts = n  # Initially, the number of butts equals the number of smoked cigarettes

    while butts >= k:
        # Exchange butts for new cigarettes
        new_cigs = butts // k
        # Smoke the new cigarettes
        total += new_cigs
        # Update the count of butts: add new butts, subtract used butts
        butts = butts % k + new_cigs
        if butts < k:
            break
    return total
assert total_smoked_cigarettes(4, 3) == 5
assert total_smoked_cigarettes(10, 3) == 14
assert total_smoked_cigarettes(1, 2) == 1  # Peter cannot exchange butts as he starts with less than k
assert total_smoked_cigarettes(20, 4) == 26
assert total_smoked_cigarettes(0, 5) == 0  # Peter starts with no cigarettes
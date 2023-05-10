d = [1, 3, 54, 712, 52, 904, 113, 12, 135, 32, 31, 56, 23, 79, 611, 123, 677, 232, 997, 101, 111,
123, 2, 7, 24, 57, 99, 45, 666, 42, 104, 129, 554, 335, 876, 35, 15, 93, 13]


def min_efficiency(efficiency):
    """
    Given a list of integers `efficiency`, returns a list containing the cost
    of each configuration where the list is partitioned into pairs, and the
    cost is the sum of the absolute differences between each pair.
    
    Args:
    - efficiency (list of int): the list of integers to partition into pairs
    
    Returns:
    - list of int: the cost of each partition configuration
    """
    n = len(efficiency)
    efficiency.sort()
    costs = []
    for i in range(n):
        pairs = efficiency[:i] + efficiency[i+1:]
        cost = sum(abs(pairs[j] - pairs[j+1]) for j in range(0, n-2, 2))
        costs.append(cost)
    return(costs)

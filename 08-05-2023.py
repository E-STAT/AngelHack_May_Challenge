import itertools

def permutatation(string: str) -> list:
    """
    Generate all permutations of the characters in a string.
    """
    perms = [''.join(p) for p in itertools.permutations(string)]
    return perms

def divisible_by_seven(perms: list) -> list:
    """
    Check each permutation to see if it is divisible by 7.
    """
    divisible_perms = []
    for perm in perms:
        if int(perm) % 7 == 0:
            divisible_perms.append(int(perm))
    return divisible_perms

def avg_of_min_max(divisible_perms: list) -> float:
    """
    Calculate the average between the smallest and largest divisible permutation.
    """
    if len(divisible_perms) > 0:
        divisible_perms.sort()
        print(f"Divisible by 7 are: {divisible_perms}")
        avg = (divisible_perms[0] + divisible_perms[-1]) / 2
    else:
        print("No permutation is divisible by 7.")
        avg = None
    return avg

if __name__ == "__main__":
    perm = permutatation("1867")
    div_7 = divisible_by_seven(perms=perm)
    avg = avg_of_min_max(divisible_perms=div_7)

    if avg:
        print(f"The Average of the smallest and largest permutation\
            that is divisible by 7 is: {avg}")

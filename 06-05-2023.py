def fastest_runner(speed: int, limit: int, rest: int) -> int:
    """
    Calculates the total distance covered by a runner given their
    running speed, limit time, and rest time, assuming they run for
    a total of 1234 seconds.

    Parameters:
        speed (int): The speed of the runner in units per second.
        limit (int): The maximum time the runner can run without resting.
        rest (int): The time the runner rests after reaching their limit.

    Returns:
        int: The total distance covered by the runner in the given time.

    Example:
        >>> fastest_runner(10, 6, 20)
        820
    """
    distance = 0
    time_used = 0
    
    # Run and rest in a loop until 1234 seconds are up
    for i in range(1234 // (limit + rest)):
        # Run for the limit time units
        distance += speed * limit
        time_used += limit

        # Rest for the rest time units
        time_used += rest

    # If there is remaining time, run for the remaining time
    remaining_time = 1234 % (limit + rest)
    if remaining_time > 0:
        if remaining_time <= limit:
            distance += speed * remaining_time
        else:
            distance += speed * limit

    return distance


if __name__ == "__main__":
    # Calculate the distance covered by each runner
    john = fastest_runner(10, 6, 20)
    james = fastest_runner(8, 8, 25)
    jenna = fastest_runner(12, 5, 16)
    josh = fastest_runner(7, 7, 23)
    jacob = fastest_runner(9, 4, 32)
    jerry = fastest_runner(5, 9, 18)

    # Create a list of distances and find the maximum distance
    winner = [john, james, jenna, josh, jacob, jerry]
    max_distance = max(winner)

    # Print the maximum distance and the index of the winning runner
    print(f"The winner ran {max_distance} units!")
    print(f"The winning runner is #{winner.index(max_distance)+1}.")

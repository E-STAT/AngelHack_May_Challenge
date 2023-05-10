# AngelHack_May_Challenge

## First Challenge
* **Question**

    John was visiting a friend one day who lived in an apartment, but the instructions that he
    received were a bit confusing. When he arrives, he starts on the ground floor (floor 0) and
    has to follow the instructions one character at a time.
    A left arrow (<) means going up one floor, and a right arrow (>) means going down one floor.
    For example:
    <<>> results in Floor 0, because he goes up twice (<<) and then goes down twice (>>).
    <><> results in Floor 0 as well because he goes up once, followed by down once
    <<< results in Floor 3
    >><<<>> results in Floor -1
    This is what John saw:
    <<<<<<><><><><<<<><><><><><<<<><><><><><>>>><<><><><><><><><><>>>><<<<
    <><><><><><<<<<><><><><><><<<<><><><><><><><><><><><<<<<<><><<><><>>><
    <>><<><<>><><<><><><><><><><<<<<<<<<>><<><><<<><><><><<<<<<>>>>>>>>>>>
    <>><><><>><<<><><><><<><><<><><><><><><><<<<><><><>><<>>>>><><><>><<<>
    <><><><><><>><><><><><><><><><><><><><><><><><<<><><><><><><><><><><><
    ><><><><><><>>>><><><><><><><><><>><<<<<<<<<<>>>>><<<<<>>>><<<<>><<><<
    ><><><><><><><><><><<<<<<<><><<><<><<><<><><><><><<>><><>><><><><><<><
    <<<<>><<<<><><<<><>>><<><>>>>><>>><<><<><><><><<>><><><><><><><><><><>
    <><><><><><<<<><><<<<><<<>>>>>>>>><<><<<>>>>><<<<<<<<<>>>><<><>><><<><
    <>><<>><<>><
    Which floor did he end up on?

* **Answer**

![image](https://user-images.githubusercontent.com/54026058/236300882-84ee1cce-02e9-4dad-91b0-b7119f411689.png)

    John is on the 56th floor


# Second Challenge

* **Question** 

    Run run run away! A group of friends wanted to know who is the fastest amongst them, and
    decided to hold a running race.
    It wasn’t fun just running, so they decided to go for a marathon. These guys are good, but
    must rest occasionally to recover their energy.
    Did I mention that these people are weird? They can only be running (always at their top
    speed), or resting (not moving at all), and can only spend integer amounts of time in either
    state.
    Example case:
    John can run 10 m/s for 6 seconds, but then must rest for 20 seconds
    James can run 8 m/s for 8 seconds, but then must rest for 25 seconds
    After one second (T=1), John has gone 10m, while James has gone 8m. After 6 seconds
    (T=6), John has gone 60m, while James has gone 48m. On the 7th second, John begins
    resting (staying at 60m), while James continues on for a total distance of 64m. On the 9th
    second, both runners are resting. They continue to rest until the 27th second when John
    runs for another 6 seconds. On the 34th second, James runs for another 8 seconds.
    At the 100th second, John is resting after running 240m while James has travelled 200m. In
    this case, John would have won if the race ended at 100 seconds.
    Here are the descriptions of this group of friends:
    1) John can run 10 m/s for 6 seconds, but then must rest for 20 seconds
    2) James can run 8 m/s for 8 seconds, but then must rest for 25 seconds
    3) Jenna can run 12 m/s for 5 seconds, but then must rest for 16 seconds
    4) Josh can run 7 m/s for 7 seconds, but then must rest for 23 seconds
    5) Jacob can run 9 m/s for 4 seconds, but then must rest for 32 seconds
    6) Jerry can run 5 m/s for 9 seconds, but then must rest for 18 seconds
    After 1234 seconds, what is the distance of the winning runner?

* **Answer** 

    ![image](https://user-images.githubusercontent.com/54026058/236636060-0d982704-8cab-4133-9ef9-b2b0cb0081b5.png)

  
    The winner is Jenna with 3540m


# Third Challenge

* **Question**
    
    Given an integer string, create all integer permutations of its digits. Determine if there is a
    permutation whose integer value is evenly divisible by 7, i.e. (permutation value) mod 7 = 0.
    For example, the possible permutations of 789 are p = {789, 798, 879, 897, 978, 987}. Of
    these values, p[2] and p[5] is divisible by 7 because 879 mod 7 = 0 and 987 mod 7 = 0.
    Their average is (879 + 987) / 2 = 933
    What you’ll need to do is determine if any of the permutations of 1867 are divisible by 7, and
    if so, what is the average between the smallest and largest permutation? Decimals are
    allowed.

* **Answer**

![image](https://user-images.githubusercontent.com/54026058/236897264-0ac49c6b-cecb-4bbf-848b-1247824c3907.png)
    
The Average of the smallest and largest permutation that is divisible by 7 is: 5152.0


# Fourth Challenge

* **Question**

    A group of workers gathered to complete a task. Each worker has an efficiency rating. They
    will be grouped in pairs so an even number of workers are required. The cost of a pair is the
    absolute difference of the efficiencies assigned to the workers. The cost of the task is the
    sum of the costs of all pairs formed. There are an odd number of workers to choose from, so
    one worker will not be paired. Select the worker to exclude so the task's cost is minimized.
    Given n workers and efficiency for each worker, find a configuration of the workers such that
    the cost of the task is the minimum possible. Return the minimum cost as the answer.
    First Example
    Efficiency = [1, 2, 4]
    The first worker has an efficiency of 1, the second worker has an efficiency of 2, and the last
    worker has an efficiency of 4.
    If we excluded the first worker (1) and pair the second (2) and last worker (4), the cost is |2 -
    4| = 2
    If we excluded the second worker (2), and pair the first and last worker instead, the cost is |1
    - 4| = 3
    If we excluded the last worker (4), the cost is |1 - 2| = 1
    Thus, the minimum cost is 1.
    Second Example
    efficiency = [4, 2, 8, 1, 9]
    The first worker has an efficiency of 4, the second worker has an efficiency of 2, … , last
    worker has an efficiency of 9.
    If we excluded the first worker (4), and you pair up the second and third workers (2, 8), and
    the fourth and fifth workers (1, 9), the cost of the task is |2 - 8| + |1 - 9| = 14.
    Can we do it differently? If we pair up the second and fourth workers (2, 1) and third and last
    worker (8, 9), the cost of the task is |2 - 1| + |8 - 9| = 2.
    Suppose we exclude the last worker who has an efficiency of 9, because we think that the
    largest inefficiency is bad. In that case, we have (4, 2, 8, 1), and you won’t be able to get a
    cost that’s lower than 2.
    This is the minimum possible cost so return 2.
    Task
    What is the minimum cost of this array of efficiencies:
    [1, 3, 54, 712, 52, 904, 113, 12, 135, 32, 31, 56, 23, 79, 611, 123, 677, 232, 997, 101, 111,
    123, 2, 7, 24, 57, 99, 45, 666, 42, 104, 129, 554, 335, 876, 35, 15, 93, 13]

* **Solution**

![image](https://github.com/E-STAT/AngelHack_May_Challenge/assets/54026058/51e86f8d-c0e3-4d4f-9b21-f683f1f5b4e5)



The minimum cost is 475

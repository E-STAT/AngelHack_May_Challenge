from json.tool import main


floor ='''
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
'''


def count_floor(floor_mov: str):
    """Calculate John's current floor based on a string of floor movement.

    Args:
        floor_mov (str): A string representing John's floor movements, with
        '<' representing a move down one floor and '>' representing a move up
        one floor.

    Returns:
        int: John's current floor after following the movements in `floor_mov`.
    """
    step = 0

    for f in floor_mov:
        if f == '<':
            step += 1
        if f == '>':
            step -= 1

    return step



if __name__ == "__main__":

    floor_no = count_floor(floor_mov = floor)
    print(f"John is currently on {floor_no}th floor ")



    

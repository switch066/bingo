import random

SHAPE = 5

def bingo_card():
    number_range = [
            [1,15],
            [16, 30],
            [31, 45],
            [46, 60],
            [61, 75],
    ]
    bingo_card = []
    for row in range(SHAPE):
        random_number = random.sample(range(number_range[row][0], number_range[row][1] + 1), SHAPE)
        bingo_card.append(random_number)

    bingo_card[2][2] = "Free"

    return list(map(list, zip(*bingo_card)))

def print_card(card):
    for row in card:
        print(" ".join(str(num).zfill(2) if isinstance(num, int) else  num for num in row))


def convert_to_number(value):
    if isinstance(value, str) and value.startswith('(') and value.endswith(')'):
        return int(value[1:-1])
    else:
        return value

def check_mark(marks, item, reach_lines, bingo_lines):
    if marks == SHAPE - 1:
        if item not in reach_lines:
            reach_lines.append(item)
    elif marks == SHAPE:
        if item not in bingo_lines:
            bingo_lines.append(item)
        if item in reach_lines:
            reach_lines.remove(item)

def roll():
    card = bingo_card()
    number_storage = []
    bingo_lines = []
    reach_lines = []
    balls = [i for i in range(1, 76)]
    random.shuffle(balls)
    while True:
        draw_number = balls.pop()
        number_storage.append(draw_number)
        print(f"ball[{len(number_storage)}]: {draw_number}")
        for lists in card:
            for index, number in enumerate(lists):
                if draw_number == number:
                    lists[index] = f"({str(number).zfill(2)})"

        for col in range(SHAPE):
            row_marks = sum(isinstance(card[col][row], str) for row in range(SHAPE))
            row_item = [convert_to_number(card[col][row]) for row in range(SHAPE)]
            check_mark(row_marks, item=row_item, reach_lines=reach_lines, bingo_lines=bingo_lines)

        for col in range(SHAPE):
            col_marks = sum(isinstance(card[row][col], str) for row in range(SHAPE))
            col_item = [convert_to_number(card[row][col]) for row in range(SHAPE)]
            check_mark(col_marks, item=col_item, reach_lines=reach_lines, bingo_lines=bingo_lines)
            
        diag1 = sum(isinstance(card[i][i], str) for i in range(SHAPE))
        diag1_item = [convert_to_number(card[i][i]) for i in range(SHAPE)]
        check_mark(diag1, item=diag1_item, reach_lines=reach_lines, bingo_lines=bingo_lines)
                    
        diag = [
            [0,4],
            [1,3],
            [2,2],
            [3,1],
            [4,0]
        ]

        diag2 = sum(isinstance(card[row][column], str) for row, column in diag)
        diag2_item = [convert_to_number(card[row][column]) for row, column in diag]
        check_mark(diag2, item=diag2_item, reach_lines=reach_lines, bingo_lines=bingo_lines)
            
        print_card(card)
        print(f"REACH: {len(reach_lines)}")
        print(f"BINGO: {len(bingo_lines)}")
        print("----------------")

        if all(isinstance(number, str) for lists in card for number in lists):
            break
        
roll()
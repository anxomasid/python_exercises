from enum import Enum

class Movement(Enum):
    DOWN = 1
    RIGHT = 2
    LEFT = 3
    ROTATE = 4

def tetris():

    screen = [['🔲', '🔲', '🔲', '🔲', '🔲', '🔲', '🔲', '🔲', '🔲', '🔲'],
              ['🔲', '🔳', '🔳', '🔲', '🔲', '🔲', '🔲', '🔲', '🔲', '🔲'],
              ['🔲', '🔲', '🔲', '🔲', '🔲', '🔲', '🔲', '🔲', '🔲', '🔲'],
              ['🔲', '🔲', '🔲', '🔲', '🔲', '🔲', '🔲', '🔲', '🔲', '🔲'],
              ['🔲', '🔲', '🔲', '🔲', '🔲', '🔲', '🔲', '🔲', '🔲', '🔲'],
              ['🔲', '🔲', '🔲', '🔲', '🔲', '🔲', '🔲', '🔲', '🔲', '🔲'],
              ['🔲', '🔲', '🔲', '🔲', '🔲', '🔲', '🔲', '🔲', '🔲', '🔲'],
              ['🔲', '🔲', '🔲', '🔲', '🔲', '🔲', '🔲', '🔲', '🔲', '🔲'],
              ['🔲', '🔲', '🔲', '🔲', '🔲', '🔲', '🔲', '🔲', '🔲', '🔲'],
              ['🔲', '🔲', '🔲', '🔲', '🔲', '🔲', '🔲', '🔲', '🔲', '🔲']]
    
    print_screen(screen)
    move_piece(Movement.DOWN, screen)

def print_screen(screen: list):
    print('\n Pantalla Tetris:\n')
    for row in screen:
        print(''.join(map(str, row)))

def move_piece(movement: Movement, screen: list):

    new_screen = [['🔲'] * 10 for _ in range(10)]

    for row_index, row in enumerate(screen):
        for col_index, item in enumerate(row):
            if item == '🔳':

                new_row_index = 0
                new_col_index = 0

                match movement:
                    case Movement.DOWN:
                        new_row_index = row_index + 1
                        new_col_index = col_index

                    case Movement.RIGHT:
                        break
                    case Movement.LEFT:
                        break
                    case Movement.ROTATE:
                        break    
                
                new_screen[new_row_index][new_col_index] = '🔳'
    print_screen(new_screen)
    
tetris()
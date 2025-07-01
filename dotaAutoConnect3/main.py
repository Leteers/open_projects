import pyautogui
import numpy as np
from PIL import Image
from pynput import keyboard
import threading

# Захват скриншота

FIELD_WIDTH = 720
FIELD_HEIGTH = 720

MARGIN_LEFT = 208
MARGIN_TOP = 115

LEFT_TOP = (223, 130)
RIGHT_BOT = (943, 850)


LEFT = 226
RIGHT = 943

TOP = 137
BOT = 853

def move_up(game_field: np.array ,rgb: tuple, cur_pos: tuple) ->bool:
    global square_height
    global square_width
    if cur_pos[0]-square_height*3 > 0 and is_close(rgb,game_field[(cur_pos[0]-square_height*2,cur_pos[1])]) and is_close(rgb,game_field[(cur_pos[0]-square_height*3,cur_pos[1])]):
        return True
    elif cur_pos[0]-square_height>0 and cur_pos[1]-square_width*2>0 and is_close(rgb,game_field[(cur_pos[0]-square_height,cur_pos[1]-square_width)]) and is_close(rgb,game_field[(cur_pos[0]-square_height,cur_pos[1]-square_width*2)]):
        return True
    elif cur_pos[0]-square_height>0 and cur_pos[1]+square_width*2<RIGHT_BOT[0] - LEFT_TOP[0] and is_close(rgb,game_field[(cur_pos[0]-square_height,cur_pos[1]+square_width)]) and is_close(rgb,game_field[(cur_pos[0]-square_height,cur_pos[1]+square_width*2)]):
        return True
    else:
        return False
    
def move_down(game_field: np.array ,rgb: tuple, cur_pos: tuple):
    global square_height
    global square_width
    if cur_pos[0]+square_height*3 > 0 and is_close(rgb,game_field[(cur_pos[1],cur_pos[0]+square_height*2)]) and is_close(rgb,game_field[(cur_pos[1],cur_pos[0]+square_height*3)]):
        return True
    elif cur_pos[0]+square_height<RIGHT_BOT[1]-LEFT_TOP[1] and cur_pos[1]-square_width*2>0 and is_close(rgb,game_field[(cur_pos[1]-square_width,cur_pos[0]+square_height)]) and is_close(rgb,game_field[(cur_pos[1]-square_width*2,cur_pos[0]+square_height)]):
        return True
    elif cur_pos[0]+square_height<RIGHT_BOT[1]-LEFT_TOP[1] and cur_pos[1]+square_width*2<RIGHT_BOT[0] - LEFT_TOP[0] and is_close(rgb,game_field[(cur_pos[1]+square_width,cur_pos[0]+square_height)]) and is_close(rgb,game_field[(cur_pos[1]+square_width*2,cur_pos[0]+square_height)]):
        return True
    else:
        return False



def is_close(rgb1: tuple,rgb2: tuple) -> bool:
    rgb1_int = [int(value) for value in rgb1]
    rgb2_int = [int(value) for value in rgb2]

    if sum([abs(rgb1_int[i] - rgb2_int[i]) for i in range(len(rgb1_int))]) > 120:
        return False
    else:
        return True

def return_mean(rgb_list:list) ->float:
    result_list = []
    for i in range(len(rgb_list)):
        for k in range(i+1,len(rgb_list)):
            result_list.append(sum([abs(rgb_list[i][j]-rgb_list[k][j]) for j in range(len(rgb_list[k]))]))
    print(result_list)
    return sum(result_list)/len(result_list)

def divide_area(width, height, num_parts):
    if num_parts != 8:
        raise ValueError("This function only supports dividing into 8 parts")

    # Разделение на 2 строки и 4 столбца (или можно на 4 строки и 2 столбца, в зависимости от предпочтений)
    num_rows = 8
    num_cols = 8

    # Размеры каждого квадрата
    global square_width
    square_width = width // num_cols
    global square_height
    square_height = height // num_rows

    return [(row * square_height+ square_height//3,col * square_width + square_width//2)
            for row in range(num_rows)
            for col in range(num_cols)]

    # return [(row * square_height,col * square_width)
    #         for row in range(num_rows)
    #         for col in range(num_cols)]


# Пример использования
width = RIGHT_BOT[0] - LEFT_TOP[0]
height = RIGHT_BOT[1]-LEFT_TOP[1]
num_parts = 8

squares = divide_area(width, height, num_parts)
# for i, (x, y) in enumerate(squares):
#     print(f"Square {i+1}: Start at ({x}, {y})")

GAME_FIELD = pyautogui.screenshot(region=(
    LEFT_TOP[0], LEFT_TOP[1], RIGHT_BOT[0]-LEFT_TOP[0], RIGHT_BOT[1]-LEFT_TOP[1]),)
GAME_FIELD = np.array(GAME_FIELD)


print(len(GAME_FIELD))

color_dict = {}
for i, (x, y) in enumerate(squares):
    square = (x,y)
    # print((x,y))
    # square_image = pyautogui.screenshot(region=(LEFT_TOP[0]+y,LEFT_TOP[1]+x,90,90))
    # square_image = np.array(square_image)
    # image = Image.fromarray(square_image)
    # image.show()
    # GAME_FIELD[square] = np.array((255,255,255))
    # print(tuple(GAME_FIELD[square]))
    
    if move_up(GAME_FIELD,tuple(GAME_FIELD[square]),square):
        print(f"Row: {x//90} Column: {y//90} : Start at ({x}, {y})")
# for square in squares:
#     if tuple(GAME_FIELD[square]) in color_dict.keys():
#         color_dict[tuple(GAME_FIELD[square])] += 1
#     else:
#         color_dict[tuple(GAME_FIELD[square])] = 1
# print(len(color_dict.keys()))
# print(color_dict.keys())
# image = Image.fromarray(GAME_FIELD)
# image.show()

# # Переменная для отслеживания состояния клавиши
key_pressed = False


def on_release(key):
    global key_pressed
    if key == keyboard.Key.esc:
        # Остановка слушателя при нажатии клавиши Escape
        return False


def on_press(key):
    global key_pressed
    try:
        if key.char == 'q':  # Пример действия при нажатии клавиши 'q'
            print("Key 'q' pressed")
            key_pressed = True
    except AttributeError:
        pass

# Функция для запуска слушателя в отдельном потоке


def start_listener():
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()


# Запуск слушателя в отдельном потоке
listener_thread = threading.Thread(target=start_listener)
listener_thread.start()

# Основная программа

if __name__ == '__main__':
    while True:
        if key_pressed:
            break
        print(1)

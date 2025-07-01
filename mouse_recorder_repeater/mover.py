import pyautogui
import pickle
import time
from pynput import keyboard
import threading

start_replay = False
stop_program = False

def on_press(key):
    global start_replay, stop_program
    try:
        if key.char == 'q':
            print("Повтор координат запущен.")
            start_replay = True
        elif key.char == 's':
            print("Повтор координат остановлен.")
            start_replay = False
    except AttributeError:
        if key == keyboard.Key.esc:
            stop_program = True
            print("Выход из программы...")
            return False

def start_listener():
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

def replay_coords():
    global start_replay
    try:
        with open("coords.pkl", "rb") as f:
            coords = pickle.load(f)
    except FileNotFoundError:
        print("Файл coords.pkl не найден.")
        return

    interval = 0.1  # интервал между перемещениями

    while not stop_program:
        if start_replay:
            print("Зажимаю ПКМ...")
            pyautogui.mouseDown(button='right')  # Зажимаем ПКМ

            for pos in coords:
                if not start_replay or stop_program:
                    break
                pyautogui.moveTo(pos)
                print(f"Перемещение в: {pos}")
                time.sleep(interval)

            pyautogui.mouseUp(button='right')  # Отпускаем ПКМ
            print("ПКМ отпущена.")
            start_replay = False  # Авто-остановка после одного прохода
        time.sleep(0.1)

if __name__ == '__main__':
    replay_thread = threading.Thread(target=replay_coords)
    replay_thread.start()

    listener_thread = threading.Thread(target=start_listener)
    listener_thread.start()

    listener_thread.join()
    replay_thread.join()

import pyautogui
import pickle
from pynput import keyboard
import threading
import time

collecting = False  # Флаг начала/остановки сбора координат
coordinates = []    # Список координат
stop_program = False  # Для выхода из программы


def toggle_collecting():
    global collecting
    collecting = not collecting
    if collecting:
        print("Сбор координат начался...")
    else:
        print("Сбор координат остановлен. Сохраняю в файл...")
        with open("coords.pkl", "wb") as f:
            pickle.dump(coordinates, f)
        print("Координаты сохранены в coords.pkl")


def on_press(key):
    global stop_program
    try:
        if key.char == 'q':
            toggle_collecting()
    except AttributeError:
        if key == keyboard.Key.esc:
            stop_program = True
            print("Выход из программы...")
            return False  # Остановить слушатель


def start_listener():
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()


def collect_mouse_coords():
    while not stop_program:
        if collecting:
            pos = pyautogui.position()
            coordinates.append(pos)
            print(f"Текущая позиция: {pos}")
        time.sleep(0.1)  # Интервал между записями


if __name__ == '__main__':
    # Поток для сбора координат мыши
    collector_thread = threading.Thread(target=collect_mouse_coords)
    collector_thread.start()

    # Поток для клавиатурного слушателя
    listener_thread = threading.Thread(target=start_listener)
    listener_thread.start()

    # Ждём завершения
    listener_thread.join()
    collector_thread.join()
import os
import time
import shutil

def rename_and_move_files():
    dir_path = r"D:/STORAGE/CONVERSION_AI_PLT/Out_Varya/"
    mask = ".plt"
    suffix = "_Varya"
    output_dir = r"D:/STORAGE/CONVERSION_AI_PLT/OUTPUT_PLT"

    # dir_path = r"C:/Users/fn111/Desktop/test1"
    # mask = ".txt"
    # suffix = "_Varya"
    # output_dir = r"C:/Users/fn111/Desktop/test2"

    
    while True:
        # Получаем список файлов с указанным расширением
        files = [f for f in os.listdir(dir_path) if f.endswith(mask)]
        
        # Переименовываем файлы
        for file_name in files:
            base_name, ext = os.path.splitext(file_name)
            new_name = f"{base_name}{suffix}{ext}"
            old_file = os.path.join(dir_path, file_name)
            new_file = os.path.join(dir_path, new_name)
            os.rename(old_file, new_file)
        
        # Перемещаем файлы
        for file_name in files:
            new_file_name = f"{os.path.splitext(file_name)[0]}{suffix}{mask}"
            if os.path.exists(output_dir+'/'+new_file_name):
                os.remove(output_dir+'/'+new_file_name)
            shutil.move(os.path.join(dir_path, new_file_name),output_dir)
        
        # Ждем 3 секунды перед повтором
        time.sleep(3)

if __name__ == "__main__":
    rename_and_move_files()
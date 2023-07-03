from ctypes import windll

GetAsyncKeyState = windll.user32.GetAsyncKeyState

VM_LBUTTON = 0x01

def foo():
    print("Кнопка нажата!")

while True:
    if GetAsyncKeyState(VM_LBUTTON):
        print(GetAsyncKeyState(VM_LBUTTON))
    else:
        print(GetAsyncKeyState(VM_LBUTTON))
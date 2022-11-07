from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle
from lab_python_oop.square import Square
from tkinter import Tk, Frame, Label, BOTH, X

N = 15

def main():
    r = Rectangle("синего", N, N)
    c = Circle("зеленого", N)
    s = Square("красного", N)
    print(r)
    print(c)
    print(s)

    tk = Tk()
    tk.title("Lab2")
    tk.geometry("500x250")
    frame = Frame(tk, borderwidth=50)
    frame.pack(fill=BOTH, expand=1)
    label = Label(frame, text="Hello, World!")
    label.pack(fill=X, expand=1)

    tk.mainloop()

if __name__ == "__main__":
    main()
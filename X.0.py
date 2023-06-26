import tkinter as tk
root = tk.Tk()
root.title("X.O")

root.resizable(False,False)

def point():
    board_frame = tk.Frame(root)
    board_frame.grid(row=0)
    label_1 = tk.Label(board_frame,text="بازیکن 1",font=("Aviny",16),padx=10)
    label_2 = tk.Label(board_frame, text="بازیکن 2", font=("Aviny", 16), padx=10)
    label_1.grid(row=0,column=0)
    label_2.grid(row=0,column=2)

    point_frame = tk.Frame(root)
    point_frame.grid(row=1)
    point_player_1 = tk.Label(point_frame,text="0",padx=20,font=("Aviny",18))
    point_player_2 = tk.Label(point_frame, text="0", padx=20, font=("Aviny", 18))
    point_player_1.grid(row=0,column=0)
    point_player_2.grid(row=0,column=1)

def board():
    buttons = []
    counter = 0
    board_frame = tk.Frame(root)
    board_frame.grid(row=2)
    for row in range(1,4):
        for column in range(1,4):
            index = counter
            buttons.append(index)
            buttons[index] = tk.Button(board_frame)
            buttons[index].config(width=10,height=4,font=("None",18,"bold"))
            buttons[index].grid(row=row,column=column)
            counter +=1

board()
point()


root.mainloop()
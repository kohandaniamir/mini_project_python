from tkinter import *
from random import randint
import sys
import os
# -------------------------------
game_withe = 700
game_height = 600
bodysnake = 3
background = "black"
space_size = 20
speed_snake = 150
snake_color = "blue"
food_color = "red"
score = 0
first_move = "down"

# ==================================
def restart_program():
    path = sys.executable
    os.execl(path,path, *sys.argv)

# ==================================
root = Tk()
root.title("snake game")
root.resizable(width=False,height=False)
label_1 = Label(root,text=f"score {score}",font=("Latha",20))
label_1.pack()
root.resizable(False,False)
# ==============================================================
canvas = Canvas(root,bg=background,height=game_height,width=game_withe)
canvas.pack()
restart = Button(root,text="RESTART",fg="red",command=restart_program,width=10,height=10,font=("Arial"))
restart.pack()
# ===============================================================

root.geometry(f"{705}x{680}+{400}+{50}")

#================================================================

class Snake:
    def __init__(self):
        self.bodysize = bodysnake
        self.coordinates = []
        self.squares = []
        for i in range(0, bodysnake):
            self.coordinates.append([0,0])
        for x , y in self.coordinates:
            squre=canvas.create_rectangle(x,y,x + space_size,y+space_size,fill=snake_color,tag="snake")
            self.squares.append(squre)
snake = Snake()

class Food:
    def __init__(self):
        x= randint(0,(game_withe // space_size) - 1) * space_size
        y= randint(0,(game_height // space_size) - 1) * space_size
        self.coordinates=[x,y]
        canvas.create_rectangle(x,y,x+space_size,y+space_size,fill=food_color,tag="food")


# ===================================================================

def next_move(snake,food):
    x , y = snake.coordinates[0]
    if first_move == "up":
        y -= space_size
    elif first_move == "down":
        y += space_size
    elif first_move == "left":
        x -= space_size
    elif first_move == "right":
        x += space_size

    snake.coordinates.insert(0,[x,y])
    squre = canvas.create_rectangle(x,y,x+space_size,y+space_size,fill=snake_color)
    snake.squares.insert(0,squre)
    if x == food.coordinates[0] and y == food.coordinates[1]:
        global score
        score += 1
        label_1.config(text=f"Score : {score}")
        canvas.delete("food")
        food = Food()
    else:
        del snake.coordinates[-1]
        canvas.delete(snake.squares[-1])
        del snake.squares[-1]

    if check_game_over(snake):
        game_over()
    else:
        root.after(speed_snake,next_move,snake,food)




def check_game_over(snake):
    x , y = snake.coordinates[0]
    if x < 0 or x > game_withe:
        return True
    if y < 0 or y > game_height:
        return True
    for i in snake.coordinates[1:]:
        if x == i[0] and y == i[1]:
            return True
    return False


def game_over():
    canvas.delete(ALL)
    canvas.create_text(canvas.winfo_width() / 2 ,canvas.winfo_height() / 2,font=("Terminal", 60)
                       , text="GAME OVER!", fill="#DF1A2F", tag="gameover")


def chnage_direction(new_dir):
    global first_move
    if new_dir == "left":
        if first_move != "right":
            first_move=new_dir
    elif new_dir == "right":
        if first_move != "left":
            first_move = new_dir
    elif new_dir == "up":
        if first_move != "down":
            first_move = new_dir
    elif new_dir == "down":
        if first_move != "up":
            first_move = new_dir

# ===================================================================

root.bind("<Left>",lambda event:chnage_direction("left"))
root.bind("<Right>",lambda event:chnage_direction("right"))
root.bind("<Up>",lambda event:chnage_direction("up"))
root.bind("<Down>",lambda event:chnage_direction("down"))

# ===================================================================
food = Food()

next_move(snake,food)



root.update()
root.mainloop()
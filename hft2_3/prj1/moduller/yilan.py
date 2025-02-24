import tkinter as tk
import random

class SnakeGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Yılan Oyunu")
        self.master.resizable(False, False)

        self.canvas = tk.Canvas(self.master, width=400, height=400, bg="white")
        self.canvas.pack()

        self.snake = [(20, 20), (20, 30), (20, 40)]
        self.food = self.create_food()
        self.direction = "Down"
        self.running = True

        self.master.bind("<KeyPress>", self.change_direction)
        self.update()

    def create_food(self):
        while True:
            x = random.randint(0, 39) * 10
            y = random.randint(0, 39) * 10
            if (x, y) not in self.snake:
                return (x, y)

    def change_direction(self, event):
        if event.keysym in ["Up", "Down", "Left", "Right"]:
            self.direction = event.keysym

    def update(self):
        if self.running:
            self.move_snake()
            self.check_collision()
            self.check_food()
            self.draw_elements()
            self.master.after(100, self.update)

    def move_snake(self):
        head_x, head_y = self.snake[-1]
        if self.direction == "Up":
            new_head = (head_x, head_y - 10)
        elif self.direction == "Down":
            new_head = (head_x, head_y + 10)
        elif self.direction == "Left":
            new_head = (head_x - 10, head_y)
        elif self.direction == "Right":
            new_head = (head_x + 10, head_y)
        self.snake.append(new_head)
        self.snake.pop(0)

    def check_collision(self):
        head_x, head_y = self.snake[-1]
        if head_x < 0 or head_x >= 400 or head_y < 0 or head_y >= 400 or len(self.snake) != len(set(self.snake)):
            self.running = False
            self.canvas.create_text(200, 200, text="Oyun Bitti", fill="red", font=("Arial", 24))

    def check_food(self):
        if self.snake[-1] == self.food:
            self.snake.insert(0, self.snake[0])
            self.food = self.create_food()

    def draw_elements(self):
        self.canvas.delete(tk.ALL)
        for x, y in self.snake:
            self.canvas.create_rectangle(x, y, x + 10, y + 10, fill="green")
        food_x, food_y = self.food
        self.canvas.create_rectangle(food_x, food_y, food_x + 10, food_y + 10, fill="red")

def yilanmenu():
    root = tk.Tk()
    game = SnakeGame(root)
    root.mainloop()

if __name__ == "__main__":
    yilanmenu()
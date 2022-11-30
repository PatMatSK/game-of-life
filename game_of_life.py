import tkinter as tk

root = tk.Tk()
root.title("Game of Life")
test = True
canvas_width = 1000
canvas_height = 500
row = 20
column = 50
square = 20
canvas = tk.Canvas(root, width=canvas_width, heigh=canvas_height)
canvas.pack()
life = [[0] * column for _ in range(row)]
new_life = [[0] * column for _ in range(row)]


def drow_net():
    for i in range(row + 1):
        canvas.create_line(0, i * square, column * square, i * square)
    for i in range(column + 1):
        canvas.create_line(i * square, 0, i * square, row * square)


def lets_live(event):
    global life
    if event.x < column * square and event.y < row * square:
        x = (event.x // square) * square
        y = (event.y // square) * square
        canvas.create_oval(x, y, x + square, y + square, fill="blue")
        x1 = event.x // square
        y1 = event.y // square
        life[y1][x1] = 1


def edit_life(life):
    global test, edited
    edited = life
    if test:
        edited.append([9] * (column + 2))
        edited[-len(edited):0] = ([[9] * (column + 2)])
        for i in range(1, len(edited) - 1):
            edited[i].append(9)
            edited[i][-len(edited[i]):0] = [9]
        test = False
        return edited


def get_neigh(x, y):
    global row, column, edited
    count = 0
    if edited[x + 1][y] == 1:
        count += 1
    if edited[x - 1][y] == 1:
        count += 1
    if edited[x][y + 1] == 1:
        count += 1
    if edited[x][y - 1] == 1:
        count += 1
    if edited[x - 1][y - 1] == 1:
        count += 1
    if edited[x + 1][y - 1] == 1:
        count += 1
    if edited[x + 1][y + 1] == 1:
        count += 1
    if edited[x - 1][y + 1] == 1:
        count += 1
    return count


def super_nova(to_live):
    global life, test, new_life
    canvas.delete("all")
    drow_net()
    x, y = 0, 0
    for i in to_live:
        x = 0
        for cell in i:
            if cell == 1:
                canvas.create_oval(x, y, x + square, y + square, fill="blue")
            x += square
        y += square
    life = new_life
    test = True
    new_life = [[0] * column for _ in range(row)]


def game():
    global edited
    edit_life(life)
    for x in range(1, len(edited) - 1):
        for y in range(1, len(edited[x]) - 1):
            if edited[x][y] == 1 and (get_neigh(x, y) == 3 or get_neigh(x, y) == 2):
                new_life[x - 1][y - 1] = 1
            elif edited[x][y] == 0 and get_neigh(x, y) == 3:
                new_life[x - 1][y - 1] = 1
    super_nova(new_life)


drow_net()

button1 = tk.Button(root, text="NEXT GENERATION", command=game)
button1.pack()
canvas.bind("<Button-1>", lets_live)

root.mainloop()

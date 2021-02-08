import tkinter as tk

CANVAS_WIDTH, CANVAS_HEIGHT = 600, 600
x1 = 280
coté = 60 
x2 = x1 + coté
name1 = "Pause"
root = tk.Tk()
root.title("Mon Interface graphique")


#def fonction
def appuyer_sur_pause():
    if name1 == "Pause":
        name1 = "Restart"
    else:
        name1 == "Pause"
    return name1
    


def appuyer_sur_carré():
    if coté >= 20:
        coté =- 10
    return coté
    


def appuyer_sur_canvas():
    if coté <= 120:
        coté =+ 10
    return coté




#labels 
canvas = tk.Canvas(root, bg="blue", bd=10, relief="ridge", width=CANVAS_WIDTH, height=CANVAS_HEIGHT)
pause = tk.Button(root, text=name1, command=appuyer_sur_pause, activeforeground="blue", overrelief="ridge", font="overstrike")
canvas.create_oval(x1, x1, x2, x2, fill="yellow")


#emplacements
canvas.grid(column=0, row=0, rowspan=3, columnspan=3)
pause.grid(column=1, row=4)



root.mainloop()
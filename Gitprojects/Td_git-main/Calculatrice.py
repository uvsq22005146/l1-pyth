import tkinter as tk

CANVAS_WIDTH, CANVAS_HEIGHT = 500, 500
root = tk.Tk()
root.title("Ma Calculatrice")


#def (ici tu pourras coder les fonctions qui seront utiles.)
def appuyer_sur_0():
    pass 

def appuyer_sur_1():
    pass

def appuyer_sur_2():
    pass

def appuyer_sur_3():
    pass

def appuyer_sur_4():
    pass

def appuyer_sur_5():
    pass

def appuyer_sur_6():
    pass

def appuyer_sur_7():
    pass

def appuyer_sur_8():
    pass

def appuyer_sur_9():
    pass

def appuyer_sur_plus():
    pass

def appuyer_sur_moins():
    pass

def appuyer_sur_multi():
    pass

def appuyer_sur_div():
    pass

def appuyer_sur_suppr():
    pass

def appuyer_sur_calc():
    pass



#labels (ici je vais coder les différents lables nécessaires.)
canvas = tk.Canvas(root, bg="black", bd=10, relief="ridge")
zero = tk.Button(root, text="0", command=appuyer_sur_0, activeforeground="blue", overrelief="ridge", font="overstrike")
un = tk.Button(root, text="1", command=appuyer_sur_1, activeforeground="blue", overrelief="ridge", font="overstrike")
deux = tk.Button(root, text="2", command=appuyer_sur_2, activeforeground="blue", overrelief="ridge", font="overstrike")
trois = tk.Button(root, text="3", command=appuyer_sur_3, activeforeground="blue", overrelief="ridge", font="overstrike")
quatre = tk.Button(root, text="4", command=appuyer_sur_4, activeforeground="blue", overrelief="ridge", font="overstrike")
cinq = tk.Button(root, text="5", command=appuyer_sur_5, activeforeground="blue", overrelief="ridge", font="overstrike")
six = tk.Button(root, text="6", command=appuyer_sur_6, activeforeground="blue", overrelief="ridge", font="overstrike")
sept = tk.Button(root, text="7", command=appuyer_sur_7, activeforeground="blue", overrelief="ridge", font="overstrike")
huit = tk.Button(root, text="8", command=appuyer_sur_8, activeforeground="blue", overrelief="ridge", font="overstrike")
neuf = tk.Button(root, text="9", command=appuyer_sur_9, activeforeground="blue", overrelief="ridge", font="overstrike")
plus = tk.Button(root, text="+", command=appuyer_sur_plus, activeforeground="blue", overrelief="ridge", font="overstrike")
moins = tk.Button(root, text="-", command=appuyer_sur_moins, activeforeground="blue", overrelief="ridge", font="overstrike")
div = tk.Button(root, text="/", command=appuyer_sur_div, activeforeground="blue", overrelief="ridge", font="overstrike")
multi = tk.Button(root, text="*", command=appuyer_sur_multi, activeforeground="blue", overrelief="ridge", font="overstrike")
efface = tk.Button(root, text="Effacer", command=appuyer_sur_suppr, activeforeground="blue", overrelief="ridge", font="overstrike")
calc = tk.Button(root, text="Calculer", command=appuyer_sur_calc, activeforeground="blue", overrelief="ridge", font="overstrike")


#emplacements (ici je définirais les emplacements des différents labels.)
canvas.grid(column=0, row=0, rowspan=3, columnspan=3)
zero.grid(column=0, row=4)
deux.grid(column=1, row=4)
trois.grid(column=2, row=4)
quatre.grid(column=0, row=5)
cinq.grid(column=1, row=5)
six.grid(column=2, row=5)
sept.grid(column=0, row=6)
huit.grid(column=1, row=6)
neuf.grid(column=2, row=6)
plus.grid(column=1, row=8)
moins.grid(column=2, row=8)
multi.grid(column=1, row=9)
div.grid(column=2, row=9)
efface.grid(column=0, row=10)
calc.grid(column=2, row=10, columnspan=2)


root.mainloop()
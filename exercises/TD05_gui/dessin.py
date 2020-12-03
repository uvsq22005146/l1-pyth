import tkinter as tk

CANVAS_WIDTH, CANVAS_HEIGHT = 600, 400
root = tk.Tk()
root.title("Mon dessin")

#def 

#labels
canvas = tk.Canvas(root, bg="black", bd=10, relief="ridge")
couleur = tk.Button(root, text="Choisir couleur", activeforeground="blue", overrelief="ridge", font="overstrike")
cercle = tk.Button(root, text="Cercle", activeforeground="blue", overrelief="ridge", font="overstrike")
carre = tk.Button(root, text="Carré", activeforeground="blue", overrelief="ridge", font="overstrike")
croix = tk.Button(root, text="Croix", activeforeground="blue", overrelief="ridge", font="overstrike")

#emplacements
couleur.grid(column=1, row=0)
cercle.grid(column=0, row=1)
carre.grid(column=0, row=2)
croix.grid(column=0, row=3)
canvas.grid(column=1, row=1, rowspan=3)

root.mainloop()

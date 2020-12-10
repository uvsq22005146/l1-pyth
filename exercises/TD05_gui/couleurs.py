import tkinter as tk
import random as rd

CANVAS_WIDTH, CANVAS_HEIGHT = 256, 256
root = tk.Tk()
root.title("Mes Couleurs")

#def 
def get_color(r, g, b):
    """ Retourne une couleur à partir de ses composantes r, g, b entre 0 et 255"""
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)

def draw_pixel(i, j, color): 
    """colorie le pixel de coordonée (i, j)"""
    canvas.create_line((i, j), (i+1, j), fill=color)

def ecran_aleatoire():
    for i in range(256):
        for j in range(256):
             color = get_color(rd.randint(0,255), rd.randint(0,255), rd.randint(0,255))
             draw_pixel(i, j, color)
            

def degrade_gris():
    for i in range(256):
        color = get_color((i), (i), (i))
        for j in range(256):
                draw_pixel(i, j, color)

def degrade_2D():
    for i in range(256):
                for j in range(256):
                    color = get_color((i), (0), (j))
                    draw_pixel(i, j, color)



#labels
canvas = tk.Canvas(root, bg="black", bd=10, relief="ridge")
aleatoire = tk.Button(root, text="Aléatoire", command=ecran_aleatoire, activeforeground="blue", overrelief="ridge", font="overstrike")
deg_gris = tk.Button(root, text="Dégradé Gris", command=degrade_gris, activeforeground="blue", overrelief="ridge", font="overstrike")
deg_2d = tk.Button(root, text="Dégradé 2D", command=degrade_2D, activeforeground="blue", overrelief="ridge", font="overstrike")

#emplacements
aleatoire.grid(column=0, row=0)
deg_gris.grid(column=0, row=1)
deg_2d.grid(column=0, row=2)
canvas.grid(column=1, row=0, rowspan=3)

root.mainloop()
import tkinter as tk

root = tk.Tk()
canvas = tk.Canvas(root, width=600, height=400, bg="white")
canvas.pack()
# canvas.create_rectangle(x1, y1, x2, y2, fill="color", outline="color")
canvas.create_rectangle(50, 100, 200, 150, fill="lightgreen", outline="green")
# Dibuja una elipse dentro del rectángulo delimitador.
canvas.create_oval(300, 100, 400, 200, fill="yellow", outline="orange")

# canvas.create_text(x, y, text="texto", fill="color", font=("fuente", tamaño))
canvas.create_text(300, 50, text="Diagrama de Flujo", fill="black", font=("Arial", 16))

# canvas.create_line(x1, y1, x2, y2, fill="color", width=grosor)
canvas.create_line(50, 50, 200, 50, fill="blue", width=3)

canvas.create_arc(400, 250, 500, 350, start=0, extent=90, fill="purple")

# canvas.create_oval(x1, y1, x2, y2, fill="color", outline="color")

img = tk.PhotoImage(file="foto01.jpg")
canvas.create_image(x, y, image=img, anchor="center")

canvas.create_line(200, 100, 200, 150, arrow="last")

root.mainloop()

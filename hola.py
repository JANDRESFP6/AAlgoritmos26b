import tkinter as tk
#Aqui va a ir la creacion de la funcion 
def saludar():
    nombre=entrada.get().strip()
    if not nombre:
        nombre="Jose Andres Flores Parra"
    lbl.config(text=f"Hola,{nombre}")

root = tk.Tk()
root.title("Saludador de compas")
root.geometry("360x220")
lbl= tk.Label(root, text="Hola, escribe tu nombre y presiona el boton")
lbl.pack(pady=30)#pady es el espacio de la posicion en Y
entrada=tk.Entry(root)
entrada.pack(pady=10)

#Creacion de boton 
btn=tk.Button(root,text="Saludar",command=saludar) 
btn.pack(pady=10)

root.mainloop()

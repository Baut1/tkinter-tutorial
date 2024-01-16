import tkinter as tk

app = tk.Tk()

palabra = tk.StringVar(app)
entrada = tk.StringVar(app)



app.geometry("600x300")
app.configure(background="black")
tk.Wm.wm_title(app, "Palabras")

def cambiarPalabra():
    palabra.set("the word is " + entrada.get())

tk.Button(
    app,
    text="click me",
    font=("Courier", 18),
    bg="#090999",
    fg="white",
    command=cambiarPalabra,
    relief="flat"
).pack(
    fill=tk.BOTH,
    expand=True
)

tk.Label(
    app,
    text="im a label",
    textvariable=palabra,
    fg="white",
    bg="black",
    justify="center"
).pack(
    fill=tk.BOTH,
    expand=True
)

tk.Entry(
    fg="white",
    bg="black",
    justify="center",
    textvariable=entrada
).pack(
    fill=tk.BOTH,
    expand=True
)

app.mainloop()
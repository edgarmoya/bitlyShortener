from tkinter import *
from bitly import *

raiz = Tk()
raiz.title("Acortador Bitly")
raiz.resizable(False, False)
raiz.iconbitmap("icono.ico")
raiz.config(bg="white")

frame = Frame(raiz, width="500", height="250")
frame.pack(side="left", anchor="n")
frame.config(bg="white")

long_url = StringVar()
short_url = StringVar()
uso = StringVar()

labelUsage = Label(frame, textvariable=uso, bg="white").grid(row=2, column=0, sticky="w", padx=10)
campoUrl = Entry(frame, width=45, textvariable=long_url).grid(row=0, column=1, padx=20, pady=20, columnspan=2)
labelUrl = Label(frame, text="Url a acortar:", bg="white").grid(row=0, column=0, sticky="w", padx=10)

campoUrlAcortado = Entry(frame, width=45, textvariable=short_url).grid(row=1, column=1, padx=20, pady=5, columnspan=2)
labelUrlAcortado = Label(frame, text="Url acortado:", bg="white").grid(row=1, column=0, sticky="w", padx=10)

# funcion para mostrar texto acortado
def acortar_url():
    if long_url.get() == "":
        short_url.set("ERROR")
    else:
        result = acortar(long_url.get())
        short_url.set(result)
    uso.set(uso_bitly())

# funcion para limpiar los campos
def limpiar_urls():
    long_url.set("")
    short_url.set("")

btnAcortar = Button(frame, width=15, text="Acortar", command=acortar_url).grid(row=2, column=1, pady=15)
btnLimpiar = Button(frame, width=15, text="Limpiar", command=limpiar_urls).grid(row=2, column=2, pady=15)

raiz.mainloop()

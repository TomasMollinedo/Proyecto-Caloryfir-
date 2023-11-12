from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.geometry("1300x800")
root.title("CaloryFit")

img = Image.open("Frame-final.jpg")
new_img = img.resize((1540,850))
render = ImageTk.PhotoImage(new_img)
img2 = Label(root, image = render)
img2.image = render
img2.place(x=0, y=0)

#-------------------------------------funciones-----------------------------

def imagen_subir():
    img = Image.open("subir.jpg")
    new_img = img.resize((450,100))
    render = ImageTk.PhotoImage(new_img)
    img2 = Label(root, image = render)
    img2.image = render
    img2.place(x=924, y=550)

def imagen_mantener():
    img = Image.open("mantener.jpg")
    new_img = img.resize((450,100))
    render = ImageTk.PhotoImage(new_img)
    img2 = Label(root, image = render)
    img2.image = render
    img2.place(x=924, y=550)

def imagen_bajar():
    img = Image.open("bajar-valido.jpg")
    new_img = img.resize((450,100))
    render = ImageTk.PhotoImage(new_img)
    img2 = Label(root, image = render)
    img2.image = render
    img2.place(x=924, y=550)

def calcula_mantenimiento():
    global peso
    global altura
    global edad

    peso_local = int(peso.get())
    altura_local = int(altura.get())
    edad_local = int(edad.get())

    TMBhombre = 10*peso_local + 6.25*altura_local - 5*edad_local + 5

    factor_actividad = valor.get()
    indice = lista_fisica.index(factor_actividad)

    if indice == 0:
        get = TMBhombre * 1.3
    elif indice == 1:
        get = TMBhombre * 1.5
    elif indice == 2:
        get = TMBhombre * 1.7
    elif indice == 3:
        get = TMBhombre * 1.9

    altura_metros = altura_local/100

    IMC = peso_local/(altura_metros**2)

    listareturn = [int(get), int(IMC)]
    
    return listareturn


def introducir(var,numero):
    var.config(state="normal")
    var.delete(0, END)
    var.insert(0,numero)
    var.config(state="readonly")

def cal_adicionales():
    objetivo = valor_2.get()
    if objetivo == "ganancia de peso":
        signo = "+"
    elif objetivo == "perdida de peso":
        signo = "-"
    else:
        signo = "#"
    
    cuanto_local = int(cuanto.get())
    if 0 <= cuanto_local <= 10:
        sumar = "300"
    else:
        sumar = "500"


    if signo == "+":
        cant_final = str(calcula_mantenimiento()[0]) + signo + sumar 
        listaa = cant_final.split("+")
        cantidad = str(int(listaa[0]) + int(listaa[1]))
        variable = cant_final + "=" + cantidad
    elif signo == "-":
        cant_final = str(calcula_mantenimiento()[0]) + signo + sumar
        listaa = cant_final.split("-")
        cantidad = str(int(listaa[0]) - int(listaa[1]))
        variable = cant_final + "=" + cantidad
    else:
        signo ="+"
        sumar = "0"
        cant_final = str(calcula_mantenimiento()[0]) + signo + sumar
        listaa = cant_final.split("+")
        cantidad = str(int(listaa[0]) + int(listaa[1]))
        variable = cantidad

    return variable




def aceptar():
    objetivo = valor_2.get()
    if objetivo == "ganancia de peso":
        imagen_subir()
    elif objetivo == "perdida de peso":
        imagen_bajar()
    else:
        imagen_mantener()
    
    introducir(calorias ,calcula_mantenimiento()[0])
    introducir(indice ,calcula_mantenimiento()[1])
    introducir(porcentaje, valor_4.get())
    introducir(cantidad, cal_adicionales())

#---------------------------------------------------------------------------

#--------inputs--------
peso = Entry(root, bg="grey80", width=20)
peso.insert(0,0)
peso.place(x=75,y=250)

altura = Entry(root, bg="grey80", width=20)
altura.insert(0,0)
altura.place(x=322,y=250)

edad = Entry(root, bg="grey80", width=20)
edad.insert(0,0)
edad.place(x=573,y=250)

lista_fisica = ["Sedentario", "Ligeramente activo", "Activo", "Muy activo"]
valor = StringVar()
valor.set(lista_fisica[0])
fisica_drop = OptionMenu(root, valor, *lista_fisica)
fisica_drop.config(width=54)
fisica_drop.place(x=75, y=370)

lista_objetivo = ["ganancia de peso", "perdida de peso", "mantener el peso"]
valor_2 = StringVar()
valor_2.set(lista_objetivo[0])
objetivo_drop = OptionMenu(root, valor_2, *lista_objetivo)
objetivo_drop.config(width=54)
objetivo_drop.place(x=75, y=480)

cuanto = Entry(root, bg="grey80", width=60)
cuanto.insert(0,0)
cuanto.place(x=75,y=590)

aceptar = Button(root, text="Aceptar", width=10, command=aceptar)
aceptar.place(x=220,y=730)

def imagen_mujer():
    img = Image.open("mujer.jpg")
    new_img = img.resize((300,400))
    render = ImageTk.PhotoImage(new_img)
    img2 = Label(root, image = render)
    img2.image = render
    img2.place(x=500, y=315)

def imagen_hombre():
    img = Image.open("hombree.jpg")
    new_img = img.resize((300,400))
    render = ImageTk.PhotoImage(new_img)
    img2 = Label(root, image = render)
    img2.image = render
    img2.place(x=500, y=315)

mujer = Button(root, text="Mujer", command=imagen_mujer)
mujer.place(x=500, y=730)

hombre = Button(root, text="Hombre", command=imagen_hombre)
hombre.place(x=748, y=730)

lista_grasa = ["1-4%", "5-7%", "8-10%", "11-12%", "13-15%", "16-19%", "20-24%", "25-30%", "35-40%"]
valor_4 = StringVar()
valor_4.set(lista_grasa[0])
grasa_drop = OptionMenu(root, valor_4, *lista_grasa)
grasa_drop.place(x=615, y=729)

calorias = Entry(root, bg="grey80", state="readonly")
calorias.place(x=1210, y=195)

porcentaje = Entry(root, bg="grey80", state="readonly")
porcentaje.place(x=1210, y=255)

indice = Entry(root, bg="grey80", state="readonly")
indice.place(x=1210, y=315)

cantidad = Entry(root, bg="grey80", state="readonly", width=67)
cantidad.place(x=925, y=450)

#-------------salir-------------
salir = Button(root, text="Salir", width=7, fg="white", bg="#353534", command=root.destroy)
salir.place(x=1305, y=40)

root.mainloop()
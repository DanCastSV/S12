from tkinter import Tk, Label, Button, Entry, Text, messagebox
from os import environ
from source.email import Email
from dotenv import load_dotenv

#se crea la ventana 
venatana = Tk()

#se pone el titulo, color y tamaño de la ventana 
venatana.title("Semana 12")
venatana.geometry("500x400")
venatana.config(bg="#5F6A6A")

#se crean los parametros de los objetos de la ventana
share = Label(venatana, text="Correo: ", font=14, bg="#5F6A6A")
user = Label(venatana, text="Usuario: ", font=14, bg="#5F6A6A")


ce = Entry(venatana, font= 14, bg="white")
user2 = Entry(venatana, font= 14, bg="white")
message1= Text(venatana, font= 14, bg="white")

#Se cre la estructura para HTML
html = """
<!DOCYPE html>
<html>
<body>
<h1>Estimado {}</h1>
<p>{}</p>
</body>
</html>
"""

load_dotenv()
#Se cre la funcion para enviar el correo 
def sendemail():
    correo = Email()
    correo.mandar_email([ce.get()], "Semana 12 Programacion", message_format=html.format(user2.get(), message1.get('1.0', 'end-1c')), format="html")
    messagebox.showinfo("Aviso", "El correo se ha enviado de manera sastifactoria.")

#se cre el bonton de envio
btnshare = Button(venatana, text="Enviar", command=sendemail, bg="#283747")

#se establecen los parametros de los objetos dentro de la ventana 

share.place(x=50, y=10)
ce.place(x=150, y=10, width=290)
user.place(x=50, y=60)
user2.place(x=150, y=60, width=290)
message1.place(x=60, y=110, width=380, height=225)
btnshare.place(x=60, y=350, width=380, height=40)

venatana.mainloop()


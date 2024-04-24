import customtkinter as ctk
import PIL
from PIL import Image,ImageTk
ventana = ctk.CTk()
ventana.title("Ruta De Buses Massay")
ventana.geometry("400x200")
ctk.set_appearance_mode("dark")


btn0 = ctk.CTkButton(ventana,text="Ruta De Buses",width=370, height=40)
btn0.place(x=10,y=10)




btn1 = ctk.CTkButton(ventana,text="Bus 1 ",width=100, height=30)
btn1.place(x=290,y=60)


btn2 = ctk.CTkButton(ventana,text="Bus 2 ",width=100, height=30)
btn2.place(x=290,y=100)

btn3 = ctk.CTkButton(ventana,text="Bus 3 ",width=100, height=30)
btn3.place(x=290,y=140)

btn4 = ctk.CTkButton(ventana,text="Bus 4",width=100, height=30)
btn4.place(x=290,y=180)


ventana.mainloop()


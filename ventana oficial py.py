from tkinter import Tk, Button

ventana = Tk()
ventana.title("Ruta De Buses Massay")
ventana.geometry("400x200")

btn0=Button(ventana,text="Ruta De Buses")
btn0.place(x=10,y=10, width=370, height=40)




btn1=Button(ventana,text="Bus 1 ")
btn1.place(x=290,y=60, width=100, height=30)


btn2=Button(ventana,text="Bus 2 ")
btn2.place(x=290,y=100, width=100, height=30)

btn3=Button(ventana,text="Bus 3 ")
btn3.place(x=290,y=140, width=100, height=30)

btn4=Button(ventana,text="Bus 4")
btn4.place(x=290,y=180, width=100, height=30)


ventana.mainloop()

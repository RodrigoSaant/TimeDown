#importando as bibliotecas

import os
import tkinter as tk
from PIL import Image, ImageTk
import time

from numpy import number



#Criando a janela do programa

abrir = tk.Tk() 
abrir.title('TimeDown') 
abrir.resizable(0,0) 
imagem = tk.PhotoImage(file='Fundo.png')
abrir.iconbitmap("Icone.ico")

w = abrir.winfo_reqwidth()
h = abrir.winfo_reqheight()
ws = abrir.winfo_screenwidth()
hs = abrir.winfo_screenheight()
x = (ws/2) - (w/1)
y = (hs/3) - (h/1)
abrir.geometry('+%d+%d' % (x, y))

mostrar = tk.Canvas(abrir,width=500,height=500)
mostrar.create_image(250,250,image=imagem)
mostrar.pack(expand = "yes")



input1 = tk.Entry(width=30,highlightthickness=0,justify='center',font='Verdana',)
mostrar.create_window(100,250,anchor='nw',window=input1)


#Definindo as funções do programa

def comecar():

        
  comando = int(input1.get())

  if  comando == int(input1.get()):

    os.system(f"shutdown /s /t {comando * 60}")

    abrir.destroy()


 

botao = tk.Button(abrir,width=20,text='Começar',font='Gotham',background='#87611A',cursor='hand2',command=lambda:comecar())
mostrar.create_window(252,320,window=botao)



abrir.mainloop()#Deixando em loop



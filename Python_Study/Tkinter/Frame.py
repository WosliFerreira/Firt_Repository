from tkinter import *

janela = Tk()
janela.title('Radio_Button')
janela.geometry('400x400')
janela.config(bg='black')


frame_nav = Frame(janela, width=400, height=40, bg='white')
frame_nav.grid(row=0, column=0, columnspan=3, padx=0, pady=2)

frame_esquerda = Frame(janela, width=100, height=260, bg='#d6d6d6')
frame_esquerda.grid(row=1, column=0)

frame_meio = Frame(janela, width=200, height=260, bg='white')
frame_meio.grid(row=1, column=1)

frame_direita = Frame(janela, width=100, height=260, bg='#d6d6d6')
frame_direita.grid(row=1, column=2)



janela.mainloop()

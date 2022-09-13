from tkinter import *


janela = Tk()
janela.title('Calculadora_V1')
janela.geometry('240x310')

# Frames --------------------------------
frame_cima = Frame(janela, width=250, height=50, bg='#161d40')
frame_cima.grid(row=0, column=0)

frame_baixo = Frame(janela, width=250, height=270, bg='black')
frame_baixo.grid(row=1, column=0)


# Funções --------------------------------
todos_valores = ''
def entrada_valores(event):
    global todos_valores
    todos_valores += str(event)
    valor_texto.set(todos_valores)

def calculo():
    global todos_valores
    resultado = eval(todos_valores)
    valor_texto.set(str(resultado))

def limpar_tela():
    global todos_valores
    todos_valores = ''
    valor_texto.set('')
# Labels ---------------------------------
valor_texto = StringVar()
label = Label(frame_cima, textvariable=valor_texto, width=16, height=2, padx=7, bg='#161d40', fg='white', relief=FLAT, anchor='e', justify=RIGHT, font='Ivy 16 bold')
label.place(x=0, y=0)
# botões ---------------------------------
b_1 = Button(frame_baixo,command=limpar_tela, text="C", width=11, height=2, bg='#cbcdd6', font='Ivy 13 bold', relief=RAISED, overrelief=RIDGE)
b_1.place(x=0, y=0)
b_2 = Button(frame_baixo, command=lambda: entrada_valores('%'), text="%", width=5, height=2, bg='#cbcdd6', font='Ivy 13 bold', relief=RAISED, overrelief=RIDGE)
b_2.place(x=120, y=0)
b_3 = Button(frame_baixo, command=lambda: entrada_valores('/'), text="/", width=5, height=2, bg='orange', fg='white', font='Ivy 13 bold', relief=RAISED, overrelief=RIDGE)
b_3.place(x=180, y=0)

b_4 = Button(frame_baixo, command=lambda: entrada_valores('7'), text="7", width=5, height=2, bg='#cbcdd6', font='Ivy 13 bold', relief=RAISED, overrelief=RIDGE)
b_4.place(x=0, y=52)
b_5 = Button(frame_baixo, command=lambda: entrada_valores('8'), text="8", width=5, height=2, bg='#cbcdd6', font='Ivy 13 bold', relief=RAISED, overrelief=RIDGE)
b_5.place(x=60, y=52)
b_6 = Button(frame_baixo, command=lambda: entrada_valores('9'), text="9", width=5, height=2, bg='#cbcdd6', font='Ivy 13 bold', relief=RAISED, overrelief=RIDGE)
b_6.place(x=120, y=52)
b_7 = Button(frame_baixo, command=lambda: entrada_valores('*'), text="*", width=5, height=2, bg='orange', fg='white', font='Ivy 13 bold', relief=RAISED, overrelief=RIDGE)
b_7.place(x=180, y=52)

b_8 = Button(frame_baixo, command=lambda: entrada_valores('4'), text="4", width=5, height=2, bg='#cbcdd6', font='Ivy 13 bold', relief=RAISED, overrelief=RIDGE)
b_8.place(x=0, y=104)
b_9 = Button(frame_baixo, command=lambda: entrada_valores('5'), text="5", width=5, height=2, bg='#cbcdd6', font='Ivy 13 bold', relief=RAISED, overrelief=RIDGE)
b_9.place(x=60, y=104)
b_10 = Button(frame_baixo, command=lambda: entrada_valores('6'), text="6", width=5, height=2, bg='#cbcdd6', font='Ivy 13 bold', relief=RAISED, overrelief=RIDGE)
b_10.place(x=120, y=104)
b_11 = Button(frame_baixo, command=lambda: entrada_valores('-'), text="-", width=5, height=2, bg='orange', fg='white', font='Ivy 13 bold', relief=RAISED, overrelief=RIDGE)
b_11.place(x=180, y=104)

b_12 = Button(frame_baixo, command=lambda: entrada_valores('1'), text="1", width=5, height=2, bg='#cbcdd6', font='Ivy 13 bold', relief=RAISED, overrelief=RIDGE)
b_12.place(x=0, y=156)
b_13 = Button(frame_baixo, command=lambda: entrada_valores('2'), text="2", width=5, height=2, bg='#cbcdd6', font='Ivy 13 bold', relief=RAISED, overrelief=RIDGE)
b_13.place(x=60, y=156)
b_14 = Button(frame_baixo, command=lambda: entrada_valores('3'), text="3", width=5, height=2, bg='#cbcdd6', font='Ivy 13 bold', relief=RAISED, overrelief=RIDGE)
b_14.place(x=120, y=156)
b_15 = Button(frame_baixo, command=lambda: entrada_valores('+'), text="+", width=5, height=2, bg='orange', fg='white', font='Ivy 13 bold', relief=RAISED, overrelief=RIDGE)
b_15.place(x=180, y=156)

b_1 = Button(frame_baixo, command=lambda: entrada_valores('0'), text="0", width=11, height=2, bg='#cbcdd6', font='Ivy 13 bold', relief=RAISED, overrelief=RIDGE)
b_1.place(x=0, y=208)
b_2 = Button(frame_baixo, text=".", width=5, height=2, bg='#cbcdd6', font='Ivy 13 bold', relief=RAISED, overrelief=RIDGE)
b_2.place(x=120, y=208)
b_3 = Button(frame_baixo, command=calculo, text="=", width=5, height=2, bg='orange', fg='white', font='Ivy 13 bold', relief=RAISED, overrelief=RIDGE)
b_3.place(x=180, y=208)

janela.mainloop()

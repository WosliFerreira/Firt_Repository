from tkinter import ttk, messagebox
from tkinter.ttk import *
from tkinter import *
from PIL import ImageTk, Image
import string
import random


janela = Tk()
janela.title('Gerador de Senhas ')
janela.geometry('300x398')
janela.iconphoto(False, PhotoImage(file='password.png'))
janela.config(bg='black')

stilo = ttk.Style(janela)
stilo.theme_use('clam')

# Dividinho a tela em 2 frames ----------------------------
frame_cima = Frame(janela, width=300, height=50, bg='white', pady=0, padx=0, relief='flat')
frame_cima.grid(row=0, column=0, sticky=NSEW)

frame_baixo = Frame(janela, width=300, height=310, bg='black', pady=0, padx=0, relief='flat')
frame_baixo.grid(row=1, column=0, sticky=NSEW)

# modelagem fram_cima ----------------------------
img = Image.open('password.png')
img = img.resize((40, 40), Image.Resampling.LANCZOS)
img = ImageTk.PhotoImage(img)

app_logo = Label(frame_cima, height=60, image=img, compound=LEFT, padx=10, relief='flat', anchor=NW, bg='white')
app_logo.place(x=2, y=0)

app_name = Label(frame_cima, text='GERADOR DE SENHAS', width=20, height=1, padx=0, relief='flat', anchor=NW,
                 font='Ivy 16 bold', bg='white', fg='black')
app_name.place(x=45, y=2)

app_linha = Label(frame_cima, text='', width=300, height=1, padx=0, relief='flat', anchor=NW, font='Ivy 1', bg='red',
                  fg='black')
app_linha.place(x=0, y=42)


# Função gerar senha ----------------------
def criar_senha():
    alfabeto_maior = string.ascii_uppercase
    alfabeto_menor = string.ascii_lowercase
    numeros = '1234567890'
    simbolos = '[]{}()!@#$%&*/,.-;'

    global combinar
    combinar = ''

    # condição maiuscula
    if estado_1.get() == alfabeto_maior:
        combinar = alfabeto_maior
    else:
        pass
    # condição minuscula
    if estado_2.get() == alfabeto_menor:
        combinar = combinar + alfabeto_menor
    else:
        pass
    # condição Numeros
    if estado_3.get() == numeros:
        combinar = combinar + numeros
    else:
        pass

    # condição Simbolos
    if estado_4.get() == simbolos:
        combinar = combinar + simbolos
    else:
        pass

    comprimento = int(combo.get())
    senha = ''.join(random.sample(combinar, comprimento))
    app_senha['text'] = senha

    def copiar():
        info = senha
        frame_baixo.clipboard_clear()
        frame_baixo.clipboard_append(info)

        messagebox.showinfo('Sucesso', 'Senha Copiada')

    botao_copiar = Button(frame_baixo, command=copiar, text='Copiar', width=6, height=2, overrelief='solid',
                          anchor=CENTER, bg='white', relief='raised', font='Ivy 11 bold', fg='black')
    botao_copiar.grid(row=0, column=1, sticky=NW, padx=0, pady=10, columnspan=1)


# Modelando frame baixo ----------------------

app_senha = Label(frame_baixo, text='********', width=22, height=2, padx=0, relief='solid', anchor=CENTER,
                  font='Ivy 12 bold', bg='white', fg='black')
app_senha.grid(row=0, column=0, columnspan=1, sticky=NSEW, padx=3, pady=10)

app_info = Label(frame_baixo, text='Numero Totais de Caracteres na Senha:', height=1, padx=0, relief='flat', anchor=NW,
                 font='Ivy 10 bold', bg='black', fg='white')
app_info.grid(row=1, column=0, columnspan=2, sticky=NSEW, padx=5, pady=1)

# var = IntVar()
# var.set(8)
# spin = Spinbox(frame_baixo, from_=0, to=16, width=5, textvariable=var)
# spin.grid(row=2, column=0, columnspan=2, sticky=NW, padx=5, pady=8)
combo = Combobox(frame_baixo, width=7)
combo['values'] = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16)
combo.current(8)
combo.grid(row=2, column=0, columnspan=2, padx=5, pady=8, sticky=NW)

# Frame Caracteres  ----------------------
frame_caracteres = Frame(frame_baixo, width=300, height=210, bg='black', pady=0, padx=0, relief='flat')
frame_caracteres.grid(row=3, column=0, sticky=NSEW, columnspan=3)

alfabeto_maior = string.ascii_uppercase
alfabeto_menor = string.ascii_lowercase
numeros = '1234567890'
simbolos = '[]{}()!@#$%&*/,.-;'

# Letras Maiusculas ----------------------
estado_1 = StringVar()
estado_1.set(False)
check_1 = Checkbutton(frame_caracteres, width=1, var=estado_1, onvalue=alfabeto_maior, offvalue='off', bg='white',
                      relief='flat')
check_1.grid(row=0, column=0, padx=5, pady=8, sticky=NW)
label_check_1 = Label(frame_caracteres, text='Letras Maiusculas', height=1, padx=0, relief='flat', anchor=NW,
                      font='Ivy 12 bold', bg='black', fg='white')
label_check_1.grid(row=0, column=1, sticky=NW, padx=2, pady=5)

# Letras Minusculas ----------------------
estado_2 = StringVar()
estado_2.set(False)
check_2 = Checkbutton(frame_caracteres, width=1, var=estado_2, onvalue=alfabeto_menor, offvalue='off', bg='white',
                      relief='flat')
check_2.grid(row=2, column=0, padx=5, pady=8, sticky=NW)
label_check_2 = Label(frame_caracteres, text='Letras Minusculas', height=1, padx=0, relief='flat', anchor=NW,
                      font='Ivy 12 bold', bg='black', fg='white')
label_check_2.grid(row=2, column=1, sticky=NW, padx=2, pady=5)

# Numeros -------------------------------------
estado_3 = StringVar()
estado_3.set(False)
check_3 = Checkbutton(frame_caracteres, width=1, var=estado_3, onvalue=numeros, offvalue='off', bg='white',
                      relief='flat')
check_3.grid(row=3, column=0, padx=5, pady=8, sticky=NW)
label_check_3 = Label(frame_caracteres, text='Numeros', height=1, padx=0, relief='flat', anchor=NW, font='Ivy 12 bold',
                      bg='black', fg='white')
label_check_3.grid(row=3, column=1, sticky=NW, padx=2, pady=5)

# Simbolos -------------------------------------
estado_4 = StringVar()
estado_4.set(False)
check_4 = Checkbutton(frame_caracteres, width=1, var=estado_4, onvalue=simbolos, offvalue='off', bg='white',
                      relief='flat')
check_4.grid(row=4, column=0, padx=5, pady=8, sticky=NW)
label_check_4 = Label(frame_caracteres, text='Simbolos', height=1, padx=0, relief='flat', anchor=NW, font='Ivy 12 bold',
                      bg='black', fg='white')
label_check_4.grid(row=4, column=1, sticky=NW, padx=2, pady=5)

# Botão -------------------------------------
botao = Button(frame_caracteres, command=criar_senha, text='Gerar Senha', width=28, height=1, overrelief='solid',
               anchor=CENTER, bg='red', relief='flat', font='Ivy 12 bold', fg='white')
botao.grid(row=5, column=0, sticky=NSEW, padx=5, pady=15, columnspan=5)

janela.mainloop()

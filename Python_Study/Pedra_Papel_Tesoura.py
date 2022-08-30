
from tkinter import *
from tkinter import ttk
import random

# Importando o pillow
from PIL import Image, ImageTk

# Cores
co0 = "#FFFFFF" # White
co1 = "#333333" # Branca
co2 = "#fcc058" # Orange
co3 = "#38576b" # Valor
co4 = "#3292a8" # Blue
co5 = "#fff873" # Yellow
co6 = "#fcc058" # Orange
co7 = "#e85151" # Red
co8 = "#34eb3d" # Green
fundo = "#3b3b3b"

# Configurando Janela
janela = Tk()
janela.title('')
janela.geometry('260x280')
janela.configure(bg=fundo)

# Dividindo a janela
frame_cima = Frame(janela, width=260, height=100, bg=co1, relief='raised')
frame_cima.grid(row=0, column=0, sticky=NW)
frame_baixo = Frame(janela, width=260, height=180, bg=co0, relief='flat')
frame_baixo.grid(row=1, column=0, sticky=NW)

stilo = ttk.Style(janela)
stilo.theme_use('clam')

# Configurando frame cima

play_1 = Label(frame_cima, text='Você', height=1, anchor='center', font=('Ivy 10 bold'), bg=co1, fg=co0)
play_1.place(x=25, y=70)
play_1_linha = Label(frame_cima, text='', height=10, anchor='center', font=('Ivy 10 bold'), bg=co0, fg=co0)
play_1_linha.place(x=0, y=0)
play_1_pontos = Label(frame_cima, text='0', height=1, anchor='center', font=('Ivy 30 bold'), bg=co1, fg=co0)
play_1_pontos.place(x=50, y=20)

app = Label(frame_cima, text=':', height=1, anchor='center', font=('Ivy 30 bold'), bg=co1, fg=co0)
app.place(x=125, y=20)

play_2 = Label(frame_cima, text='PC', height=1, anchor='center', font=('Ivy 10 bold'), bg=co1, fg=co0)
play_2.place(x=205, y=70)
play_2_linha = Label(frame_cima, text='', height=10, anchor='center', font=('Ivy 10 bold'), bg=co0, fg=co0)
play_2_linha.place(x=255, y=0)
play_2_pontos = Label(frame_cima, text='0', height=1, anchor='center', font=('Ivy 30 bold'), bg=co1, fg=co0)
play_2_pontos.place(x=170, y=20)

app_linha = Label(frame_cima, text='', width=255, anchor='center', font=('Ivy 1 bold'), bg=co1, fg=co0)
app_linha.place(x=0, y=95)

global voce
global pc
global rodadas
global pontos_voce
global pontos_pc

pontos_voce = 0
pontos_pc = 0
rodadas = 5

# Logica do jogo
def jogar(i):
    global rodadas
    global pontos_voce
    global pontos_pc

    if rodadas >0:
        print(rodadas)
        opcoes = ['Pedra', 'Papel', 'Tesoura']
        pc = random.choice(opcoes)
        voce = i

        print(voce, pc)

    else:
        fim_do_jogo()

# Iniciar o jogo
# Configurando frame baixo
def iniciar_jogo():
    global icon1
    global icon2
    global icon3
    global b_icon_1
    global b_icon_2
    global b_incon_3
    icon1 = Image.open('Imagens/pedra.jpg')
    icon1 = icon1.resize((50,50), Image.Resampling.LANCZOS)
    icon1 = ImageTk.PhotoImage(icon1)
    b_icon_1 = Button(frame_baixo,command=lambda:jogar('Pedra'), width=50, image=icon1, compound=CENTER, bg=co0, fg=co0, font=('Ivy 10 bold'), anchor=CENTER, relief='flat')
    b_icon_1.place(x=15, y=60)

    icon2 = Image.open('Imagens/papel.jpg')
    icon2 = icon2.resize((50,50), Image.Resampling.LANCZOS)
    icon2 = ImageTk.PhotoImage(icon2)
    b_icon_2 = Button(frame_baixo,command=lambda:jogar('Papel'), width=50, image=icon2, compound=CENTER, bg=co0, fg=co0, font=('Ivy 10 bold'), anchor=CENTER, relief='flat')
    b_icon_2.place(x=95, y=60)

    icon3 = Image.open('Imagens/tesoura.jpg')
    icon3 = icon3.resize((50,50), Image.Resampling.LANCZOS)
    icon3 = ImageTk.PhotoImage(icon3)
    b_icon_3 = Button(frame_baixo,command=lambda:jogar('Tesoura'), width=50, image=icon3, compound=CENTER, bg=co0, fg=co0, font=('Ivy 10 bold'), anchor=CENTER, relief='flat')
    b_icon_3.place(x=170, y=60)


# Terminar o jogo
def fim_do_jogo():
    pass


b_jogar = Button(frame_baixo,command=iniciar_jogo, width=30, text='Play', bg=fundo, fg=co0, font=('Ivy 10 bold'), anchor=CENTER, relief=RAISED, overrelief=RIDGE)
b_jogar.place(x=5, y=151)



janela.mainloop()
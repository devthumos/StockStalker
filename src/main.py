from tkinter import *
from tkinter.font import Font
from tkinter import ttk


def logar():
    try:
        if user_entry.get() == "admin" and pass_entry.get() == "admin":
            print("ACESSO PERMITIDO")
        else:
            print("ACESSO NEGADO")
    except ValueError:
        print("Deu ruim aqui meu truta")


wndlogin = Tk()
wndlogin.title("ActionStalker")
wndlogin.geometry("500x250+100+100")

mainframe = ttk.Frame(wndlogin)
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
wndlogin.columnconfigure(0, weight=1)
wndlogin.rowconfigure(0, weight=1)

# Frame que conterá a label "LOGIN", label "LOGIN"
lbl_lgin_frm = Frame(mainframe, bg="#58636E")
lbl_log = Label(lbl_lgin_frm, text="LOGIN", background="#58636E", fg="white",
                font=Font(family="Comic Sans Ms", size=15, weight="bold"))
lbl_log.pack()
lbl_lgin_frm.pack(fill=X, side=TOP)

# Frame que conterá as Labels "Usuário", "Senha", o Botão "Logar" e os
# Widgets de entrada de dados
lgn_frm = Frame(mainframe, pady=10)
    # Label "Usuário"
ttk.Label(lgn_frm, text="Usuário",
          font=Font(family="Comic Sans Ms", size=10, weight="normal")).grid(column=0, row=0, sticky=(E))
user_entry = Entry(lgn_frm, width=20)
user_entry.grid(column=1, row=0, sticky=(W))
user_entry.grid_configure(padx=5, pady=5)
    # Label "Senha"
ttk.Label(lgn_frm, text="Senha",
          font=Font(family="Comic Sans Ms", size=10, weight="normal")).grid(column=0, row=1, sticky=(E))
pass_entry = Entry(lgn_frm, width=20)
pass_entry.grid(column=1, row=1, sticky=(W))
pass_entry.grid_configure(padx=5, pady=5)
# Botão "Logar"
btn_log = Button(lgn_frm, text="Logar", bg="#58636E", fg="white", relief="flat", command=logar)
btn_log.grid(column=1, row=3, sticky=(N, W, S, E), columnspan=1)
btn_log.grid_configure(padx=5, pady=5)
lgn_frm.pack()

wndlogin.mainloop()

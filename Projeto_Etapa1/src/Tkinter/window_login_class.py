from tkinter import *
from tkinter.font import *
from tkinter import ttk
from window_carteira_class import WindowCarteira
from src.MySQL.login import LoginMySQL


class LoginWindow:

    def __init__(cls):
        cls.object_login = LoginMySQL()

        cls.wndlogin = Tk()
        cls.wndlogin.title("ActionStalker")
        cls.wndlogin.geometry("500x250+100+100")

        mainframe = ttk.Frame(cls.wndlogin)
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        cls.wndlogin.columnconfigure(0, weight=1)
        cls.wndlogin.rowconfigure(0, weight=1)

        # Frame que conterá a label "LOGIN", label "LOGIN"
        lbl_lgin_frm = Frame(mainframe, bg="Black")
        lbl_log = Label(lbl_lgin_frm, text="LOGIN", background="Black", fg="white",
                            font=Font(family="Arial Black", size=15, weight="bold"))
        lbl_log.pack()
        lbl_lgin_frm.pack(fill=X, side=TOP)

        # Frame que conterá as Labels Estáticas e os Widgets de Entrada
        lgn_frm = Frame(mainframe, pady=10)
        # Parte Usuário
        cls.uservar = StringVar()
        ttk.Label(lgn_frm, text="Usuário",font=Font(family="Arial Black", size=10, weight="normal",
                                                    underline=True)).grid(column=0, row=0, sticky=(E))
        user_entry = Entry(lgn_frm, width=20, textvariable=cls.uservar)
        user_entry.grid(column=1, row=0, sticky=(W))
        user_entry.grid_configure(padx=5, pady=5)
        # Parte Senha
        cls.passvar = StringVar()
        ttk.Label(lgn_frm, text="Senha",
                  font=Font(family="Arial Black", size=10, weight="normal",
                            underline=True)).grid(column=0, row=1, sticky=(E))
        pass_entry = Entry(lgn_frm, width=20, show="*", textvariable=cls.passvar)
        pass_entry.grid(column=1, row=1, sticky=(W))
        pass_entry.grid_configure(padx=5, pady=5)

        # Botão "Logar"
        btn_log = Button(lgn_frm, text="Logar", bg="Black", fg="white", relief="flat", command=cls.for_carteira_window,
                         font=Font(family="Arial Black", size=9, weight="normal"))
        btn_log.grid(column=1, row=3, sticky=(N, W, S, E), columnspan=1)
        btn_log.grid_configure(padx=5, pady=5)
        # Botão "Não Tenho Cadastro"
        btn_regst = Button(lgn_frm, text="Registrar", bg="Black", fg="white", relief="flat", command=cls.registrar,
                           font=Font(family="Arial Black", size=9, weight="normal"))
        btn_regst.grid(column=1, row=4, sticky=(N, W, S, E), columnspan=1)
        lgn_frm.pack()
        lgn_frm.pack_configure(padx="0 52")
        btn_regst.grid_configure(padx=5, pady=5)
        # Label Não Estática "ACESSO PERMITIDO", "ACESSO NEGADO", "ACESSO REGISTRADO"
        cls.lbl = Label(mainframe, text="")
        cls.lbl.pack()

        # Botão Quit

        cls.wndlogin.bind("<Return>", cls.for_carteira_window)
        cls.wndlogin.mainloop()

    def logar(cls, *args):
        credenciais = cls.object_login.verificacao_login(cls.uservar.get(), cls.passvar.get())
        user = cls.uservar
        if credenciais:
            cls.lbl["text"] = "ACESSO PERMITIDO"
            return True
        else:
            cls.lbl["text"] = "ACESSO NEGADO"
            cls.passvar.set("")
            cls.uservar.set("")
            return False

    def registrar(cls, *args):
        registro = cls.object_login.registrar_login(cls.uservar.get(), cls.passvar.get())

        if registro == None:
            cls.lbl["text"] = f"Usuário \"{cls.uservar.get()}\" Já Existente, Insira Outro Usuário"
        elif registro == True:
            cls.lbl["text"] = f"Usuário \"{cls.uservar.get()}\" Cadastrado Com Sucesso"
        else:
            cls.lbl["text"] = f"ERRO, Não Foi Possível Registrar o Usuário \"{cls.uservar.get()}\""

        cls.passvar.set("")
        cls.uservar.set("")

    def for_carteira_window(cls, *args):
        if cls.logar():
            cls.wndlogin.destroy()
            cls.wndcart = WindowCarteira("user_" + cls.object_login.get_id(cls.uservar.get()))
            cls.wndcart.main()

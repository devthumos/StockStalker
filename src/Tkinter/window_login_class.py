from tkinter import *
from tkinter.font import *
from tkinter import ttk


class Login():


    def __init__(cls):
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

        # Frame que conterá as Labels Estáticas e os Widgets de Entrada
        lgn_frm = Frame(mainframe, pady=10)
        # Parte Usuário
        cls.uservar = StringVar()
        ttk.Label(lgn_frm, text="Usuário",
                  font=Font(family="Comic Sans Ms", size=10, weight="normal")).grid(column=0, row=0, sticky=(E))
        user_entry = Entry(lgn_frm, width=20, textvariable=cls.uservar)
        user_entry.grid(column=1, row=0, sticky=(W))
        user_entry.grid_configure(padx=5, pady=5)
        # Parte Senha
        cls.passvar = StringVar()
        ttk.Label(lgn_frm, text="Senha",
                  font=Font(family="Comic Sans Ms", size=10, weight="normal")).grid(column=0, row=1, sticky=(E))
        pass_entry = Entry(lgn_frm, width=20, textvariable=cls.passvar)
        pass_entry.grid(column=1, row=1, sticky=(W))
        pass_entry.grid_configure(padx=5, pady=5)
        # Botão "Logar"
        btn_log = Button(lgn_frm, text="Logar", bg="#58636E", fg="white", relief="flat", command=cls.logar)
        btn_log.grid(column=1, row=3, sticky=(N, W, S, E), columnspan=1)
        btn_log.grid_configure(padx=5, pady=5)
        # Botão "Não Tenho Cadastro"
        btn_regst = Button(lgn_frm, text="Registrar", bg="#58636E", fg="white", relief="flat", command=cls.registrar)
        btn_regst.grid(column=1, row=4, sticky=(N, W, S, E), columnspan=1)
        btn_regst.grid_configure(padx=5, pady=5)
        # Label Não Estática "ACESSO PERMITIDO", "ACESSO NEGADO", "ACESSO REGISTRADO"
        cls.lbl = Label(lgn_frm, text="")
        cls.lbl.grid(column=1, row=5, sticky=(N, W, S, E), columnspan=1)
        cls.lbl.grid_configure(padx=5, pady=5)
        lgn_frm.pack()

        # Botão Quit

        wndlogin.bind("<Return>", cls.logar)
        wndlogin.mainloop()


    def logar(cls, *args):
        try:
            if cls.uservar.get() == "admin" and cls.passvar.get() == "admin":
                cls.uservar.set("")
                cls.passvar.set("")

                cls.lbl["text"] = "ACESSO PERMITIDO"
            else:
                cls.uservar.set("")
                cls.passvar.set("")

                cls.lbl["text"] = "ACESSO NEGADO"
        except ValueError:
            cls.uservar.set("DADOS INVÁLIDOS")
            cls.passvar.set("DADOS INVÁLIDOS")

            cls.lbl["text"] = "DADOS INVÁLIDOS"


    def registrar(cls, *args):
        pass


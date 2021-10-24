from ttkbootstrap import Style
from tkinter import *
from tkinter.font import *
from tkinter import ttk
from window_carteira_class_atualizado import WindowCarteira
from src.MySQL.login import LoginMySQL


class LoginWindow:

    def __init__(self):
        self.object_login = LoginMySQL()

        style = Style("flatly")
        style.configure('primary.TButton', font=('Arial Black', 12))

        self.wndlogin = style.master
        self.wndlogin.title("ActionStalker")
        self.wndlogin.geometry("500x300+200+50")

        self.mainframe = ttk.Frame(self.wndlogin)
        self.mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        self.wndlogin.columnconfigure(0, weight=1)
        self.wndlogin.rowconfigure(0, weight=1)


    def lbl_lgin_frm_func(self):
        # Frame "lbl_lgin_frm" que conterá label e button, label "LOGIN", button "Config"
        # Frame lbl_lgin_frm
        lbl_lgin_frm = Frame(self.mainframe, bg="#3D3D3D")
        lbl_lgin_frm.pack(fill=X)
        lbl_lgin_frm.columnconfigure(0, weight=1)
        lbl_lgin_frm.rowconfigure(0, weight=1)
        # Label "CARTEIRA STALKER"
        lbl_log = Label(lbl_lgin_frm, text="LOGIN", background="#3D3D3D", fg="white",
                        font=Font(size=20, weight="bold"))
        lbl_log.pack()
        lbl_log.pack_configure()


    def lgn_frm_func(self):
                # Frame que conterá as Labels Estáticas e os Widgets de Entrada
        lgn_frm = Frame(self.mainframe, pady=10)

        # Parte Usuário
        self.uservar = StringVar()
        ttk.Label(lgn_frm, text="Usuário", foreground="#3D3D3D",
                  font=Font(family="Arial #3D3D3D", size=12, weight="bold", underline=True)).grid(column=0, row=0, sticky=(E), pady=10)
        user_entry = ttk.Entry(lgn_frm, width=20, textvariable=self.uservar, style="primary.TEntry")
        user_entry.grid(column=1, row=0, sticky=(W))
        user_entry.grid_configure(padx=5, pady=10)

        # Parte Senha
        self.passvar = StringVar()
        ttk.Label(lgn_frm, text="Senha", foreground="#3D3D3D",
                  font=Font(family="Arial #3D3D3D", size=12, weight="bold", underline=True)).grid(column=0, row=1, sticky=(E), pady=10)
        pass_entry = ttk.Entry(lgn_frm, width=20, show="*", textvariable=self.passvar, style="primary.TEntry")
        pass_entry.grid(column=1, row=1, sticky=(W))
        pass_entry.grid_configure(padx=5, pady=10)

        # Botão "Logar"
        btn_log = ttk.Button(lgn_frm, text="Logar", command=self.for_carteira_window, style="primary.TButton")
        btn_log.grid(column=1, row=3, sticky=(N, W, S, E), columnspan=1)
        btn_log.grid_configure(padx=5, pady=5)

        # Botão "Não Tenho Cadastro"
        btn_regst = ttk.Button(lgn_frm, text="Registrar", command=self.registrar, style="primary.TButton")
        btn_regst.grid(column=1, row=4, sticky=(N, W, S, E), columnspan=1)
        lgn_frm.pack()
        lgn_frm.pack_configure(padx="0 52")
        btn_regst.grid_configure(padx=5, pady=5)


    def startloop(self):
        # Label Não Estática "ACESSO PERMITIDO", "ACESSO NEGADO", "ACESSO REGISTRADO"
        self.lbl = Label(self.mainframe, text="")
        self.lbl.pack()

        # Botão Quit

        self.wndlogin.bind("<Return>", self.for_carteira_window)
        self.wndlogin.mainloop()

    def logar(self, *args):
        credenciais = self.object_login.verificacao_login(self.uservar.get(), self.passvar.get())
        user = self.uservar
        if credenciais:
            self.lbl["text"] = "ACESSO PERMITIDO"
            return True
        else:
            self.lbl["text"] = "ACESSO NEGADO"
            self.passvar.set("")
            self.uservar.set("")
            return False

    def registrar(self, *args):
        registro = self.object_login.registrar_login(self.uservar.get(), self.passvar.get())

        if registro == None:
            self.lbl["text"] = f"Usuário {self.uservar.get()} Já Existente, Insira Outro Usuário"
        elif registro == True:
            self.lbl["text"] = f"Usuário {self.uservar.get()} Cadastrado Com Sucesso"
        else:
            self.lbl["text"] = f"ERRO, Não Foi Possível Registrar o Usuário \"{self.uservar.get()}\""

        self.passvar.set("")
        self.uservar.set("")

    def for_carteira_window(self, *args):
        if self.logar():
            self.wndlogin.destroy()
            self.wndcart = WindowCarteira("user_" + self.object_login.get_id(self.uservar.get()))
            self.wndcart.main()

    def main(self):
        self.lbl_lgin_frm_func()
        self.lgn_frm_func()
        self.startloop()


if __name__ == "__main__":
    item = LoginWindow()
    item.main()

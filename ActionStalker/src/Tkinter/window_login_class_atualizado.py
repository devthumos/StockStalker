from ttkbootstrap import Style
from tkinter import *
from tkinter.font import *
from tkinter import ttk
from verificacoes import Verificacoes
from window_carteira_class_atualizado import WindowCarteira
from src.MySQL.login import LoginMySQL


class LoginWindow:
    """
    Classe responsável integração do banco de dados com a janela wndlogin, a janela de login do usuário
    """
    def __init__(self):
        self.object_verificacoes = Verificacoes()
        self.object_login = LoginMySQL()

        style = Style("flatly")
        style.configure('primary.TButton', font=('Arial Black', 12))

        self.wndlogin = style.master
        self.wndlogin.title("ActionStalker")
        self.wndlogin.geometry("500x315+200+50")

        self.mainframe = ttk.Frame(self.wndlogin)
        self.mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        self.wndlogin.columnconfigure(0, weight=1)
        self.wndlogin.rowconfigure(0, weight=1)

    def lbl_lgin_frm_func(self):
        """
        Método responsável por inserir o cabeçalho da janela de carteira
        """
        # Frame "lbl_lgin_frm" que conterá label estática "LOGIN"
        lbl_lgin_frm = Frame(self.mainframe, bg="#3D3D3D")
        lbl_lgin_frm.pack(fill=X)
        lbl_lgin_frm.columnconfigure(0, weight=1)
        lbl_lgin_frm.rowconfigure(0, weight=1)
        # Label estática "LOGIN"
        lbl_log = Label(lbl_lgin_frm, text="LOGIN", background="#3D3D3D", fg="white",
                        font=Font(size=20, weight="bold"))
        lbl_log.pack()
        lbl_log.pack_configure()

    def lgn_frm_func(self):
        """
        Método  responsável por inserir as entries, labels e botões principais
        """
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

        # Botão "Registrar"
        btn_regst = ttk.Button(lgn_frm, text="Registrar", command=self.registrar, style="primary.TButton")
        btn_regst.grid(column=1, row=4, sticky=(N, W, S, E), columnspan=1)
        lgn_frm.pack()
        lgn_frm.pack_configure(padx="0 52")
        btn_regst.grid_configure(padx=5, pady=5)

    def startloop(self):
        """
        Método responsável por inserir a label dinâmica que informa o usuário sobre a tentativa de login e iniciar o
        looping da janela
        """
        # Label dinâmica "ACESSO PERMITIDO", "ACESSO NEGADO"
        self.lbl = Label(self.mainframe, text="")
        self.lbl.pack()

        self.wndlogin.bind("<Return>", self.for_carteira_window)
        self.wndlogin.mainloop()

    def logar(self, *args):
        """
        Método responsável por logar o usuário e o informar sobre a tentativa de login
        Retorna True, caso o acesso for permitido
        Retorna False, caso o acesso seja negado
        """
        if self.object_verificacoes.verificacao_senha(self.uservar.get()) and self.object_verificacoes.verificacao_senha(self.passvar.get()):
            credenciais = self.object_login.verificacao_login(self.uservar.get(), self.passvar.get())
            if credenciais:
                self.lbl["text"] = "ACESSO PERMITIDO"
                return True
            else:
                self.lbl["text"] = "ACESSO NEGADO"
                self.passvar.set("")
                self.uservar.set("")
                return False
        else:
            self.lbl["text"] = "ACESSO NEGADO"
            self.passvar.set("")
            self.uservar.set("")
            return False

    def registrar(self, *args):
        """
        Método responsável por registrar o usuário e o informar sobre a tentativa de cadastro
        """
        if self.object_verificacoes.verificacao_senha(
                self.uservar.get()) and self.object_verificacoes.verificacao_senha(self.passvar.get()):
            registro = self.object_login.registrar_login(self.uservar.get(), self.passvar.get())

            if registro == None:
                self.lbl["text"] = f"Usuário {self.uservar.get()} Já Existente, Insira Outro Usuário"
            elif registro == True:
                self.lbl["text"] = f"Usuário {self.uservar.get()} Cadastrado Com Sucesso"
            else:
                self.lbl["text"] = f"ERRO, Não Foi Possível Registrar o Usuário \"{self.uservar.get()}\""

            self.passvar.set("")
            self.uservar.set("")
        else:
            self.lbl["text"] = "Usuário e senha devem ser maiores que 4 caracteres\nApenas a senha pode possuir caracteres especiais\nNenhum deles podem ter espaço"
            self.passvar.set("")
            self.uservar.set("")

    def for_carteira_window(self, *args):
        """
        Método responsável por direcionar o usuário, caso o acesso seja permitido, à sua respectiva carteira
        """
        if self.logar():
            self.wndlogin.destroy()
            self.wndcart = WindowCarteira("user_" + self.object_login.get_id(self.uservar.get()))
            self.wndcart.main()

    def main(self):
        """
        Método responsável por juntar todos os métodos da classe
        """
        self.lbl_lgin_frm_func()
        self.lgn_frm_func()
        self.startloop()


if __name__ == "__main__":
    item = LoginWindow()
    item.main()

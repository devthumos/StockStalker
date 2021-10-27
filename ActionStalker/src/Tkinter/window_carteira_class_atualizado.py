import time
from ttkbootstrap import Style
from tkinter import *
from tkinter.font import *
from tkinter import ttk
from verificacoes import Verificacoes
from src.MySQL.registro import RegistroMySQL
from src.Web_Scraping.statusinvest import Webscrapper


class WindowCarteira:
    """
    Classe responsável pela integração do banco de dados com a janela wndcarteira, a janela de carteira do usuário
    """
    def __init__(self, id_user):
        """
        Método responsável por instanciar/iniciar a janela de carteira e outros objetos relevantes ao código
        """
        self.object_verificacoes = Verificacoes()
        self.object_registro = RegistroMySQL()
        self.id_user = id_user

        style = Style("flatly")
        style.configure('primary.TButton', font=('Arial Black', 12))

        self.wndcarteira = style.master
        self.wndcarteira.title("ActionStalker")
        self.wndcarteira.geometry("925x925+200+50")

        # Frame principal "self.mainframe"
        self.mainframe = ttk.Frame(self.wndcarteira)
        self.mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        self.wndcarteira.columnconfigure(0, weight=1)
        self.wndcarteira.rowconfigure(0, weight=1)

    def lbl_lgin_frm(self):
        """
        Método responsável por inserir o cabeçalho da janela de carteira
        """
        # Frame "lbl_lgin_frm" que conterá label estática "CARTEIRA"
        lbl_lgin_frm = Frame(self.mainframe, bg="#3D3D3D")
        lbl_lgin_frm.pack(fill=X)
        lbl_lgin_frm.columnconfigure(0, weight=1)
        lbl_lgin_frm.rowconfigure(0, weight=1)
        # Label estática "CARTEIRA STALKER"
        lbl_log = Label(lbl_lgin_frm, text="CARTEIRA STALKER", background="#3D3D3D", fg="white",
                        font=Font(size=20, weight="bold"))
        lbl_log.pack()
        lbl_log.pack_configure()

    def rgst_cod_frm(self):
        """
        Método responsável por inserir os entries, labels e botões principais
        """
        # Frame "self.rgst_cod_frm" que conterá labels, button, Entry Widgets
        self.rgst_cod_frm = ttk.Frame(self.mainframe, style="TFrame")
        self.rgst_cod_frm.pack(fill=X)
        self.rgst_cod_frm.columnconfigure(0, weight=1)
        self.rgst_cod_frm.rowconfigure(0, weight=1)
        # Frame "self.space_frm" responsável pelo espaçamento dentro do Frame "self.rgst_cod_frm"
        self.space_frm = ttk.Frame(self.rgst_cod_frm, style="TFrame")
        self.space_frm.pack()
        self.space_frm.pack_configure(padx="0 7")
        # Label text="Código" e Entry "cod_entry"
        self.codvar = StringVar()
        ttk.Label(self.space_frm, text="Código", foreground="#3D3D3D",
                  font=Font(family="Arial #3D3D3D", size=12, weight="bold", underline=True)).grid(row=0, column=0, sticky=(E), padx="0 8", pady="10 10")
        cod_entry = ttk.Entry(self.space_frm, width=51, textvariable=self.codvar, style="primary.TEntry")
        cod_entry.grid(row=0, column=1, sticky=(E), pady="10 10")
        # Button "rgst_btn"
        rgst_btn = ttk.Button(self.space_frm, text="Registrar", command=self.registrar, style="primary.TButton") # TESTE
        rgst_btn.grid(row=1, column=1, sticky=(N, S, W, E))
        # Refresh Button
        refresh_btn = ttk.Button(self.space_frm, text="Atualizar", command=self.refresh, style="primary.TButton")
        refresh_btn.grid(row=1, column=2, sticky=(E), padx="10 0")
        # Delete Button
        del_btn = ttk.Button(self.space_frm, text="Remover", command=self.delete, style="primary.TButton")
        del_btn.grid(row=1, column=0, sticky=(E), padx="0 10")

    def treeview_frms(self):
        """
        Método responsável por inserir na janela as treeviews
        """
                # Frame treeviews "self.treeviews_frm_conjunt" que conterá os treeviews
        self.treeviews_frm_conjunt = Frame(self.mainframe, padx="10", pady="10")
        self.treeviews_frm_conjunt.pack(fill=BOTH)
        self.treeviews_frm_conjunt.columnconfigure(0, weight=1)
        self.treeviews_frm_conjunt.rowconfigure(0, weight=1)

                # Frames para cada treeview e seu respectivo scrollbar
            # treemajor_frm
        treemajor_frm = LabelFrame(self.treeviews_frm_conjunt, text="Ação/FII/BDRS", foreground="#3D3D3D", font=Font(family="Arial Black", size="10"))

        self.treemajor = ttk.Treeview(treemajor_frm, column=("col1", "col2", "col3", "col4", "col5", "col6"), style="secondary.Treeview")
        self.treemajor.heading("#0", text="")
        self.treemajor.heading("#1", text="Empresa")
        self.treemajor.heading("#2", text="Valor Atual")
        self.treemajor.heading("#3", text="Min. 52 Semanas")
        self.treemajor.heading("#4", text="Máx. 52 Semanas")
        self.treemajor.heading("#5", text="Dividend Yield")
        self.treemajor.heading("#6", text="Valorização (12M)")

        treemajor_scrollv = Scrollbar(treemajor_frm, orient=VERTICAL, command=self.treemajor.yview)
        treemajor_scrollh = Scrollbar(treemajor_frm, orient=HORIZONTAL, command=self.treemajor.xview)
        treemajor_scrollv.pack(side=RIGHT, fill=Y)
        treemajor_scrollh.pack(side=BOTTOM, fill=X)

        self.treemajor.configure(yscrollcommand=treemajor_scrollv.set)
        self.treemajor.configure(xscrollcommand=treemajor_scrollh.set)
        self.treemajor.pack(fill=X)

        treemajor_frm.pack(fill=X)

            # treefundos_frm
        treefundos_frm = LabelFrame(self.treeviews_frm_conjunt, text="Fundos de Investimento", foreground="#3D3D3D", font=Font(family="Arial Black", size="10"))

        self.treefundos = ttk.Treeview(treefundos_frm, column=("col1", "col2", "col3", "col4", "col5", "col6", "col7"), style="secondary.Treeview")
        self.treefundos.heading("#0", text="")
        self.treefundos.heading("#1", text="Empresa")
        self.treefundos.heading("#2", text="Preço da Cota")
        self.treefundos.heading("#3", text="Rentabilidade (12M)")
        self.treefundos.heading("#4", text="Rentabilidade (24M)")
        self.treefundos.heading("#5", text="Volatilidade (6M)")
        self.treefundos.heading("#6", text="Índice de Sharpe (6M)")
        self.treefundos.heading("#7", text="Patrimônio Líquido")

        treefundos_scrollv = Scrollbar(treefundos_frm, orient=VERTICAL, command=self.treefundos.yview)
        treefundos_scrollh = Scrollbar(treefundos_frm, orient=HORIZONTAL, command=self.treefundos.xview)
        treefundos_scrollv.pack(side=RIGHT, fill=Y)
        treefundos_scrollh.pack(side=BOTTOM, fill=X)

        self.treefundos.configure(yscrollcommand=treefundos_scrollv.set)
        self.treefundos.configure(xscrollcommand=treefundos_scrollh.set)
        self.treefundos.pack(fill=X)

        treefundos_frm.pack(fill=X)

            # treetesouro_frm
        treetesouro_frm = LabelFrame(self.treeviews_frm_conjunt, text="Tesouro", foreground="#3D3D3D", font=Font(family="Arial Black", size="10"))

        self.treetesouro = ttk.Treeview(treetesouro_frm, column=("col1", "col2", "col3", "col4", "col5"), style="secondary.Treeview")
        self.treetesouro.heading("#0", text="")
        self.treetesouro.heading("#1", text="Valor Unitário")
        self.treetesouro.heading("#2", text="Taxa de Rentabilidade")
        self.treetesouro.heading("#3", text="Min. 52 Semanas")
        self.treetesouro.heading("#4", text="Máx. 52 Semanas")
        self.treetesouro.heading("#5", text="Valorização (12M)")

        treetesouro_scrollv = Scrollbar(treetesouro_frm, orient=VERTICAL, command=self.treetesouro.yview)
        treetesouro_scrollh = Scrollbar(treetesouro_frm, orient=HORIZONTAL, command=self.treetesouro.xview)
        treetesouro_scrollv.pack(side=RIGHT, fill=Y)
        treetesouro_scrollh.pack(side=BOTTOM, fill=X)

        self.treetesouro.configure(yscrollcommand=treetesouro_scrollv.set)
        self.treetesouro.configure(xscrollcommand=treetesouro_scrollh.set)
        self.treetesouro.pack(fill=X)

        treetesouro_frm.pack(fill=X)

        self.refreshT2T()  # Inserindo as informações atualizadas nas treeviews logo que a carteira é carregada e também a cada 1 minuto

    def polishing_endloop(self):
        self.wndcarteira.bind("<Return>", self.registrar)

        # Startando o Loopping
        self.wndcarteira.mainloop()

    def into_wbscrapper(self) -> tuple:
        """
        Método responsável para fazer o webscraping do código inserido e retornar os seus indicadores
        """
        wb = Webscrapper()
        indicadores = wb.main(self.codvar.get())

        return indicadores

    def registrar(self, *args):
        """
        Método responsável por registrar o código no banco de dados e inserir suas informações na treeview
        """
        if self.object_verificacoes.verificacao_codigo(self.codvar.get()):
            stt = self.into_wbscrapper()
            if self.object_registro.registrar_registros(self.codvar.get().lower(), stt, self.id_user) != False:
                if stt[1] == "Ação" or stt[1] == "Fundo Imobiliario" or stt[1] == "BDRS":
                    self.treemajor.insert('', 0, text=self.codvar.get().lower(), values=(stt[0][0], "R$ "+stt[0][1], "R$ "+stt[0][2],
                                                                                     "R$ "+stt[0][3], stt[0][4]+"%", stt[0][5]))
                elif stt[1] == "Fundo de Investimento":
                    self.treefundos.insert('', 0, text=self.codvar.get().lower(), values=(stt[0][0], "R$ "+stt[0][6], stt[0][1]+"%",
                                                                                stt[0][2]+"%", stt[0][3]+"%", stt[0][4], "R$ "+stt[0][5]))
                elif stt[1] == "Tesouro":
                    self.treetesouro.insert('', 0, text=self.codvar.get().lower(), values=("R$ "+stt[0][1], stt[0][6]+"% a.a", "R$ "+stt[0][2],
                                                                       "R$ "+stt[0][3], stt[0][4],))
        else:
            pass
        self.codvar.set("")

    def filltree(self):
        """
        Método que preenche as treeviews com os códigos da tabela code_user
        """
        registros = self.object_registro.list_elements(self.id_user)
        for i in registros:
             if i[1] == "Ação" or i[1] == "Fundo Imobiliario" or i[1] == "BDRS":
                 self.treemajor.insert('', 0, text=i[0], values=(i[2], "R$ "+i[3], "R$ "+i[4],
                                                                                  "R$ "+i[5], i[6]+"%", i[7]))
             elif i[1] == "Fundo de Investimento":
                 self.treefundos.insert('', 0, text=i[0], values=(i[2], "R$ "+i[8],i[3]+"%", i[4]+"%",
                                                                             i[5]+"%", i[6], "R$ "+i[7]))
             elif i[1] == "Tesouro":
                 self.treetesouro.insert('', 0, text=i[0], values=("R$ "+i[3], i[8]+"% a.a.", "R$ "+i[4], "R$ "+i[5],
                                                                        i[6]))

    def refresh(self):
        """
        Método responsável por deletar todos os itens das treeviews, atualizar os indicadores dos códigos da tabela
        user_n , além de inserir todos os códigos na treeview denovo
        """
        for i in self.treemajor.get_children():
            self.treemajor.delete(i)

        for i in self.treefundos.get_children():
            self.treefundos.delete(i)

        for i in self.treetesouro.get_children():
            self.treetesouro.delete(i)

        self.object_registro.update_registro(self.id_user)
        self.filltree()

    def delete(self):
        """
        Método responsável por deletar todos os items selecionados das treeviews
        """
        major = self.treemajor.selection()
        fundos = self.treefundos.selection()
        tesouro = self.treetesouro.selection()

        try:
            for i in range(len(major)):
                self.object_registro.delete_registro(self.id_user, self.treemajor.item(major[i])['text'])
                self.treemajor.delete(major[i])
        except:
            pass
        try:
            for i in range(len(fundos)):
                self.object_registro.delete_registro(self.id_user, self.treefundos.item(fundos[i])['text'])
                self.treefundos.delete(fundos[i])
        except:
            pass
        try:
            for i in range(len(tesouro)):
                self.object_registro.delete_registro(self.id_user, self.treetesouro.item(tesouro[i])['text'])
                self.treetesouro.delete(tesouro[i])
        except:
            pass

    def refreshT2T(self):
        """
        Método responsável por chamar o método refresh() de 1 em 1 minuto, assim atualizando os códigos periodicamente
        """
        self.refresh()
        self.wndcarteira.after(60000, self.refreshT2T)

    def main(self):
        """
        Método responsável por juntar todos os métodos
        """
        self.lbl_lgin_frm()
        self.rgst_cod_frm()
        self.treeview_frms()
        self.polishing_endloop()


if __name__ == "__main__":
    wndcart = WindowCarteira("user_1")
    wndcart.main()

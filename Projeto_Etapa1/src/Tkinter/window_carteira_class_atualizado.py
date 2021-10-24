from ttkbootstrap import Style
from tkinter import *
from tkinter.font import *
from tkinter import ttk
from src.MySQL.registro import RegistroMySQL
from src.Web_Scraping.statusinvest import Webscrapper


class WindowCarteira:
    def __init__(self, id_user):
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
        # Frame "lbl_lgin_frm" que conterá label e button, label "LOGIN", button "Config"
        # Frame lbl_lgin_frm
        lbl_lgin_frm = Frame(self.mainframe, bg="#3D3D3D")
        lbl_lgin_frm.pack(fill=X)
        lbl_lgin_frm.columnconfigure(0, weight=1)
        lbl_lgin_frm.rowconfigure(0, weight=1)
        # Label "CARTEIRA STALKER"
        lbl_log = Label(lbl_lgin_frm, text="CARTEIRA STALKER", background="#3D3D3D", fg="white",
                        font=Font(size=20, weight="bold"))
        lbl_log.pack()
        lbl_log.pack_configure()
        # Label "img_sett"
        # lbl_sett = Label(lbl_lgin_frm, text="img_sett", background="#3D3D3D", fg="white",
        #                  font=Font(family="Comic Sans Ms", size=15, weight="bold"))
        # lbl_sett.grid(row=0, column=1, sticky=(E))
        # lbl_sett.grid_configure(padx=5)

    def rgst_cod_frm(self):
        # Frame "self.rgst_cod_frm" que conterá labels, button, Entry Widgets
        # Frame self.rgst_cod_frm
        self.rgst_cod_frm = ttk.Frame(self.mainframe, style="TFrame")
        self.rgst_cod_frm.pack(fill=X)
        self.rgst_cod_frm.columnconfigure(0, weight=1)
        self.rgst_cod_frm.rowconfigure(0, weight=1)
        # Frame "self.space_frm" responsável pelo espaçamento dentro do Frame "self.rgst_cod_frm"
        self.space_frm = ttk.Frame(self.rgst_cod_frm, style="TFrame")
        self.space_frm.pack()
        self.space_frm.pack_configure(padx="0 70")
        # Label text="Código" e Entry "cod_entry"
        self.codvar = StringVar()
        ttk.Label(self.space_frm, text="Código", foreground="#3D3D3D",
                  font=Font(family="Arial #3D3D3D", size=12, weight="bold", underline=True)).grid(row=0, column=0, sticky=(W), padx="0 6", pady="10 10")
        cod_entry = ttk.Entry(self.space_frm, width=51, textvariable=self.codvar, style="primary.TEntry")
        cod_entry.grid(row=0, column=1, sticky=(W), pady="10 10")
        # Button "rgst_btn" e Legendas, não vou fazer as legendas agora
        rgst_btn = ttk.Button(self.space_frm, text="Registrar", command=self.registrar, style="primary.TButton") # TESTE
        rgst_btn.grid(row=1, column=1, sticky=(N, S, W, E))


    def treeview_frms(self):
        # $$##@@ MELHOR UTILIZAR tkinter.scrolledtext PARA APARECER AS IMAGENS DAS EMPRESAS
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
        # self.treemajor.column("#0", width=50)
        # self.treemajor.column("#1", width=100)
        # self.treemajor.column("#2", width=100)
        # self.treemajor.column("#3", width=100)
        # self.treemajor.column("#4", width=100)
        # self.treemajor.column("#5", width=100)
        # self.treemajor.column("#6", width=100)


        treemajor_scrollv = Scrollbar(treemajor_frm, orient=VERTICAL, command=self.treemajor.yview)
        treemajor_scrollh = Scrollbar(treemajor_frm, orient=HORIZONTAL, command=self.treemajor.xview)
        treemajor_scrollv.pack(side=RIGHT, fill=Y)
        treemajor_scrollh.pack(side=BOTTOM, fill=X)

        self.treemajor.configure(yscrollcommand=treemajor_scrollv.set)
        self.treemajor.configure(xscrollcommand=treemajor_scrollh.set)
        self.treemajor.pack(fill=X)

        treemajor_frm.pack(fill=X)

            # treefundos_frm
        treefundos_frm = LabelFrame(self.treeviews_frm_conjunt, text="Fundos de Ações", foreground="#3D3D3D", font=Font(family="Arial Black", size="10"))

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
        # self.treetesouro.column("#0", width=50)
        # self.treetesouro.column("#1", width=100)
        # self.treetesouro.column("#2", width=100)
        # self.treetesouro.column("#3", width=100)
        # self.treetesouro.column("#4", width=100)
        # self.treetesouro.column("#5", width=100)


        treetesouro_scrollv = Scrollbar(treetesouro_frm, orient=VERTICAL, command=self.treetesouro.yview)
        treetesouro_scrollh = Scrollbar(treetesouro_frm, orient=HORIZONTAL, command=self.treetesouro.xview)
        treetesouro_scrollv.pack(side=RIGHT, fill=Y)
        treetesouro_scrollh.pack(side=BOTTOM, fill=X)

        self.treetesouro.configure(yscrollcommand=treetesouro_scrollv.set)
        self.treetesouro.configure(xscrollcommand=treetesouro_scrollh.set)
        self.treetesouro.pack(fill=X)

        treetesouro_frm.pack(fill=X)

        self.filltree()  # Inserindo as informações nas treeviews

                # Inserindo os elementos nas treeviews
        # registros = self.object_registro.list_elements(user)
        # for indicadores in registros:
        #     if indicadores[1] == "Fundo de Investimento":
        #         msg = f"CÓDIGO:{indicadores[0]} | TIPO:{indicadores[1]} | RENTABILIDADE(12M):{indicadores[2]} | RENTABILIDADE(24M):{indicadores[3]} | VOLATILIDADE(12M):{indicadores[4]} | ÍNDICE DE SHARPE(6M):{indicadores[5]} | PATRIMÔNIO LÍQUIDO: {indicadores[6]} | PREÇO DA COTA: {indicadores[7]}"
        #     elif indicadores[1] == "Tesouro":
        #         msg = f"CÓDIGO:{indicadores[0]} | TIPO:{indicadores[1]} | VALOR UNITÁRIO:{indicadores[2]} | MIN. 52 SEM.:{indicadores[3]} | MÁX. 52 SEM.:{indicadores[4]} | VALORIZAÇÃO(12M):{indicadores[5]}"
        #     else:
        #         msg = f"CÓDIGO:{indicadores[0]} | TIPO:{indicadores[1]} | VALOR ATUAL:{indicadores[2]} | MIN. 52 SEM.:{indicadores[3]} | MÁX. 52 SEM.:{indicadores[4]} | DIVIDEND YIELD:{indicadores[5]} | VALORIZAÇÃO (12M):{indicadores[6]}"
        #     self.cbx.insert(END, msg)


        # teste
        # self.treetesouro.insert('', 'end', text='tesouro-prefixado', values=('R$ 718,77', "10,89 % a.a.", 'R$ 718,77',
        #                                                                      'R$ 792,82', "-4,88%"))
        # self.treefundos.insert('', 'end', text='FIA TRIGONO VERBIER',
        #                        values=("FIA TRIGONO VERBIER", "R$ 12,0408", '101,78 %', "134,77 %", '18,00 %',
        #                                '- %', "R$ 322,55 M"))
        # self.treemajor.insert('', 'end', text='CIEL3', values=("CIELO", 'R$ 2,37', "R$ 2,29", 'R$ 4,34',
        #                                                        '4,92 %', "-35,07%"))




    def polishing_endloop(self):
        # # POLIMENTOS
        # # Espaçamento dentro do frame "self.space_frm" que é child do frame "self.rgst_cod_frm"
        # for child in self.treeviews_frm_conjunt.winfo_children():
        #     child.pack_configure(pady=5)
        #     """# Espaçamento dentro do frame comboxox "self.treeviews_frm_conjunt"
        # for child in self.treeviews_frm_conjunt.winfo_children():
        #     child.pack_configure(pady=10, padx=5)"""

        self.wndcarteira.bind("<Return>", self.registrar)

        # Startando o Loopping
        self.wndcarteira.mainloop()

    # Parei aqui
    def into_wbscrapper(self) -> tuple:
        wb = Webscrapper()
        indicadores = wb.main(self.codvar.get())

        return indicadores

    def registrar(self, *args):
        stt = self.into_wbscrapper()
        if self.object_registro.registrar_registros(self.codvar.get().lower(), stt, self.id_user) != False:
            if stt[1] == "Ação" or stt[1] == "Fundo Imobiliario" or stt[1] == "BDRS":
                self.treemajor.insert('', 0, text=self.codvar.get().lower(), values=(stt[0][0], stt[0][2], stt[0][1],
                                                                                 stt[0][3], stt[0][4], stt[0][5]))
            elif stt[1] == "Fundo de Investimento":
                self.treefundos.insert('', 0, text=self.codvar.get().lower(), values=(stt[0][0], stt[0][1], stt[0][6],
                                                                            stt[0][2], stt[0][3], stt[0][4], stt[0][5]))
            elif stt[1] == "Tesouro":
                self.treetesouro.insert('', 0, text=self.codvar.get().lower(), values=(stt[0][1], stt[0][6], stt[0][2],
                                                                       stt[0][3], stt[0][4],))
        self.codvar.set("")

    def filltree(self):
        """
        Função que preenche as treeviews com os códigos da tabela code_user
        :param indicadores:
        :return:
        """
        registros = self.object_registro.list_elements(self.id_user)
        for i in registros:
             if i[1] == "Ação" or i[1] == "Fundo Imobiliario" or i[1] == "BDRS":
                 self.treemajor.insert('', 0, text=i[0], values=(i[2], i[3], i[4],
                                                                                  i[5], i[6], i[7]))
             elif i[1] == "Fundo de Investimento":
                 self.treefundos.insert('', 0, text=i[0], values=(i[2], i[3], i[4],
                                                                             i[5], i[6], i[7], i[8]))
             elif i[1] == "Tesouro":
                 self.treetesouro.insert('', 0, text=i[0], values=(i[3], i[2], i[4], i[5],
                                                                        i[6]))

    def main(self):
        self.lbl_lgin_frm()
        self.rgst_cod_frm()
        self.treeview_frms()
        self.polishing_endloop()

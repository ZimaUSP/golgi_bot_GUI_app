from datetime import datetime
import os
from fpdf import FPDF
from fpdf.enums import XPos, YPos

LOGO_PADRAO = "images/logo_hu.png"


def _wrap(pdf, texto, largura_max):
    """Quebra um texto em várias linhas para caber em 'largura_max' (mm),
    respeitando a fonte atualmente selecionada no PDF."""
    linhas, atual = [], ""
    for palavra in str(texto).split():
        teste = (atual + " " + palavra).strip()
        if pdf.get_string_width(teste) <= largura_max:
            atual = teste
        else:
            if atual:
                linhas.append(atual)
            atual = palavra
    if atual:
        linhas.append(atual)
    return linhas or [""]


class ReciboHU(FPDF):
    def __init__(self, dados, logo=LOGO_PADRAO, **kwargs):
        super().__init__(orientation="P", unit="mm", format="A4", **kwargs)
        self.dados = dados
        self.logo = logo

    def header(self):
        d = self.dados

        # ---- Logo no lugar do antigo "hu" ----
        if self.logo and os.path.exists(self.logo):
            # mantém a proporção da imagem (108x98 -> ~1.10)
            self.image(self.logo, x=5, y=9, w=17)
        else:
            self.set_xy(5, 10)
            self.set_font("Helvetica", "B", 22)
            self.cell(14, 12, "hu", border=0)

        # Dados do hospital
        self.set_xy(24, 9)
        self.set_font("Helvetica", "", 9)
        self.set_text_color(0, 0, 0)
        self.cell(0, 4, "Hospital Universitário da USP", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.set_x(24)
        self.set_font("Helvetica", "", 7.5)
        self.cell(0, 3.6, "Av. Pro. Lineu Prestes, 2565 - Cidade Universitária", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.set_x(24)
        self.cell(0, 3.6, "São Paulo/SP - Cep 05508-900  Fone: 3039-9200 - Fax: 3812-8004", new_x=XPos.LMARGIN, new_y=YPos.NEXT)

        # Horario atual
        agora = datetime.now()
        data_formatada = agora.strftime("%d/%m/%Y %H:%M:%S")
        print(data_formatada)

        # Bloco "Sistema Apolo" à direita
        self.set_xy(150, 9)
        self.set_font("Helvetica", "", 7.5)
        self.multi_cell(
            50, 3.6,
            f"{"Sistema Apolo"}\n{"Rel: SGM-001-V01"}\n{data_formatada}\n{"Página 1 de 1"}",
            align="L",
        )

        self.set_line_width(0.4)
        self.line(5, 28, 205, 28)

        # ---- Título ----
        self.set_xy(10, 30)
        self.set_font("Helvetica", "B", 16)
        self.cell(0, 9, "Recibo de Baixa", align="C",
                  new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.line(5, 38, 205, 38)

    def footer(self):
        # ---------- Rodapé com assinaturas ----------
        assinaturas_y = 245

        def bloco(y, rotulo, texto_lines=None):
            self.set_line_width(0.3)
            self.line(5, y, 205, y)
            self.set_xy(5, y + 2)
            self.set_font("Helvetica", "B", 9)
            self.cell(40, 5, rotulo)
            if texto_lines:
                self.set_font("Helvetica", "", 7)
                for i, t in enumerate(texto_lines):
                    self.set_xy(55, y + 2 + i * 3.2)
                    self.cell(80, 3.2, t)

        bloco(assinaturas_y + 10, "Conferido Por")
        bloco(assinaturas_y + 23, "Liberado Por")
        bloco(assinaturas_y + 36, "Recebido Por")

    def gerar_pdf(self, caminho="recibo_baixa.pdf"):
        pdf = ReciboHU(self.dados, logo=self.logo)
        pdf.set_auto_page_break(auto=False)
        pdf.set_margins(5, 5, 5)
        pdf.add_page()
        pdf.set_text_color(0, 0, 0)

        # ---------- Bloco de informações ----------
        y = 41
        pdf.set_xy(15, y)
        pdf.set_font("Helvetica", "B", 9)
        pdf.cell(16, 5, "Loja:")
        pdf.set_font("Helvetica", "", 9)
        pdf.set_xy(26, y)
        pdf.cell(0, 5, "DISP CONTROLADO")
        pdf.set_xy(150, y)
        pdf.set_font("Helvetica", "B", 9)
        pdf.cell(0, 5, f"Nº Baixa: {self.dados['num_baixa']}", align="R")

        pdf.set_line_width(0.4)
        pdf.line(5, y + 6, 205, y + 6)

        for rotulo, chave in [("Solicitante:", "solicitante"),
                            ("Operador:", "operador"),
                            ("Tipo Baixa:", "tipo_baixa")]:
            y += (9 if rotulo == "Solicitante:" else 7)
            x = (7 if rotulo == "Operador:" else 5.5 if rotulo == "Solicitante:" else 5)
            pdf.set_xy(x, y)
            pdf.set_font("Helvetica", "B", 9)
            pdf.cell(24, 5, rotulo)
            pdf.set_font("Helvetica", "", 9)
            pdf.set_xy(26, y)
            pdf.cell(0, 5, self.dados[chave])

        pdf.set_line_width(0.4)
        pdf.line(5, 73, 205, 73)

        # ---------- Cabeçalho da tabela ----------
        cols = {
            "sgm":      (15, 12),
            "item":     (27, 50),
            "paciente": (80, 38),
            "unidade":  (118, 30),
            "produto":  (142, 22),
            "um":       (168, 14),
            "qtd":      (178, 20),
        }
        y_head = 78
        pdf.set_font("Helvetica", "B", 8.5)
        pdf.set_xy(cols["sgm"][0], y_head);      pdf.cell(cols["sgm"][1], 5, "SGM")
        pdf.set_xy(cols["item"][0], y_head);     pdf.cell(cols["item"][1], 5, "Item")
        pdf.set_xy(cols["paciente"][0], y_head); pdf.cell(cols["paciente"][1], 5, "Paciente")
        pdf.set_xy(cols["unidade"][0], y_head - 4); pdf.cell(cols["unidade"][1], 5, "Unidade")
        pdf.set_xy(cols["unidade"][0], y_head);  pdf.cell(cols["unidade"][1], 5, "Consumo")
        pdf.set_xy(cols["produto"][0], y_head);  pdf.cell(cols["produto"][1], 5, "Produto")
        pdf.set_xy(cols["um"][0], y_head);       pdf.cell(cols["um"][1], 5, "U.M.")
        pdf.set_xy(cols["qtd"][0], y_head);      pdf.cell(cols["qtd"][1], 5, "Qtd", align="R")

        # ---------- Linhas (dinâmicas) ----------
        line_h = 3.8
        y_row = y_head + 7
        pdf.set_font("Helvetica", "", 8.5)

        for it in self.dados["itens"]:
            # quebra automática conforme a largura de cada coluna
            item_lines = _wrap(pdf, it.get("item", ""), cols["item"][1] - 2)
            paciente_lines = _wrap(pdf, it.get("paciente", ""), cols["paciente"][1] - 2)
            unid_lines = _wrap(pdf, it.get("unidade", ""), cols["unidade"][1] - 2)
            prod_lines = _wrap(pdf, it.get("produto", ""), cols["produto"][1] - 2)
            um_lines = _wrap(pdf, it.get("um", ""), cols["um"][1] - 2)

            pdf.set_xy(cols["sgm"][0], y_row)
            pdf.cell(cols["sgm"][1], line_h, str(it.get("sgm", "")))

            for i, t in enumerate(item_lines):
                pdf.set_xy(cols["item"][0], y_row + i * line_h)
                pdf.cell(cols["item"][1], line_h, t)

            for i, t in enumerate(paciente_lines):
                pdf.set_xy(cols["paciente"][0], y_row + i * line_h)
                pdf.cell(cols["paciente"][1], line_h, t)

            for i, t in enumerate(unid_lines):
                pdf.set_xy(cols["unidade"][0], y_row + i * line_h)
                pdf.cell(cols["unidade"][1], line_h, t)

            for i, t in enumerate(prod_lines):
                pdf.set_xy(cols["produto"][0], y_row + i * line_h)
                pdf.cell(cols["produto"][1], line_h, t)

            for i, t in enumerate(um_lines):
                pdf.set_xy(cols["um"][0], y_row + i * line_h)
                pdf.cell(cols["um"][1], line_h, t)

            pdf.set_xy(cols["qtd"][0], y_row)
            pdf.cell(cols["qtd"][1], line_h, str(it.get("qtd", "")), align="R")

            n = max(len(item_lines), len(unid_lines), len(prod_lines), len(um_lines), len(paciente_lines), 1)
            y_row += n * line_h + 2.5

            pdf.set_line_width(0.1)
            pdf.line(26, y_row - 2, 205, y_row - 2)

        pdf.output(caminho)
        return caminho


# ---------------------------------------------------------------------------
# EXEMPLO DE USO — edite este dicionário (ou monte outro) para cada recibo.
# ---------------------------------------------------------------------------
DADOS_EXEMPLO = {
    # Dados do cabeçalho do recibo
    "num_baixa": "1014870",
    "solicitante": "LILIAN ABGAIL RIBEIRO DE OLIVEIRA",
    "operador": "PAULO SERGIO ALVES DE LIMA",
    "tipo_baixa": "Baixa Outros Setores",

    # Lista de medicamentos 
    "itens": [
        {"sgm": "3548",
         "item": "TRAMADOL INJETAVEL 50 MG/ML 1 ML CONTROLADO (CADMAT 292382)",
         "paciente": "Nenhum Nenhum aaaaaa a aaabbb", "unidade": "PS ADULTO OBSERVACAO",
         "produto": "teste mto foda mto gamer", "um": "teste mto foda mto gamer", "qtd": "3,000"},
        {"sgm": "3352",
         "item": "HALOPERIDOL INJETAVEL 5 MG/ML 1 ML CONTROLADO (CADMAT 292196)",
         "paciente": "Nenhum", "unidade": "PS ADULTO OBSERVACAO",
         "produto": "", "um": "", "qtd": "1,000"},
        {"sgm": "3293",
         "item": "FENITOINA INJETAVEL 50 MG/ML 5 ML CONTROLADO (CADMAT 267107)",
         "paciente": "Nenhum", "unidade": "PS ADULTO OBSERVACAO",
         "produto": "", "um": "", "qtd": "1,00"},
        {"sgm": "3244",
         "item": "DIAZEPAM INJETAVEL 5 MG/ML 2 ML CONTROLADO (CADMAT 267194)",
         "paciente": "Nenhum", "unidade": "PS ADULTO OBSERVACAO",
         "produto": "", "um": "", "qtd": "1,00"},
    ]
}
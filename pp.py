import openpyxl
from const import *
'''
Importado o módulo const que para fins de organização e escalabilidade de código agrega constantes.
'''
from os import path
#Importada a classe 'path' da lib 'os' para consumo de seus métodos.

workbook_alunos = openpyxl.load_workbook(path.join(XLSX_PATH, 'alunos.xlsx')) #Utilizada a XLSX_PATH do módulo const.py, para referenciar o endereço da pasta onde ficam as planilhas.
'''
Foi incluso o endereçamento da planilha através da lib 'os' com a classe path utilizando o método
'.join' que remove a necessidade de escrever os endereços manualmente com '/' ou '\\', também
garantindo que esta união de endereços ocorra de acordo com o SO operante.
'''

sheet_alunos = workbook_alunos ['Sheet1']

for linha in sheet_alunos.iter_rows(min_row=2):

    nome_curso = linha [0].value # Nome do
    nome_participante= linha [1].value #г
    tipo_participacao= linha [2].value #t
    data_inicio= linha [3].value # data in
    data_final = linha [4].value # data ini
    carga_horaria= linha [5].value # carga
    data_emissao = linha [6].value # data e
    input('')
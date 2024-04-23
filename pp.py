import openpyxl


workbook_alunos = openpyxl.load_workbook('alunos.xlsx')



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
import os



MAIN_PATH = os.path.dirname(os.path.abspath(__file__))
'''MAIN_PATH - é a constante que agrega o endereço da pasta raiz do projeto.

'os.path.abspath()' coleta o diretório absoluto de alguma coisa, no caso utilizei __file__ que referencia 
o arquivo sendo executado. RESULTADO => d:\\repositorys\\automa_fork\\const.py

'os.path.dirname' coleta o diretório raiz de algo, no caso estamos colocando o resultado do diretório raiz do
arquivo const.py. d:\\repositorys\\automa_fork

'''


XLSX_PATH = os.path.join(MAIN_PATH, 'xlsx_path') 
'''Agora que temos em MAIN_PATH: 'd:\\repositorys\\automa_fork\\const.py', estaremos unindo com o .join a pasta xlsx_path
ficando assim: d:\\repositorys\\automa_fork\\const.py\\xlsx_path'''


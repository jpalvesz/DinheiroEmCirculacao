import requests
from sqlalchemy import create_engine
import pandas as pd
import os
from dotenv import load_dotenv

#Lendo Variaveis de ambiente
load_dotenv()
username = os.getenv('MYSQL_USERNAME')
password = os.getenv('MYSQL_PASSWORD')
database = os.getenv('MYSQL_DB')
host = os.getenv('MYSQL_HOST')

#requisicao e transformar em json
link = "https://olinda.bcb.gov.br/olinda/servico/mecir_dinheiro_em_circulacao/versao/v1/odata/informacoes_diarias?&$format=json&$select=Data,Quantidade,Valor,Denominacao,Especie"
requisicao = requests.get(link)
informacoes = requisicao.json()

#Criando DataFrame
tabela = pd.DataFrame (informacoes["value"])
tabela ["Quantidade"] = tabela["Quantidade"].map("{}".format)

#Mudando DataTypes para colocar no Banco
tabela["Valor"] = tabela["Valor"].astype(float)
tabela['Data'] = tabela['Data'].astype('datetime64[ns]')
tabela["Quantidade"] = tabela["Quantidade"].astype('Int64')
tabela['Denominacao'] = tabela['Denominacao'].astype(float)

#Instanciando a conexao
my_conn = create_engine("mysql+mysqldb://{0}:{1}@{2}/{3}".format(username,password,host,database))

#Criando a tabela no Banco de Dados através do DataFrame com o paramentro de se existir, reescrever
tabela.to_sql('money', con=my_conn, if_exists='replace')
print('Os dados foram gravados com sucesso')
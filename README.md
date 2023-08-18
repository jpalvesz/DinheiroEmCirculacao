# DinheiroEmCirculacao
## Nesse projeto eu extraio dados diários de dinheiro em circulação da API do Banco Central e insiro em um Banco MySql

### Pré-requisitos
Antes de começar, você vai precisar ter instalado em sua máquina a
seguinte ferramenta:
[Python](https://www.python.org/downloads/). 

Não se esqueça atualizar a variável de ambiente na instalação do python.

<img src="./img/python.png" />

Além disto é bom ter um editor para trabalhar com o código como [Atom](https://atom.io/)

### Variaveis de ambiente 
Acessar o arquivo .env e adicionar as credenciais do MySql

```bash
# MYSQL_USERNAME=
# MYSQL_PASSWORD=
# MYSQL_DB=
# MYSQL_HOST=
```

### 🎲 Rodando o Back End (servidor)

```bash
# Instale as dependências
$ pip install -r requirements.txt

# Execute a aplicação 
$ python app.py

```

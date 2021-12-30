#precisa intalar o pacote tqdm caso não tenha, com o comando > pip install tqdm
#abaixo foi importado apenas um pedaço da bilbioteca do tqdm como nome do tqdm
from tqdm import tqdm
import requests
import time

#dentro do tqdm() coloca o range para utilizar a barra
#fazendo com range
'''for i in tqdm(range(10)):
    time.sleep(1)'''

#fazendo com "lista"
'''lista = [1,2,3,10,15]
for i in tqdm(lista):
    time.sleep(1)'''

#outra forma
'''with tqdm(total=100) as barra_de_progresso:
    for i in range(10):
        time.sleep(1)
        barra_de_progresso.update(5)'''

#a partir daqui, iremos usar uma API para acessar um cep
#endereço da API: https://docs.awesomeapi.com.br/api-cep

#1) Pegar a lista de CEPs no arquivo TXT

with open("ceps.txt","r") as txt:
    ceps = txt.read()

    #O "\n" significa ENTER
    ceps = ceps.split("\n")
    #printa os CEPs que estão no TXT
    print(ceps)

#2) Pegar as informações de cada CEP
#cria matriz endereço para ser adicionada no for
enderecos = []

#Coloca a barra de progresso
for cep in tqdm(ceps):
    #colocando o cep que está no txt na linha da API, utilizando a variavel {cep}
    #O f é para formatar o texto da url para aceitar o valor de {cep}
    link = f'https://cep.awesomeapi.com.br/json/{cep}'

#3) Verificar se a cidade é de RJ
    #faz a requisição do link
    requisicao = requests.get(link)
    resposta = requisicao.json()

    #alimenta as variáveis com os dados em JSON vendo da API
    cidade = resposta['city']
    bairro = resposta['district']
    print(cep, bairro)
#4) Printart o CEP e o BAIRRO
    if cidade == "Rio de Janeiro":
        enderecos.append((cep, bairro))

#mostra os enderecos de Santos
print("enderecos")
print(enderecos)

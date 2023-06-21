# Webscraping Catalogo telefonico

# Importando as bibliotecas
from bs4 import BeautifulSoup
import requests
import re

# Fazendo a requisição na página de catálogos da CAT
resposta = requests.get("https://www2.ufjf.br/cat/contato/catalogo_contatos/")

# Armazenando o conteúdo da página na variável conteudo
conteudo = resposta.text

# Dando forma ao texto html com o Beautifulsoup
soup = BeautifulSoup(conteudo, 'html.parser')
print(10*'====='+'\n')

# Teste com 5 grupos: len(setores)
for i in range(0, 20):
  # Encontrando os nomes dos setores
  setores = soup.find_all('h3')

  # Exibindo o nome do setor
  print(setores[i].text+'\n')

  # Selecionando a coluna com o site, os telefones, os e-mails e redes sociais
  lista = soup.find_all('td', {'class':'column-2'})

  
  # Selecionando o site
  lista_site = lista[i].find_all('a',{'href':re.compile('http')})
  if lista_site == []:
    site = ''
  else:
    site = lista_site[0].text
    # Exibindo o site
  print(f'Site: {site}')
  print(30*'-'+'\n')
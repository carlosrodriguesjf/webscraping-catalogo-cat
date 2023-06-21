# WEBSCRAPING CATÁLOGO TELEFÔNICO DA CAT

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

# Looping para selecionar cada setor
for i in range(0, 30):

  # Encontrando e exibindo os nomes dos setores
  setores = soup.find_all('h3')
  print(setores[i].text+'\n')

  # Selecionando a coluna com o site, os telefones, os e-mails e redes sociais
  lista = soup.find_all('td', {'class':'column-2'})
  
  # Selecionando o site e o e-mail
  lista_site = lista[i].find_all('a',{'href':re.compile('http')})
  lista_emails = lista[i].find_all('a',{'href':re.compile('[\w\-.]+@[\w\-]+\.\w+')})

  if lista_emails == [] or lista_site == []:
    site = ''
    email = ''
  else:
    site = lista_site[0].text
    email = lista_emails[0].text
    # Exibindo o site
  print(f'Site: {site}')
  print(f'E-mail: {email}')
  print(30*'===='+'\n')

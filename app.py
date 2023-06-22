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

contador = soup.find_all('h3')
len(contador)

# Looping para selecionar cada setor

for i in range(0, len(contador)):

  # Encontrando e exibindo os nomes dos setores
  setores = soup.find_all('h3')
  print(setores[i].text+'\n')

  # Selecionando a coluna com o site, os telefones, os e-mails e redes sociais
  lista = soup.find_all('td', {'class':'column-2'})
  
  # Selecionando o site e o e-mail
  lista_site = lista[i].find_all('a',{'href':re.compile('http')})
  lista_emails = lista[i].find_all('a',{'href':re.compile('[\w\-.]+@[\w\-]+\.\w+')})

  # Código para selecionar telefones 
  telefones_code = str(lista[i])
  soup_tel = BeautifulSoup(telefones_code,'html.parser')
  soup_tel.get_text().find
  lista_telefones = re.findall('\([1-9]{2}\) [0-9]{4}[-][0-9]{4}.*',telefones_code)

  if lista_emails == [] or lista_site == []:
    site = ''
    email = ''
  else:
    site = lista_site[0].text
    email = lista_emails[0].text


  # Exibindo o site
  print(f'Site: {site}')
  print(f'E-mail: {email}')
  print('Telefone(s):')

  for i in range(0,len(lista_telefones)):
    telefone = lista_telefones[i].split('<')
    print(f'{telefone[0]} ')

  print(30*'===='+'\n')

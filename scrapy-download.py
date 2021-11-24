# Created By  : Anderval
# Created Date: 20/11/2021

import requests #Importa a Biblioteca requests
from bs4 import BeautifulSoup #Importa a Biblioteca BeautifulSoup

print("Starting scrap...")
for x in range(9): #loop que irá pecorrer o número de temporadas
  for i in range(12): #loop que irá pecorrer o número de episódios

    #Url utilizada para realizar o scrapy, a url recebe o numero da temporada e do episódio pelo loop
    url = "http://www.ayoitsdistrict78.com/album/abdc-season-{}-episode-{}/".format(x,i) 
    req = requests.get(url) #Envia uma resiquição get para a página
    soup = BeautifulSoup(req.content, 'html.parser') #recebe o conteúdo da página verificando os marcadores html

    for link in soup.find_all("li"): #loop que pecorre todos elementos li, os elementos li é onde estão nossos arquivos mp3
        linkMp3 = format(link.get("data-media")) #Armazenando o endereço que está na tag data-media
        nomeArquivo = nomeArquivo = linkMp3.split("/", -1)[-1] #Pegando o nome do arquivo à partir do da ultima parta da url

        if linkMp3.endswith(".mp3"): #Condicional que verifica se o endereço armazenado contem a extensão .mp3 
            print("Realizando o download do arquivo: "+ nomeArquivo)
            print(linkMp3)

            doc = requests.get(linkMp3) #Envia uma resiquição get para a página
            with open(nomeArquivo, 'wb') as f:#Abrindo o arquivo passando nome, e habilitando a escrita do arquivo binário
                f.write(doc.content) #Salvando o conteudo da requisição no arquivo
                f.close() #Fecha arquivo após a conclusão

    
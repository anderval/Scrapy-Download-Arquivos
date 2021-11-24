# Created By  : Anderval
# Created Date: 20/11/2021

from time import sleep
import requests  # Importa a Biblioteca requests
from bs4 import BeautifulSoup  # Importa a Biblioteca BeautifulSoup

print("Começando o scrap...")
for x in range(1, 9):  # loop que irá pecorrer o número de temporadas, começando da 1
    for y in range(1, 12):  # loop que irá pecorrer o número de episódios, começando do 1

        # Url utilizada para realizar o scrapy, a url recebe o numero da temporada e do episódio pelo loop
        url = "http://www.ayoitsdistrict78.com/album/abdc-season-{}-episode-{}/".format(
            x, y)

        res = requests.get(url)  # Envia uma resiquição get para a página
        # recebe o conteúdo da página verificando os marcadores html

        # continua o código apenas se a página existir
        if res.status_code != 200:
            break

        soup = BeautifulSoup(res.content, 'html.parser')

        # loop que pecorre todos elementos li, os elementos li é onde estão nossos arquivos mp3
        for link in soup.find_all("li"):
            # Armazenando o endereço que está na tag data-media
            linkMp3 = format(link.get("data-media"))
            # Pegando o nome do arquivo à partir do da ultima parta da url
            nomeArquivo = nomeArquivo = linkMp3.split("/", -1)[-1]

            # Condicional que verifica se o endereço armazenado contem a extensão .mp3
            if linkMp3.endswith(".mp3"):
                print("Realizando o download do arquivo: " + nomeArquivo)
                print(linkMp3)

                # Envia uma resiquição get para a página
                doc = requests.get(linkMp3)
                # Abrindo o arquivo passando nome, e habilitando a escrita do arquivo binário
                with open("./downloads/%s" % (nomeArquivo), 'wb') as f:
                    # Salvando o conteudo da requisição no arquivo
                    f.write(doc.content)

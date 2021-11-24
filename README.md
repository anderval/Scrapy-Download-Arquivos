# Scrapy-Download-Arquivos
O objetivo desse projeto é realizar o download automático de arquivos MP3 de uma página web. Ele pode ser modificado para realizar downloads de arquivos MP4s, PDFs, JPGs e etc.


## Desenvolvimento

http://www.ayoitsdistrict78.com/album/abdc-season-2-episode-1/


No site do District78 você consegue ouvir as músicas, mas não tem opção de download. Realizei a inspeção da página e localizei o link que levava para o arquivo .mp3 que era reproduzido

Com isso em mãos montei o script que percorre as páginas separadas por temporada/episódio, ele verifica se na página contêm arquivos com a extensão .mp3, e caso seja encontrado é realizado o download do arquivo. Após não ter mais arquivos nessa página, avança para o próximo episódio, quando não há mais episódios avança para a próxima temporada, e isso se repete até concluir todas as  temporadas.
## Execução

Para executar basta realizar o download do arquivo scrapy-download.py e abrir no terminal.

```bash
  scrapy-download.py

```
    
## Screenshots
Inspeção da página
![App Screenshot](https://user-images.githubusercontent.com/70353336/143153839-1ff19109-c936-4071-b525-5a0be1ea4211.png)

Script em Execução
![App Screenshot](https://user-images.githubusercontent.com/70353336/143153808-fc6c1036-9471-453c-b518-70a5a268ea8b.png)


## Authors

- [@Anderval](https://www.github.com/anderval)


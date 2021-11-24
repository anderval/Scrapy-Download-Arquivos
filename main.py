# Created By: Anderval
# Created On: 20/11/2021

import requests
from bs4 import BeautifulSoup  # Import scrapper


def main():

    print("Starting scrap...")
    for i in range(1, 9):  # loops through seasons
        for j in range(1, 12):  # loops through episodes

            url = "http://www.ayoitsdistrict78.com/album/abdc-season-%s-episode-%s/" % (
                i, j)
            res = requests.get(url)
            if res.status_code != 200:
                break

            soup = BeautifulSoup(res.content, 'html.parser')

            for link in soup.find_all("li"):
                # find url for download
                url_to_file = format(link.get("data-media"))
                # select original name from url string
                file_name = url_to_file.split("/", -1)[-1]

                # verify if url contains mp3 extension
                if url_to_file.endswith(".mp3"):
                    print("Starting download of the file: " + file_name)
                    print(url_to_file)

                    # request for file content
                    res = requests.get(url_to_file, stream=True)

                    # open a new file in binary
                    with open("./downloads/%s" % (file_name), 'wb') as f:
                        # write file to the hard drive
                        f.write(res.content)


if __name__ == "__main__":
    main()

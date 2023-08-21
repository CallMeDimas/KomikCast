import os
import sys
import requests
from bs4 import BeautifulSoup
from colorama import Fore, init

class KomikCast:
    def __init__(self):
        print(Fore.LIGHTCYAN_EX + """
        ╔═══════════════════════════════════╗
        ║      github.com/CallMeDimas/      ║
        ╟───────────────────────────────────╢
        ║  ╦╔═╔═╗    ╔═╗╔═╗╦═╗╔═╗╔═╗╔═╗╦═╗  ║
        ║  ╠╩╗║      ╚═╗║  ╠╦╝╠═╣╠═╝║╣ ╠╦╝  ║
        ║  ╩ ╩╚═╝────╚═╝╚═╝╩╚═╩ ╩╩  ╚═╝╩╚═  ║
        ╟───────────────────────────────────╢
        ║       KOMIKCAST.VIP SCRAPER       ║
        ╚═══════════════════════════════════╝
        """)
        print(Fore.WHITE + "Name: KomikCast Scraper")
        print(Fore.WHITE + "Author: CallMeDimas")
        print(Fore.WHITE + "Github: https://github.com/CallMeDimas/")
        print(Fore.WHITE + "Contact: callmedimas@proton.me")
        print(Fore.WHITE + "Version: v1.0.0")

    def _start_requests(self, url):
        meta_data = {}
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
        }

        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        contents = soup.select('div#content')
        meta_data['title'] = contents[0].find('h1').text
        raw_img = contents[0].find(class_='main-reading-area').find_all('img')
        meta_data['img_srcs'] = [img.get('src') for img in raw_img]
        return meta_data

    def _creating_directory(self, sub_folder):
        directory_name = f'downloads/{sub_folder}/'
        if not os.path.exists(directory_name):
            os.makedirs(directory_name)
        else:
            return 'Directory exists'
        return directory_name

    def download_images(self, url):
        meta_data = self._start_requests(url)
        directory_name = self._creating_directory(meta_data['title'])

        if directory_name == 'Directory exists':
            print(f'\n{Fore.GREEN}Chapter already downloaded!\n')
            sys.exit(0)

        counter = 1
        print(f'\nManga title: {meta_data["title"]}')
        for src in meta_data['img_srcs']:
            response = requests.get(src, stream=True)
            with open(os.path.join(directory_name, f'{counter}.jpg'), 'wb') as out_file:
                out_file.write(response.content)
            print(f'Successfully download page number {counter}!')
            counter += 1

        return counter


def main():
    url = input('\nEnter the Chapter Link: ')
    os.system('cls' if os.name == 'nt' else 'clear')
    manga = KomikCast()
    count = manga.download_images(url)
    print(f'\n{Fore.GREEN}Successfully download {count} images!\n')

if __name__ == "__main__":
    main()

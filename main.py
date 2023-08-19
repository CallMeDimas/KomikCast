import os
import requests
from bs4 import BeautifulSoup
from colorama import Fore, init

init()
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



def scrape_manga_chapter(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }

    response = requests.get(url, headers=headers)

    soup = BeautifulSoup(response.text, 'html.parser')

    div_element1 = soup.find(class_="chapter_headpost")
    h1_element = div_element1.find('h1')
    title = h1_element.get_text()

    div_element = soup.find(class_="main-reading-area")

    img_elements = div_element.find_all('img')

    img_srcs = [img.get('src') for img in img_elements]

    return title, img_srcs

def download_images(img_srcs, directory='images'):
    if not os.path.exists(directory):
        os.makedirs(directory)

    count = 0
    for i, src in enumerate(img_srcs):
        response = requests.get(src, stream=True)
        with open(os.path.join(directory, 'image{}.jpg'.format(i)), 'wb') as out_file:
            out_file.write(response.content)
        print('Downloaded... image{}'.format(i))
        count += 1

    return count

def main():
    url = input('\nEnter the Chapter Link: ')

    os.system('cls' if os.name == 'nt' else 'clear')

    title, img_srcs = scrape_manga_chapter(url)
    
    print(f'Manga Title: {title}\n')
    
    count = download_images(img_srcs)

    print(f'\n{Fore.GREEN}Successfully Downloaded: {count} images\n')

if __name__ == "__main__":
    main()

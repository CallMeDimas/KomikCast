# KomikCast Scraper

### 🇮🇩 Pemasangan:
1. Buka terminal atau command prompt, kemudian clone respository ini.

    ```sh
    git clone https://github.com/CallMeDimas/KomikCast.git
    ```

2. Masuk ke folder KomikCast.

    - Windows
    ```sh
    # cd \lokasi\folder\dari\respositori\ini\
    # contoh
    cd D:\Git\KomikCast\
    ```
    - Linux
    ```sh
    # cd /lokasi/folder/dari/respositori/ini/
    # contoh
    cd ~/Git/KomikCast/
    ```

3. Siapkan environment variable

    - Windows
    ```sh
    python -m venv Env
    Env\Scripts\activate
    ```
    - Linux
    ```sh
    python -m venv Env
    # bash/sh user
    . Env/bin/activate
    # fish user
    . Env/bin/activate.fish
    ```

4. Install dependency-nya.

    ```sh
    pip install -r requirements.txt
    ```

5. Jalankan programnya.

    ```sh
    python main.py
    # atau
    python3 main.py
    ```

6. Contoh URL:

    ```sh
    https://komikcast.vip/chapter/netoge-no-yome-ga-ninki-idol-datta-chapter-01-bahasa-indonesia/
    ```
7. Selesai! Hasil unduhan bisa dicek di folder downloads. Hasilnya akan seperti ini:

    ```sh
    (Env) (KomikCast) (* main ↑) >>> tree -L 1 downloads/
    downloads/
    ├── Netoge no Yome ga Ninki Idol datta Chapter 01 Bahasa Indonesia
    ├── Netoge no Yome ga Ninki Idol datta Chapter 02 Bahasa Indonesia
    └── Oukoku no Saishuu Heiki, Rettousei to shite Kishi Gakuin e Chapter 01.1 Bahasa Indonesia

    4 directories, 0 files
    ```
    
# 🇬🇧 ENGLISH
### Installation:
1. Open a terminal or command prompt, then clone this repository.
    ```sh
    git clone https://github.com/CallMeDimas/KomikCast.git
    ```
2. Navigate to the KomikCast folder.

    &nbsp;Windows
    ```sh
    # cd \location\to\this\repository\
    # example
    cd D:\Git\KomikCast\
    ```
    &nbsp;Linux
    ```sh
    # cd /location/to/this/repository/
    # example
    cd ~/Git/KomikCast/
    ```

3. Set up the environment variable.

    &nbsp;Windows
    ```sh
    python -m venv Env
    Env\Scripts\activate
    ```
    &nbsp;Linux
    ```sh
    python -m venv Env
    # bash/sh user
    . Env/bin/activate
    # fish user
    . Env/bin/activate.fish
    ```
    
4. Install dependency.

    ```sh
    pip install -r requirements.txt
    ```

5. Run the program.

    ```sh
    python main.py
    # or
    python3 main.py
    ```

6. Example URL:

    ```sh
    https://komikcast.vip/chapter/netoge-no-yome-ga-ninki-idol-datta-chapter-01-bahasa-indonesia/
    ```

7. Done! Downloaded results can be checked in the downloads folder. The result will look like this:
    ```sh
    (Env) (KomikCast) (* main ↑) >>> tree -L 1 downloads/
    downloads/
    ├── Netoge no Yome ga Ninki Idol datta Chapter 01 Bahasa Indonesia
    ├── Netoge no Yome ga Ninki Idol datta Chapter 02 Bahasa Indonesia
    └── Oukoku no Saishuu Heiki, Rettousei to shite Kishi Gakuin e Chapter 01.1 Bahasa Indonesia

    4 directories, 0 files
    ```
    
HAVE SOME COMPLAINT?... HIT ME AT `callmedimas@proton.me`

import requests
import time
import colorama
from colorama import Fore, Back, Style

colorama.init()


banner = """
 .----..-. .-..----. .----.  .----. .----..-..-. .-..----.
{ {__  | { } || {}  }| {}  \/  {}  \| {_  | ||  `| || {_  
.-._} }| {_} || {}  }|     /\      /| |   | || |\  || {__ 
`----' `-----'`----' `----'  `----' `-'   `-'`-' `-'`----'
                     [By H04x]

"""

def check_keyword_in_subdomain(subdomain, keyword):
    try:
        response = requests.get(subdomain)
        if keyword in response.text:
            return True
        else:
            return False
    except requests.RequestException as e:
        return False

print(Fore.MAGENTA)
print(banner)
print(Fore.CYAN)

def main():
    domain = input("Lütfen Bir Domain Girin \n> ")
    wordlist_path = input("Lütfen Wordlist Konumu Girin \n> ")
    protocol_choice = input("HTTP(0) / HTTPS(1 - Deffault) \n> ")


    if protocol_choice == "":
        protocol_choice = "1"

    if protocol_choice == "0":
        protocol = "http"
    else:
        protocol = "https"


    successful_urls = []

    with open(wordlist_path, 'r') as file:
        for line in file:
            keyword = line.strip()
            subdomain = f"{protocol}://{keyword}.{domain}"

            if check_keyword_in_subdomain(subdomain, keyword):
                print(Fore.GREEN)
                print(f"[+] {subdomain}")
                successful_urls.append(subdomain)
            else:
                print(Fore.RED)
                print(f"[-] {subdomain}")


    with open("sonuc.txt", 'w') as output_file:
        for url in successful_urls:
            output_file.write(url + "\n")
    print(Fore.LIGHTMAGENTA_EX)
    print("[i] İşlem Başarılı <sonuc.txt> olarak kaydedildi!")


    time.sleep(5)

if __name__ == "__main__":
    main()

import random
import string
import requests
import os
import time
from colorama import Fore, Style, init


init(autoreset=True)


def generate_nitro_code():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=16))


def check_nitro_code(code):
    url = f"https://discord.com/api/v9/entitlements/gift-codes/{code}?with_application=false&with_subscription_plan=true"
    try:
        response = requests.get(url, timeout=2)
        if response.status_code == 200:
            return True
        else:
            return False
    except requests.exceptions.RequestException:
        return False


def write_valid_code(code):
    with open("valid.txt", "a") as f:
        f.write(f"https://discord.gift/{code}\n")
    print(f"{Fore.GREEN}[VALID] https://discord.gift/{code} {Style.RESET_ALL}")


def main():
    os.system('cls' if os.name == 'nt' else 'clear') 

    print(Fore.RED + """

                               /$$         /$$                                                       /$$
                              /$$/        |__/                                                      | $$
      /$$$$$$   /$$$$$$      /$$//$$$$$$$  /$$ /$$$$$$$  /$$  /$$$$$$  /$$$$$$/$$$$   /$$$$$$   /$$$$$$$
     /$$__  $$ /$$__  $$    /$$/| $$__  $$| $$| $$__  $$|__/ |____  $$| $$_  $$_  $$ /$$__  $$ /$$__  $$
    | $$  \ $$| $$  \ $$   /$$/ | $$  \ $$| $$| $$  \ $$ /$$  /$$$$$$$| $$ \ $$ \ $$| $$  \ $$| $$  | $$
    | $$  | $$| $$  | $$  /$$/  | $$  | $$| $$| $$  | $$| $$ /$$__  $$| $$ | $$ | $$| $$  | $$| $$  | $$
 /$$|  $$$$$$$|  $$$$$$$ /$$/   | $$  | $$| $$| $$  | $$| $$|  $$$$$$$| $$ | $$ | $$|  $$$$$$/|  $$$$$$$
|__/ \____  $$ \____  $$|__/    |__/  |__/|__/|__/  |__/| $$ \_______/|__/ |__/ |__/ \______/  \_______/
     /$$  \ $$ /$$  \ $$                           /$$  | $$                                            
    |  $$$$$$/|  $$$$$$/                          |  $$$$$$/                                            
     \______/  \______/                            \______/                                             
""" + Style.RESET_ALL)

    print(Fore.RED + "[1] Generate N1tr0 Codes" + Style.RESET_ALL)
    print(Fore.RED + "[2] Support" + Style.RESET_ALL)
    choice = input(Fore.RED + "Entrez votre choix : " + Style.RESET_ALL)

    if choice == "1":
        num_codes = int(input(Fore.RED + "Combien de codes voulez-vous générer ? " + Style.RESET_ALL))
        print(Fore.YELLOW + "\nGénération des codes Nitro... (Appuyez sur CTRL+C pour arrêter à tout moment)\n" + Style.RESET_ALL)

        for _ in range(num_codes):
            code = generate_nitro_code()
            full_code = f"https://discord.gift/{code}"

            if check_nitro_code(code):
                write_valid_code(code)
            else:
                print(f"{Fore.RED}[INVALID] {full_code} {Style.RESET_ALL}")

    elif choice == "2":
        os.system("start https://discord.com/invite/ninjamod")
    else:
        print(Fore.RED + "Choix invalide. Réessayez..." + Style.RESET_ALL)

if __name__ == "__main__":
    main()

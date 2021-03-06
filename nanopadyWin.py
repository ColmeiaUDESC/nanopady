import requests
from bs4 import BeautifulSoup
import os
import hashlib


def getText(dontpad):
    link = requests.get(dontpad)
    soup = BeautifulSoup(link.text, "html.parser")
    text = soup.find('textarea').get_text()
    return text


def end():
    os.system("cls")
    print("\nBye!")
    exit()


def read(dontpad):
    os.system("cls")
    text = getText(dontpad)
    print(text)
    mainmenu = input(
        "Press r to return to main menu, or any other key to exit\n").lower()
    if mainmenu == "r":
        main()
    else:
        end()


def write(dontpad):
    text = getText(dontpad)
    buffer = open("buffer.txt", "w+")
    buffer.write(text)
    buffer.close()
    os.system("notepad buffer.txt")
    with open('buffer.txt', 'r') as myfile:
        text = myfile.read()
    data = {'text': text}
    r = requests.post(url=dontpad, data=data)

    # cls notepad buffer
    os.system("del /f buffer.txt")

    # clear the screen
    os.system("cls")

    mainmenu = input(
        "Press r to return to main menu, or any other key to exit\n").lower()
    if mainmenu == "r":
        main()
    else:
        end()


def main():
    try:
       # clear the screen
        os.system("cls")

        # options
        valid = False
        while(valid == False):
            print("Welcome to notepady!\n")
            print("Ctrl+d to exit\n")
            print("What do you want to do?\n")
            print("1 - Read from a dontpad address (dontpad.com/address)")
            print("2 - Write on a dontpad address (dontpad.com/address)")
            opt = input()
            if(opt == "1" or opt == "2"):
                valid = True
            else:
                print("Enter a valid option!")
        # address do dontpad
        endereco = input("Type the dontpad address: ")

        # check if the user wants to use hash on the URL
        valid = False
        while(valid == False):
            hashopt = input("Do you use hash for your address? [y,n] ").lower()
            if(hashopt == "y" or hashopt == "n"):
                valid = True
            else:
                print("Enter a valid option!")

        # runs the hash function
        if (hashopt == "y"):

            # clear the screen
            os.system("cls")

            valid = False
            while(valid == False):
                # opcoes de hash
                print("What kind of hash do you use?")
                print("1 - MD5")
                print("2 - SHA1")
                print("3 - SHA256")
                print("4 - SHA512")
                hashopt = int(input())

                # check the users option
                if hashopt == 1:
                    endereco = hashlib.md5(endereco.encode()).hexdigest()
                    valid = True
                elif hashopt == 2:
                    endereco = hashlib.sha1(endereco.encode()).hexdigest()
                    valid = True
                elif hashopt == 3:
                    endereco = hashlib.sha256(endereco.encode()).hexdigest()
                    valid = True
                elif hashopt == 4:
                    endereco = hashlib.sha512(endereco.encode()).hexdigest()
                    valid = True
                else:
                    print("Enter a valid option!")

        # runs the option mainmenu
        if opt == "1":
            read("http://dontpad.com/"+endereco+"/")
        elif opt == "2":
            write("http://dontpad.com/"+endereco+"/")

    except EOFError:
        end()


# main initial call
main()
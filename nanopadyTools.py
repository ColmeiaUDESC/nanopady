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
    os.system("clear")
    print("\nBye!")
    exit()


def write(dontpad):
    text = getText(dontpad)
    buffer = open("buffer.txt", "w+")
    buffer.write(text)
    buffer.close()
    print("What text editor do you want to use?\n")
    print("1 - Nano (default)")
    print("2 - Vim")
    if(input() == "2"):
        os.system("vim buffer.txt")
    else:
        os.system("nano buffer.txt")
    with open('buffer.txt', 'r') as myfile:
        text = myfile.read()
    data = {'text': text}
    r = requests.post(url=dontpad, data=data)

    # clear nano buffer
    os.system("rm buffer.txt")

    # clear the screen
    os.system("clear")

    mainmenu = input(
        "Press r to return to main menu, or any other key to exit\n").lower()
    if mainmenu == "r":
        main()
    else:
        end()


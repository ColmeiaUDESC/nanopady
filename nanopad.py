import requests
from bs4 import BeautifulSoup
import os

def getText(dontpad):
    link = requests.get(dontpad)
    soup = BeautifulSoup(link.text,"html.parser")
    text = soup.find('textarea').get_text()
    return text

def read(dontpad):
    text = getText(dontpad)
    print(text)

def write(dontpad):
    text = getText(dontpad)
    buffer = open("buffer.txt","w+")
    buffer.write(text)
    buffer.close()
    os.system("nano buffer.txt")
    with open('buffer.txt', 'r') as myfile:
        text = myfile.read()
    data = {'text':text}
    r = requests.post(url = dontpad, data = data)
    print(text)

print("Navigation menu: ")
barra = input("Type the dontpad /address: ")
dontpad = ("http://dontpad.com/"+barra+"/")
print("What is your desired action?")
print("1 - Read\n2 - Write")
o = int(input("Select one option: "))

if o == 1:
    read(dontpad)
elif o == 2:
    write(dontpad)

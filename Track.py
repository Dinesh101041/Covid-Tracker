import requests
import bs4

import tkinter as tk

def  get_html_data(url):
    data = requests.get(url)
    return data

def get_coivid():
    url="https://www.worldometers.info/coronavirus/"
    html_data=get_html_data(url)
    bs = bs4.BeautifulSoup(html_data.text,'html.parser')
    info=bs.find("div",class_ ="content-inner").findAll("div",id="maincounter-wrap")
    alldata=""

    for block in info:
        text=block.find("h1",class_=None).get_text()
        count=block.find("span", class_=None).get_text()
        alldata=alldata + text + " " + count + "\n"
     
    return alldata

def get_country():
    name=textfield.get()
    url="https://www.worldometers.info/coronavirus/country/"+name
    html_data=get_html_data(url)
    bs = bs4.BeautifulSoup(html_data.text,'html.parser')
    info=bs.find("div",class_ ="content-inner").findAll("div",id="maincounter-wrap")
    alldata=""

    for block in info:
        text=block.find("h1",class_=None).get_text()
        count=block.find("span", class_=None).get_text()
        alldata=alldata + text + " " + count + "\n"
     
    mainlabel['text']=alldata



def reload():
   new_data=get_coivid()
   mainlabel['text']=new_data



get_coivid()

root = tk.Tk()
root.geometry("800x900")
root.title("Covid Tracker")
f=("Arial",28,"bold")

banner = tk.PhotoImage(file="cor.png")
bannerlabel=tk.Label(root,image=banner)
bannerlabel.pack()

tk.Label(root, text="Enter your country name and click get data").pack()

textfield=tk.Entry(root,width=50)
textfield.pack()

mainlabel=tk.Label(root, text= get_coivid(), font=f )
mainlabel.pack()

gbtn=tk.Button(root,text="Get Data",relief='solid', command=get_country, padx=10, pady=10)
gbtn.pack()



rbtn=tk.Button(root,text="Reload",relief='solid', command=reload, padx=10, pady=10)
rbtn.pack()


root.mainloop()



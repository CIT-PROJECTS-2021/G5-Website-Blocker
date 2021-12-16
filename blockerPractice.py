#Importing all modules from the Tkinter library
from tkinter import * 

root=Tk()
root.geometry('500x300')
root.resizable(0,0)
root.bg = 'Green'
root.title("G5 Website Blocker")

#Label() widget is used to display one or more than one line of text that users aren’t able to modify.
Label(root,text = "WEBSITE BLOCKER",font='arial 20 bold').pack()
Label(root,text = "CIT-G5",font='arial 20 bold').pack(side=BOTTOM)

#Create an entry widget
host_path = "C:\Windows\System32\drivers\etc\hosts"
ip_address = '127.0.0.1'
Label(root, text = 'Enter Website:', font = 'arial 13 bold').place(x = 5, y = 60)
Websites = Text(root,font = 'arial 10', height = '2', width = '40', wrap = WORD, padx = 5, pady = 5)
Websites.place(x = 140,y = 60)

#define function
def Blocker():

    website_lists = Websites.get(1.0, END)
    Website = list(website_lists.split(","))

    with open(host_path,'r+') as host_file:
        file_content = host_file.read()
        for website in Website:
            if website in file_content:
                Label(root,text = 'Already Blocked', font = 'arial 12 bold').place(x = 200,y = 200)
                pass
            else:
                host_file.write(ip_address + "" + website + '\n')
                Label(root, text = "Blocked", font = 'arial 12 bold').place(x=230,y=200)

#Create a block button
block = Button(root, text = 'Block', font = 'arial 12 bold', pady = 5, command = Blocker, width = 6, bg = 'royal blue1', activebackground = 'sky blue')
block.place(x = 230, y = 150)
root.mainloop()
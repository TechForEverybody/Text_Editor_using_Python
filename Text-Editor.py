from tkinter import * 
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os
class Editor(Tk):
    file=None
    font=20
    def __init__(self,title,size):
        self.sk=Tk()
        self.sk.title(title)
        self.sk.geometry(size)
        self.menubar=Menu(self.sk,tearoff=0)
        self.sk.config(menu=self.menubar)
        
    def createMenu(self,menuname):
        self.menu=Menu(self.menubar,tearoff=0)
        self.menubar.add_cascade(label=menuname,menu=self.menu)

    def createSubMenu(self,menuname,command=None):
        self.menu.add_command(label=menuname,command=command)

    def Createtextarea(self):
        self.textArea=Text(self.sk,font="ROMEN 20")
        self.textArea.pack(fill=BOTH,expand=True)
        self.Scroll=Scrollbar(self.textArea)
        self.Scroll.pack(fill=Y,side=RIGHT)
        self.Scroll.config(command=self.textArea.yview)
        self.textArea.config(yscrollcommand=self.Scroll.set)

    def createSubmenuForFontSize(self,menuname):
        self.submenu=Menu(self.menu,tearoff=0)
        self.submenu.add_command(label="10--",command=lambda:self.ChangeFont("decrease"))
        self.submenu.add_command(label="10++",command=lambda:self.ChangeFont("increase"))
        self.menu.add_cascade(label=menuname,menu=self.submenu)

    def newfile(self):
        self.sk.title("utitled file -Shiv's editor")
        self.textArea.delete(1.0,END)

    def openfile(self):
        self.file=askopenfilename(defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documents","*.txt")])
        if self.file=="":
            self.file=None
        else:
            self.sk.title(os.path.basename(self.file)+"-Sk`s Editor")
            self.textArea.delete(1.0,END)
            with open(self.file,"r") as f:
                self.textArea.insert(1.0,f"""{f.read()}""")

    def savefile(self):
        if self.file ==None:
            self.file=asksaveasfilename(initialfile="UNTITLED.txt",defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documents","*.txt")])
            if self.file=="":
                self.file=None
            else:
                with open(self.file,"w") as f:
                    f.write(self.textArea.get(1.0,END))
                self.sk.title(os.path.basename(self.file)+"SK`s editior")
        else:
            with open(self.file,"w") as f:
                    f.write(self.textArea.get(1.0,END))

    def exitfile(self):
        exit()

    def cut(self):
        self.textArea.event_generate(("<<Cut>>"))

    def copy(self):
        self.textArea.event_generate(("<<Copy>>"))

    def paste(self):
        self.textArea.event_generate(("<<Paste>>"))

    def ChangeFont(self,type):
        if type=="increase":
            self.font=self.font+10
            self.textArea.configure(font=f"ROMEN {self.font}")
        if type=="decrease":
            self.font=self.font-10
            self.textArea.configure(font=f"ROMEN {self.font}")

    def about(self):
        showinfo("SK Editor","This Editor is created by Shivkumar chauhan")
        
    def ShowGUI(self):
        self.sk.mainloop()


if __name__=="__main__":
    sk=Editor("Shivkumar-EDITOR","600x500")
    sk.Createtextarea()
    sk.createMenu("file")
    sk.createSubMenu("New File",sk.newfile)
    sk.createSubMenu("Open File",sk.openfile)
    sk.createSubMenu("Save File",sk.savefile)
    sk.createSubMenu("exit",sk.exitfile)
    sk.createMenu("edit")
    sk.createSubMenu("copy",sk.copy)
    sk.createSubMenu("cut",sk.cut)
    sk.createSubMenu("paste",sk.paste)
    sk.createMenu("view")
    sk.createSubmenuForFontSize("Change Font Size")
    sk.createMenu("help")
    sk.createSubMenu("about",sk.about)
    sk.ShowGUI()
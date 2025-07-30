from  tkinter import *
from tkinter import messagebox

class Janela(Tk):
    
    fonteTitulo = ('Arial',18)
    fonteTexto = ('Arial',14)
    
    def __init__(self):
        super().__init__()
    
    def Titulo(self,texto):
        infor = Label(self,
                     text=texto,
                     font=self.fonteTitulo)
        infor.pack()
    
    def Texto(self,texto):
        return Label(self,
                     text=texto,
                     font=self.fonteTexto).pack()
    
    def CampoTexto(self):
        txt = Entry(self,font=self.fonteTexto)
        txt.pack()
        return txt
    
    def CampoSenha(self):
        txt = Entry(self,font=self.fonteTexto,show="*")
        txt.pack()
        return txt
    
    def Botao(self,texto,evento):
        return Button(self,
                     text=texto,command=evento,
                     font=self.fonteTexto).pack()
        
    def MensagemOK(self, mensagem):
        return messagebox.showinfo('Informação',mensagem)
    
from tkinter import *
from libFrame import Janela

class Cadastro(Janela):
    base = []
    def __init__(self):
        super().__init__()
        
        self.Titulo('Cadastro')
        
        self.Texto('Nome:')
        self.nome = self.CampoTexto()
        
        self.Texto('E-mail:')
        self.email = self.CampoTexto()
        
        self.Texto('Senha:')
        self.senha = self.CampoSenha()
        
        self.Botao("Cadastrar",self.salvar)
        
        self.Botao("Listar usuários",self.listar)
        
    def salvar(self):
        id = len(self.base)+1
        for e in self.base:
            if e[2] != self.email.get():
                self.base.append((id,self.nome.get(), self.email.get(),self.senha.get()))
        if id == len(self.base):
            self.MensagemOK("Usuário já existe!")
            self.base.pop()
        else:
            self.MensagemOK("Usuário salvo com sucesso!")
            
    def listar(self):
        for e in self.base:
            print(e)
Cadastro().mainloop()
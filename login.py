class Login:
     logado = False
    
     def login(self, senha):
        if (senha == '123'):
            self.logado = True
        else:
            raise ValueError("Senha incorreta!")
    
     def logout(self):
        self.logado = False
        
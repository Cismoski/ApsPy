# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
from user import User

class ValidateStrategy(object):
    def login(self,User):
        print ("A classe deve implementar o metodo login")
    
class DigitalImpression(ValidateStrategy):
    def login(self,User):
        print("Conectando via leitor digital")
        return True
    
class Typing(object):
    def login(self,user):
        self.User = user
        if((self.User.get_login() == "root") and True):
            return True
        else:
            return False

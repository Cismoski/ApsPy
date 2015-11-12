# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
from user import User
from validate_strategy import *

class Ifolder(object):
    def do_something(self):
        print("A classe deve implementar do something")
            
class FolderProxy(Ifolder):
    def __init__(self,User,ValidateStrategy):
        self.validateStrategy = ValidateStrategy
        self.User = User
    def do_something(self):
        if(self.validateStrategy.login(self.User) == True):
            self.User.set_state(self.User.get_connected()) 
            self.User.send_message()
            folder = Folder(self,self.validateStrategy)
            folder.do_something()
        else:
            self.User.send_message()
            
            
class Folder(FolderProxy):
     
    def do_something(self):
        print ("Realizando as operacoes solicitadas para esse diretorio")
        
            

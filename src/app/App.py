#! /usr/bin/python

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
from user import User
from folder_proxy import Ifolder
from validate_strategy import ValidateStrategy


__author__ = "Gabriel"
__date__ = "$03/11/2015 00:26:53$"

if __name__ == "__main__":
    type = ValidateStrategy.Typing() 
    usuario = User.User("root","123456")
    folder = Ifolder.FolderProxy(usuario,type)
    folder.do_something()
    usuario.print_all()

    
   

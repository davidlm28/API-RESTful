from datetime import datetime
from typing import List



class Post():
    def __init__(self, titulo:str, texto:str, creation_date :datetime=datetime.now(), id:int = 1):
        self.__titulo = titulo
        self.__texto = texto
        self.__creation_date = creation_date
        self.__id = id
    
    @property
    def titulo(self):
        return self.__titulo
    @property
    def texto(self):
        return self.__texto
    @property
    def creation_date(self):
        return self.__creation_date
    @property
    def id(self):
        return self.__id
    
    def to_json(self):
        json_user = {
            "Título": self.__titulo,
            "Texto" : self.__texto,
            "id": self.__id
        }
        return json_user
    
    def set_id(self, new_id):
        self.__id = new_id
    
    def set_titulo(self, new_titulo):
        self.__titulo = new_titulo

    def set_texto(self, new_texto):
        self.__texto = new_texto
    
    def set_date(self):
        self.__date = datetime.now()

    def to_str(self):
        return 'título: '+ self.__titulo +'   texto: '+ self.__texto

    def __eq__(self, other) -> bool:
        return self.__titulo == other.__titulo and self.__texto == other.__texto



class Usuario():
    def __init__(self, nombre:str, usuario:str, email:str, amigos:List=[], posts:List[Post]=[]):
        self.__nombre = nombre
        self.__email = email
        self.__amigos = amigos
        self.__posts = posts
        self.__usuario = usuario
    @property
    def nombre(self):
        return self.__nombre
    @property
    def email(self):
        return self.__email
    @property
    def usuario(self):
        return self.__usuario
    @property
    def amigos(self):
        return self.__amigos
    @property
    def posts(self):
        return self.__posts
    
    def set_nombre(self, nombre_new):
        self.__nombre = nombre_new
    
    def set_usuario(self, usuario_new):
        self.__usuario = usuario_new
    
    def set_email(self, email_new):
        self.__email = email_new

    def add_post(self, post_new):
        self.__posts += [post_new]
    
    def add_amigo(self, nombre_new):
        self.__amigos += [nombre_new]
    
    def remove_post(self, old_post):
        del self.__posts[self.__posts.index(old_post)]
    
    def remove_amigo(self, old_amigo):
        self.amigos.remove(old_amigo)
    
    def to_json(self):
        json_user = {
            "usuario": self.__usuario,
            "nombre" : self.__nombre,
            "email": self.__email
        }
        return json_user

    
    def __eq__(self, other) -> bool:
        return self.__usuario == other.__usuario 

Post1 = Post('post1','Este es el post 1',datetime(2019, 2, 28), 1)
Post2 = Post('post2','Este es el post 2',datetime(2020, 4, 15), 2)
Post3 = Post('post3','Este es el post 3',datetime(2021, 10, 13), 3)
Post4 = Post('post4','Este es el post 4',datetime(2020, 6, 7),4)
Post5 = Post('post1','Este es el post 5',datetime(2019, 2, 28), 5)
Post6 = Post('post2','Este es el post 6',datetime(2020, 4, 15), 6)
Post7 = Post('post3','Este es el post 7',datetime(2021, 10, 13), 7)
Post8 = Post('post4','Este es el post 8',datetime(2020, 6, 7),8)
Post9 = Post('post1','Este es el post 9',datetime(2019, 2, 28), 9)
Post10 = Post('post2','Este es el post 10',datetime(2020, 4, 15), 10)
Post11 = Post('post3','Este es el post 11',datetime(2021, 10, 13), 11)
Post12 = Post('post4','Este es el post 12',datetime(2020, 6, 7),12)
User1 = Usuario("David", "DavidLm", "Dalamartin28@gmail.com",['Pedroro','Javi34'], [Post1, Post3, Post2, Post4])
User2 = Usuario("Pedro", "Pedroro", "pedrorod@gmail.com",['DavidLm','Pablo5'],[Post11, Post7])
User3 = Usuario("Javi", "Javi34", "javier@gmail.com",['DaviLm'], [Post6, Post9, Post8])
User4 = Usuario("Pablo", "Pablo5", "pablo@gmail.com",['Pedroro','Javi34'],[Post12, Post5])
usuarios = [User1, User2, User3, User4]

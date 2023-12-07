class Usuario:
    def __init__(self, username, email, senha):
        self.username = username
        self.email = email
        self.senha = senha
        self.posts = []

    def criar_post(self, texto):
        novo_post = Post(texto, self)
        self.posts.append(novo_post)
        return novo_post

class Post:
    def __init__(self, texto, autor):
        self.texto = texto
        self.autor = autor
        self.comentarios = []

    def adicionar_comentario(self, comentario):
        self.comentarios.append(comentario)

class Comentario:
    def __init__(self, texto, autor):
        self.texto = texto
        self.autor = autor

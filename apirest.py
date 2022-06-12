from datetime import datetime
from flask import Flask, jsonify, request
import re
app = Flask(__name__)

from usuarios import  Usuario, Post, usuarios

def getid():
    posts = []
    for user in usuarios:      
        posts += [post for post in user.posts]
    return len(posts)+2


# Testing Route
@app.route("/ping", methods=["GET"])
def ping():
    return jsonify({"response": "pong!"})

# Get Data Routes
@app.route("/usuarios")
def getUsuarios():
    return jsonify({
            "usuarios": [usuario.to_json() for usuario in usuarios]
        })


@app.route("/usuarios/<string:usuario1>")
def getUsuario(usuario1):
    for user in usuarios:
        if user.usuario == usuario1:
            return user.to_json()
    return jsonify({"message": "Usuario no encontrado"})


@app.route("/usuarios/search")
def getFriends():
    users = []
    for user in usuarios:
        if  re.search(request.args.get('pattern',''), user.usuario):
            users += [user.to_json()]
    return jsonify({'usuarios': users})
    


# Create Data Routes
@app.route("/usuarios", methods=["POST"])
def addUsuario():
    new_usuarios = {
        "nombre": request.json["nombre"],
        "email": request.json["email"],
        "usuario": request.json["usuario"]
    }
    User = Usuario(request.json["nombre"],request.json["usuario"], request.json["email"])
    if User in usuarios:
        return jsonify({"message":"El usuario ya existe"})
    usuarios.append(User)
    return jsonify({
            "message": "Usuario actualizado",
            "usuarios": [usuario.to_json() for usuario in usuarios]
        })

# Update Data Route
@app.route("/usuarios/<string:username>", methods=["PUT"])
def editUsuario(username):
    for user in usuarios:
        if user.usuario == username:
            user.set_email(request.json["email"])
            user.set_nombre(request.json["nombre"])
            return jsonify({
                "message": "Usuario actualizado",
                "usuario modificado": user.to_json()
            })
    return jsonify({"message": "Usuario no encontrado"})

# DELETE Data Route
@app.route("/usuarios/<string:username>", methods=["DELETE"])
def deleteUsuario(username):
    for user in usuarios:
        if user.usuario == username:
            usuarios.remove(user)
            return jsonify({
                "message": "Usuario borrado",
                "usuarios": [usuario.to_json() for usuario in usuarios]
            })
    return jsonify({
            "message": "El usuario no ha sido encontrado."})


@app.route("/usuarios/<string:username>/posts", methods=["GET"])
def getPosts(username):
    for user in usuarios:
        if user.usuario == username:
            if len(user.posts) == 0:
                return jsonify({
            "message": "El usuario no tiene ningún post."})
            else: 
                posts = []
                for post in user.posts:
                        if (datetime.strptime(request.args.get('fecha_fin', '2100-01-01'), '%Y-%m-%d')>= post.creation_date >= datetime.strptime(request.args.get('fecha_inicio','2000-01-01'), '%Y-%m-%d')):
                            posts += [post.to_json()]
                return jsonify({"Posts": posts[int(request.args.get('post_inicio',0)):int(request.args.get('post_fin',len(posts)-1))]})
    return jsonify({
        "message": "El usuario no ha sido encontrado."})


@app.route("/posts", methods=["GET"])
def getallPosts():
    posts=[]
    for user in usuarios:
        for post in user.posts:
            if (datetime.strptime(request.args.get('fecha_fin', '2100-01-01'), '%Y-%m-%d')>= post.creation_date >= datetime.strptime(request.args.get('fecha_inicio','2000-01-01'), '%Y-%m-%d')):
                posts += [post.to_json()]
    return jsonify({"Posts": posts[int(request.args.get('post_inicio',0)):int(request.args.get('post_fin',len(posts)-1))]})


@app.route("/posts/contador", methods=["GET"])
def getPostscount():
    
    posts = []
    for user in usuarios:
        for post in user.posts:
            if (datetime.strptime(request.args.get('fecha_fin', '2100-01-01'), '%Y-%m-%d')>= post.creation_date >= datetime.strptime(request.args.get('fecha_inicio','2000-01-01'), '%Y-%m-%d')):
                posts += [post]
    return jsonify({"Posts": len(posts)})


@app.route ("/usuarios/<string:username>/posts", methods = ["POST"])
def newPost(username):
    for user in usuarios:
        if user.usuario == username:
            Post1 = Post(request.json["titulo"],request.json["texto"], datetime.now(), getid())
            user.add_post(Post1)
            posts = [post.to_json() for post in user.posts]
            return jsonify({
                    "message": "Post añadido",
                    "Posts": posts})
    return jsonify({
            "message": "El usuario no ha sido encontrado por lo que no se puede publicar el post."})
        
@app.route ("/usuarios/<string:username>/posts/<int:postid>", methods = ["DELETE"])
def deletePost(username, postid):
    for user in usuarios:
        if user.usuario == username:
            if len(user.posts) > 0:
                for post in user.posts: 
                    if post.id == postid:
                        user.remove_post(post)
                        return jsonify({
                                "message": "Post borrado"})
                else: 
                    return jsonify({
                "message": "El id no ha sido encontrado por lo que no se puede borrar el post."})
            else: return jsonify({
                "message": "El Usuario no tiene ningún post."})
    return jsonify({
            "message": "El usuario no ha sido encontrado por lo que no se puede borrar el post."})


@app.route ("/usuarios/<string:username>/posts/<int:postid>", methods = ["PUT"])
def updatePost(username, postid):
    for user in usuarios:
        if user.usuario == username:
            if len(user.posts) > 0:
                for post in user.posts: 
                    if post.id == postid:
                        post.set_date()
                        post.set_texto(request.json['texto'])
                        post.set_titulo(request.json['titulo'])
                        return jsonify({
                                "message": "Post actualizado",
                                "new Post": post.to_json()})
                else: 
                    return jsonify({
                "message": "El id no ha sido encontrado por lo que no se puede modificar el post."})
            else: return jsonify({
                "message": "El Usuario no tiene ningún post."})
    return jsonify({
            "message": "Tu usuario no ha sido encontrado por lo que no se puede modificar el post."})


@app.route('/usuarios/<string:username>/amigos', methods=['POST'])
def addFriend(username):
    for user in usuarios:
        if user.usuario == username:
            for user2 in usuarios:
                if request.json['usuario_amigo'] == user2.usuario:
                    user.add_amigo(request.json['usuario_amigo'])
                    return jsonify({'message':'Amigo añadido'})
            return jsonify({'message':"El usuario que buscas no está en la red social"})
    return jsonify({
            "message": "Tu usuario no ha sido encontrado por lo que no se puede añadir el amigo."})


@app.route('/usuarios/<string:username>/amigos/<amigo_username>', methods=['DELETE'])
def deleteFriend(username, amigo_username):
    for user in usuarios:
        if user.usuario == username:
            for amigo in user.amigos:
                if amigo_username == amigo:
                    user.remove_amigo(amigo_username)
                    return jsonify({'message':'Amigo eliminado'})
            return jsonify({'message':"El usuario que buscas no es amigo tuyo o no está en la red."})
    return jsonify({
            "message": "Tu usuario no ha sido encontrado por lo que no se puede añadir el amigo."})

@app.route("/usuarios/<string:username>/amigos", methods=["GET"])
def getAmigos(username):
    for user in usuarios:
        if user.usuario == username:
            if len(user.amigos) == 0:
                return jsonify({
            "message": "El usuario no tiene ningún amigo."})
            else: 
                amigos = []
                for amigo in user.amigos:
                    if re.search(request.args.get('pattern',''), amigo):
                        amigos += [amigo]
                return jsonify({'amigos':amigos[int(request.args.get('amigo_inicio',0)):int(request.args.get('amigo_fin',10000))]})
    return jsonify({
        "message": "El usuario no ha sido encontrado."})


@app.route('/usuarios/<string:username>/amigos/posts')
def getAmigosPosts(username):
    posts = []
    for user in usuarios:
        if user.usuario == username:
            for amigo in user.amigos:
                for user1 in usuarios:
                    if user1.usuario == amigo:
                        for post in user1.posts:
                            if re.search(request.args.get('pattern',''), amigo) and datetime.strptime(request.args.get('fecha_fin', '2100-01-01'), '%Y-%m-%d')>= post.creation_date >= datetime.strptime(request.args.get('fecha_inicio','2000-01-01'), '%Y-%m-%d'):
                                posts += [post.to_json()]
    return jsonify({'Posts':posts[int(request.args.get('post_inicio',0)):int(request.args.get('post_fin',10000))]})

                    


if __name__ == "__main__":
    app.run(debug=True, port=4000)
import requests as req


#Vemos todos los usuarios de la red
# print(req.get('http://127.0.0.1:4000/usuarios/').text)

'''Creamos un nuevo usurario'''
req.post('http://127.0.0.1:4000/usuarios',json={
	"username": "Diego5",
	"nombre" : "Diego",
	"email": "diego@gmail.com"
})
# print(req.get('http://127.0.0.1:4000/usuarios/').text)

'''Publicar un post nuevo (o varios)'''
req.post('http://127.0.0.1:4000/usuarios/Diego5/posts', json={
	"titulo": "primer post",
	"text0": "este es el primer post"
})
# print(req.get('http://127.0.0.1:4000/usuarios/Diego5/posts').text)

'''Obtener mis posts usando los filtros disponibles (en este caso, el cliente debe poder
optar por obtener la lista de identificadores de esos posts o bien directamente el
contenido de dichos posts)'''
req.get('http://127.0.0.1:4000/usuarios/Diego5/posts?fecha_inicio=2022-01-17&fecha_fin=2022-01-17')
# print(req.get('http://127.0.0.1:4000/usuarios/Diego5/posts?fecha_inicio=2020-01-18&fecha_fin=2022-01-18').text)


'''Modificar un post'''
req.put('http://127.0.0.1:4000/usuarios/Diego5/posts', json={
	"titulo": "mi primer post",
	"texto": "este es mi primer post modificado"
})
# print(req.get('http://127.0.0.1:4000/usuarios/Diego5/posts').text)

'''Borrar un post'''
req.delete('http://127.0.0.1:4000/usuarios/Diego5/posts/1')
# print(req.get('http://127.0.0.1:4000/usuarios/Diego5/posts/1').text)

'''Buscar posibles amigos entre los usuarios'''
req.get('http://127.0.0.1:4000/usuarios/DavidLm/amigos/search?pattern=P')
# print(req.get('http://127.0.0.1:4000/usuarios/DavidLm/amigos/search?pattern=P').text)

'''Agregar un amigo'''

req.post('http://127.0.0.1:4000/usuarios//Diego5/amigos', json={
	"usuario_amigo": "DavidLm"
})
# print(req.get('http://127.0.0.1:4000/usuarios/Diego5/amigos').text)

'''Eliminar a un amigo'''
req.delete('http://127.0.0.1:4000/usuarios/DavidLm/amigos/Pablo5')
# print(req.get('http://127.0.0.1:4000/usuarios/DavidLm/amigos/Pablo5').text)

'''Obtener la lista de amigos usando los filtros disponibles'''
# print(req.get('http://127.0.0.1:4000/usuarios/DavidLm/amigos/search?pattern=P&?amigo_inicio=1&?amigo_fin=3').text )#por patron

'''Consultar número de posts publicados por mí en un periodo'''
# print(req.get('http://127.0.0.1:4000/usuarios/DavidLm/posts/contador?fecha_inicio=2020-01-18&fecha_fin=2022-01-18').text)

'''Obtener la lista de usuarios'''
# print(req.get('http://127.0.0.1:4000/usuarios').text)

'''Modificar los datos de nuestro perfil'''
req.put('http://127.0.0.1:4000/usuarios/DavidLm', json={
	"nombre": "David",
	"email": "david@nuevo.com"
}) #cambiamos edad, telefono y nombre de usuario
# print(req.get('http://127.0.0.1:4000/usuarios/DavidLm'))



'''Darse de baja de la red social'''
req.delete('http://127.0.0.1:4000/usuarios/Diego5') #seria solo posible con un metodo de autenticacion (no implementado)
# print(req.get('http://127.0.0.1:4000/usuarios').text)

'''Obtener la lista de posts publicados por amigos que contienen un determinado texto o por fecha'''
print(req.get('http://127.0.0.1:4000/usuarios/DavidLm/posts?fecha_inicio=2020-8-7&?fecha_fin=2022-1-18&?post_inicio=0&?post_fin=3&?pattern=P').text)
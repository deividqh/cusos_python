print (4+5)
nombre = "Loreto"
print (nombre)
#comentario 1
"""
comentario 2
"""
mesa = False
mesa = [1,2,3,4]
print(type(mesa))
mesa = (1,2,3,4)
print(type(mesa))


"""
COLECCIONES
"""
# Create a sample collection
users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}
print(type(users))


# Strategy:  Iterate over a copy
for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]

# Strategy:  Create a new collection
active_users = {}
for user, status in users.items():
    if status == 'active':
        active_users[user] = status


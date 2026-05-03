print("CREAR Diccionarios")
empty_dict = {}

full_dict = {
'bifronte': 'De dos frentes o dos caras',
'anarcoide': 'Que tiende al desorden',
'montuvio': 'Campesino de la costa'
}
population_can = {
 2015: 2_135_209,
 2016: 2_154_924,
 2017: 2_177_048,
 2018: 2_206_901,
 2019: 2_220_270
 }

print("Convertir Diccionarios")

print(dict(['a1','b3']))    #list de cadena de texto
print(dict(('a1','b3')))    #tuple de cadenaTexto
dict([['a', 1], ['b', 2]])  #Lista de listas

# Si nos fijamos bien, cualquier iterable que tenga una estructura interna de 2 elementos
# es susceptible de convertirse en un diccionario a través de la función dict().
print(""" Operaciones con diccionarios """)

print('Operaciones con Diccionarios 1\n'+'-'*40)
rae = {'bifronte': 'De dos frentes o dos caras',
        'anarcoide': 'Que tiende al desorden',
        'montuvio': 'Campesino de la costa'
        }
# ---------------------------------------------------
# GET
print(rae.get('bifronte'))
print(rae.get('programación'))

print('Operaciones con Diccionarios 2\n'+'-'*40)
# --------------------------------------------------
VOWELS = 'aeiou'
enum_vowels = {}
for i, vowel in enumerate(VOWELS):
    enum_vowels[vowel] = i + 1

print(enum_vowels)
# ---------------------------------------------------
print('Validacion de clave: Operaciones con Diccionarios 3\n'+'-'*20)
print('bifronte' in rae)

print('Operaciones con Diccionarios 4\n'+'-'*40)
print("Keys: ",rae.keys())            #tupla de listas==> dict_keys(['bifronte', 'anarcoide', 'montuvio'])
print('Values: ',rae.values())        #tupla de listas==> dict_values(['bifronte', 'anarcoide', 'montuvio'])
print('items: ',rae.items())          #tupla de listas==> dict_items(['bifronte', 'anarcoide', 'montuvio'])


print('Operaciones con Diccionarios \n'+'-'*40)
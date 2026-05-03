import os
# _____________________
def sumar(a,b):
    isA= isinstance(a, (int, float))
    isB= isinstance(b, (int, float))

    isA = not isinstance(a, (int, float))
    isB = not isinstance(b, (int, float))
    
    # _____________
    if  isA or isB:
        print(f'{isA} OR {isB} = {isA or isB} ')    
    # _____________
    if  not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        print(f'{isA} OR {isB} = {isA or isB} ')        
    # _____________
    if  isA and isB:
        print(f'{isA} AND {isB} = {isA and isB}')
    # _____________
    if  not isinstance(a, (int, float)) and not isinstance(b, (int, float)):
        print(f'{isA} AND {isB} = {isA and isB} ')        

    # _____________
    print(f'{isA} OR {isB} = {isA or isB}')
    print(f'{isA} AND {isB} = {isA and isB}')
    
    print(False or True)
    print(False or False)
    print(True or False)
    print(True or True)

    # return a+b
# _________________________
os.system('cls')
try:
    resultado=sumar(8,8)
    
    print('\n------ cambio ---------')

    resultado=sumar("Hola",8)
except TypeError as e:
    print(f"error {e}")
"""
generic script

a = @
e = 3
i = ¡
o = 0
u = v

text: "fooziman" output => "F00z¡m@N" 
text: "barziman" output => "B@rz¡m@N" 
text: "3q" output => "3Q" 
text: "qu" output => "Qv" 
text: "qux" output => "QvX" 
"""


def fn_hack_3(palabra):

    diccionario = {
    "a": "@",
    "e": "3",
    "i": "¡",
    "o": "0",
    "u": "v"
    }

    tamano = len(palabra)
    result = ''
    vocal = 0   # indicador para saber si la v es un remplazo de la u o si es una v naturalmente
    i=1
    for x in palabra:
        if x in ("a", "e", "i", "o" , "u"):
            x = diccionario[x]
            vocal = 1
        
        if i == 1 or i == tamano and vocal == 0: # aqui aplicamos upper si es principio o final y si no es una vocal
            result = result + x.upper()
        else:
            result = result + x

        i += 1
        vocal = 0


    return result

print(fn_hack_3("fooziman"))
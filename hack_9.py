"""
text: {"foo":"fookziman","bar":"barziman"} output => {"Foo":"Fooziman"}
"""


def fn_hack_9(dicc):
    dicc1 = {} #esste va a ser el return
    for x in dicc:
        if x == 'foo':   #itero el diccionario en busca de la clave foo
            i = dicc[x]      #guardo el value correspondiente a esa clave en  i
            x = x.capitalize()
            i = i.capitalize()
            y = ''      # variable para obtener la palabra fooziman 
            for z in i:    #itero el value del diccionario de entrada y cuando sea k no lo tomo, el resto si
                if z != 'k':
                    y = y + z    #formo la palabra fooziman
            dicc1 = {               #armo el diccionario con su clave y valor
                x : y
            }
    return dicc1

print(fn_hack_9({"foo":"fookziman","bar":"barziman"}))
"""
generic script

text: "fooziman" output => "fOozIman" 
text: "qux" output => "qUx" 
text: "eq" output => "eq" 
"""


def fn_hack_1(palabra):

    result = ''
    i=0
    for x in palabra:
        if i == 1:
            if x in ('a', 'e', 'i' , 'o', 'u'): #aplica upper solo cuando es vocal
                x = x.upper()

            i = -2                    #aplica -2 reinicio el contador de letra, ya que cada 3er digito es mayuscula excepto la primera vez
        result = result  + x
        i += 1  

    return result

print(fn_hack_1('fooziman'))
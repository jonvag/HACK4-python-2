"""
generic script

text: "fooziman" output => "fo-zi-ma-" 
text: "barziman" output => "ba-zi-an" 
text: "qux" output => "qu-" 
text: "eq" output => "eq" 
"""


def fn_hack_5(palabra):

    count = 0
    vocales = 0
    result = ""
    for x in palabra:
        if count == 2:  # esta variable indica cuando debe ir guion
            if vocales == 1: 
                result = result + "-"
                result = result + x
                vocales = 0
                count = 0   #count aqui le pongo cero porque se reinicia el contador pero no a -1 porque ya le puse la letra que le sigue o sea ya paso una vez
            else:
                if x in ("a", "e", "i", "o", "u"):
                    vocales = 1
                result = result + "-"
            if count != 0:
                count = -1
        else:
            result = result + x
        count += 1
    return result

print(fn_hack_5("barziman"))
"""
generic script

text: "fooziman" output => "oozima" 
text: "barziman" output => "arzima" 
text: "qux" output => "qux" 
"""


def fn_hack_4(palabra):
    
    tamano = len(palabra)
    result = ''
    i=1
    
    if tamano > 3:
        for x in palabra:
            if i == 1 or i == tamano:
                result = result
            else:
                result = result + x
            i += 1
    else:
        result = palabra

    return result

print(fn_hack_4('qux'))
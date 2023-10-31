"""
generic script

text: "fooziman" output => "fzmn" 
text: "barziman" output => "brzmn" 
text: "qux" output => "qx" 
"""


def fn_hack_2(palabra):
    result = ''
    for x in palabra:
        if x not in ('a', 'e', 'i', 'o', 'u' , 'A', 'E', 'I', 'O', 'U'):
            result = result + x
    
    return result

print(fn_hack_2('qux'))
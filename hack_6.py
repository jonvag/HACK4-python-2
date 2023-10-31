"""
generic script

["1","-"] => type string
["0"] => type string

text: ["a","b","c","d","e"] output => ["1","-","3","-","5"]
text: [] output => ["0"] 
"""


def fn_hack_6(lista):
    result = []
    count = 0
    indicador = 0
    if len(lista) > 0:
        for x in lista:
            count += 1 
            indicador += 1
            if indicador == 2:
                result.append('-')
                indicador = 0
            else:
                result.append(str(count))
            #print(lista[::2])
    else:
        result = ["0"]
    return result

print(fn_hack_6(["a","b","c","d","e"]))
print(fn_hack_6([]))
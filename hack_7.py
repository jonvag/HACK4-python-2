"""
generic script

["1",2] => type string & type int
[0] => type int

text: ["a","b","c","d","e"] output => ["1",2,"3",4,"5"]
text: [] output => [0] 
"""


def fn_hack_7(lista):
    result = []
    count = 0
    indicador = 0
    if len(lista) > 1:
        for x in lista:
            count += 1 
            indicador += 1
            if indicador == 2:
                result.append(count)
                indicador = 0
            else:
                result.append(str(count))
            #print(lista[::2])
    else:
        result = [0]
    return result

print(fn_hack_7(["a","b","c","d","e"]))
print(fn_hack_7([]))
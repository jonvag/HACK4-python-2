"""
generic script

text: ["a","b","c","d","e"] output => ["e-5","d-4","c-3","b-2","a-1"]
text: ["a","b","c"] output => ["c-3","b-2","a-1"]
text: ["a","b","c","d"] output => ["4","3","2","1"]
text: ["a","b"] output => ["2","1"]
"""


def fn_hack_8(lista):
    count = len(lista)
    result = []
    word = ''
    if count % 2 == 0:
        for x in reversed(lista):
            word = str(count)
            result.append(word)
            count -= 1
    else:
        for x in reversed(lista):
            word = x + '-' + str(count)
            result.append(word)
            count -= 1
    
    return result
print('HACK8')
print("prueba 1: ", fn_hack_8(["a","b","c","d","e"]))
print("prueba 2: ", fn_hack_8(["a","b","c"]))
print("prueba 3: ", fn_hack_8(["a","b","c","d"]))
print("prueba 4: ", fn_hack_8(["a","b"]))
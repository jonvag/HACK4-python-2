"""
text: [{"a":"b"},{"c","d"},{"e":"f"}] output => [{"1":"2"},{"3","4"},{"5":"6"}]
"""


def fn_hack_10(entrada):

    abc = [' ', 'a', 'b', 'c','d', 'e', 'f','g', 'h', 'i','j', 'k', 'l','m', 'n', 'o','p', 'q', 'r','s', 't', 'u','v', 'w', 'x','y', 'z']
    clave = 0
    valor = 0
    elemento2 = {}
    i = 0
    result = []
    
    for x in entrada: #itero la variable de entrada
        if i % 2 == 0: #aqui verifico cual logica le voy a aplicar ya que una es como diccionario y otro como lista
            for numero in x: #tomo el elemento como diccionario
                indice = 0  #esta variable me va a dar el numero que corresponde a la letra
                for letra in abc:
                    if letra == numero:
                        clave = indice

                    elif letra == x[numero]:
                        valor = indice

                    indice += 1
                #se crea aqui el elemento del diccionario
                
                elemento = {
                    str(clave) : str(valor)
                }
                result.append(elemento)
                print(elemento) #valor
        else:
            indicador = 0
            var1 = 0
            var2 = 0
            for numero in x:
                indice = 0  #esta variable me va a dar el numero que corresponde a la letra
                for letra in abc:
                    if letra == numero:
                        if indicador == 0:
                            var2 = str(indice)
                            indicador = 1
                        else:
                            var1 = str(indice)

                        
                    indice += 1
                #se crea aqui el elemento de la lista
            elemento2= { var1, var2}
            print(elemento2)
            result.append(elemento2)

        i += 1
    return result

print(fn_hack_10([{"a":"b"},{"c","d"},{"e":"f"}]))
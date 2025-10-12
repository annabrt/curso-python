# convesão de tipos, coerção, type convertion, typecasting, coercion 
# é o ato de converter um tipo em outro
# tipos imutáveis e primitivos:
# str, int, float, bool
print(1 + 1) # dois numeros que pertencem ao mesmo tipo somados sem problema
print('a' + 'b') # misturou dois tipos diferentes, a string e o sinal matematico, que é chamado de polimorfismo quando junta assim
                # pelo python ser uma linguagem dinamica, ele consegue fazer essa soma mesmo havendo essa diferença
                # mas se quiser somar dois tipos mesmo sem ser só o sinal ele não consegue por ser de tipagem forte, por isso precisa fazer a converção

print(int('1'), type(int('1')))
print(int('1') + 1)
print(float('1') + 1)
print(type(float('1') + 1))
print(bool(' '))
print(str(11) + 'b')
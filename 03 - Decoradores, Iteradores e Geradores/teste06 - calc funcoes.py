

def calcular(operacao): # soma a + b
    def somar(a, b):
        return a + b 
    
    def somar_mult(a, b, c):  # mult, c=> 3*5 <=b = 15, e soma a=> + 2 = 17 .
       return a + b * c

    def subtrair(a, b):
        return a - b
    
    def multiplicar(a, b):
        return a * b
    
    
    
    if operacao == "+":
        return somar
    
    if operacao == "+ *":   # Aqui operacao de mult e soma.
        return somar_mult
    
    if operacao == "*":
        return multiplicar

    if operacao == "-":
        return subtrair
    
   


resultado = calcular("+")(5, 3) 
print(resultado)

resultado = calcular("+ *")(2, 5, 3) # 5 * 3 = 15 + 2 = 17 .
print(resultado)

resultado = calcular("-")(8, 2)
print(resultado)
resultado = calcular("*")(3, 3)
print(resultado)


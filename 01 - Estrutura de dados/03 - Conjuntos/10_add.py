
# Metodos da classe "set" ===>> {add}
# Utilizado para adcionar elemeto/s a minha classe "set" 

sorteio = {1, 23} # Conjuto "set" original. 
print(sorteio)
# >>> {1, 23}

sorteio.add(25) # Aqui adcionamos 25 ao Conjuto "set" original.
print(sorteio)
# >>>  {1, 23, 25}

sorteio.add(42) # Aqui adcionamos 42 ao Conjuto "set" .
print(sorteio)
# >>> {1, 23, 25, 42}


sorteio.add(25) # Aqui tentamos adicionar 25 ao Conjuto "set" . 
                # como ja existe ele e ignorado.
print(sorteio)
 # >>>  {1, 23, 25, 42}

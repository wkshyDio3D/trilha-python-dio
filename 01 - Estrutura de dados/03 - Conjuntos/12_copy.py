
# Metodos da classe "set" ===>> {copy}
# Vai pegar o "set" original e vai gerar uma copia . porem com instacia diferente. 
# Ou seja o que for auterado em um nao vai refletir no outro.

sorteio = {1, 23}
print(sorteio) 
 # >>> {1, 23}

sorteio.copy()
print(sorteio) 
 # >>> {1, 23}

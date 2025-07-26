def duplicar(func):
    def envelope(*args, **kwargs):
        print("faz algo antes de executar")
        resultado = func(*args, **kwargs)
        print("faz algo depois de executar")
        return resultado

    return envelope


@duplicar
def aprender(tecnologia):
    print(f"Olá mundo {tecnologia}!")
    return tecnologia.upper()


tecnologia = aprender("Estou Aprendendo python")
print(tecnologia)




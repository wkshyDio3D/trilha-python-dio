
Introducao de Boas praticas de seguranca ao usar APi de Banco de dados.

Ao escrever cunsultas SQL em Python, e importante seguir boas praticas para garantir a seguranca e a eficiencia do seu codigo e para evitar vazamentos de dados.

 Evitar a concatenacao de strings nas consultas  e usar consultas parametrizadas. isso melhora a legibilidade do codigo e ajuda a prevenir ataques de injecao SQL.

Exemplos:
# Modo errado:
id = 1
cursor.execute('SELECT * FROM minha_tabela WHERE id = ' + str(id))

# Modo correto:
id = 1
cursor.execute('SELECT * FROM minha_tabela WHERE id = ?', (id,))
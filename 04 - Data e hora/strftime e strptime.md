
https://docs.python.org/pt-br/3.10/library/datetime.html

https://en.wikipedia.org/wiki/List_of_tz_database_time_zones

https://time.is/pt_br/UTC 



Em Python, strftime e strptime são métodos utilizados para lidar com datas e horas, mas com funções opostas. strftime formata um objeto de data e hora (como datetime.datetime) numa string, enquanto strptime analisa uma string e a converte para um objeto de data e hora. 
strftime (String Format Time):
Função: Formata um objeto de data e hora em uma string.
Uso: Quando você tem um objeto datetime e quer apresentar a data e hora num formato específico, como por exemplo, "dd/mm/yyyy" ou "dd/mm/yyyy hh:mm:ss".
Parâmetros: Recebe um objeto de data e hora e uma string de formato com diretivas de formato (por exemplo, %Y para o ano com 4 dígitos, %m para o mês com dois dígitos, %d para o dia com dois dígitos, %H para as horas com dois dígitos, etc).
Exemplo:
Python

    import datetime

    data_atual = datetime.datetime.now()
    data_formatada = data_atual.strftime("%d/%m/%Y %H:%M:%S")
    print(data_formatada)  # Exemplo: 09/06/2025 12:34:56
strptime (String Parse Time):
Função: Analisa uma string e a converte para um objeto de data e hora.
Uso: Quando você tem uma string que representa uma data e hora e quer convertê-la para um objeto datetime para poder trabalhar com ela.
Parâmetros: Recebe uma string que representa a data e hora e uma string de formato que especifica como a string é estruturada.
Exemplo:
Python

    import datetime

    string_data = "09/06/2025 12:34:56"
    formato = "%d/%m/%Y %H:%M:%S"
    data_objeto = datetime.datetime.strptime(string_data, formato)
    print(data_objeto)  # Exemplo: 2025-06-09 12:34:56
Em resumo: strftime converte data e hora para string e strptime converte string para data e hora. 
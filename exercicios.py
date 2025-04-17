### Exercício 1: Verificação de Qualidade de Dados
# Você está analisando um conjunto de dados de vendas e precisa garantir 
# que todos os registros tenham valores positivos para `quantidade` e `preço`. 
# Escreva um programa que verifique esses campos e imprima "Dados válidos" se ambos 
# forem positivos ou "Dados inválidos" caso contrário.

# quantidade = 60
# preco = - 20

# if quantidade > 0 and preco > 0:
#     print("Dados Validos")
# elif quantidade < 0:
#     print(f'Dados invalidados: Quantidade com valor negativo: {quantidade}')
# elif preco < 0:
#     print(f'Dados invalidados: preco com valor negativo: {preco}')
# else:
#     print(f'Dados invalidados para quantidade preco')    


### Exercício 2: Classificação de Dados de Sensor
# Imagine que você está trabalhando com dados de sensores IoT. 
# Os dados incluem medições de temperatura. Você precisa classificar cada leitura 
# como 'Baixa', 'Normal' ou 'Alta'. Considerando que:

### Exercício 3: Filtragem de Logs por Severidade
# Você está analisando logs de uma aplicação e precisa filtrar mensagens 
# com severidade 'ERROR'. Dado um registro de log em formato de dicionário 
# como `log = {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Falha na conexão'}`, 
# escreva um programa que imprima a mensagem se a severidade for 'ERROR'.

history_log = [
    {'timestamp': '2021-06-23 10:00:00', 'level': 'INFO', 'message': 'Conexão bem-sucedida'},
    {'timestamp': '2021-06-23 10:01:00', 'level': 'ERROR', 'message': 'Falha na conexão'},
    {'timestamp': '2021-06-23 10:02:00', 'level': 'WARNING', 'message': 'Latência alta'},
    {'timestamp': '2021-06-23 10:03:00', 'level': 'ERROR', 'message': 'Timeout na requisição'}
]

for log in history_log:
    if log['level'] == 'ERROR':
        print(log['message'])

### Exercício 4: Validação de Dados de Entrada
# Antes de processar os dados de usuários em um sistema de recomendação, 
# você precisa garantir que cada usuário tenha idade entre 18 e 65 anos e tenha 
# fornecido um email válido. Escreva um programa que valide essas condições 
# e imprima "Dados de usuário válidos" ou o erro específico encontrado.

### Exercício 5: Detecção de Anomalias em Dados de Transações
# Você está trabalhando em um sistema de detecção de fraude e precisa identificar 
# transações suspeitas. Uma transação é considerada suspeita se o valor for superior 
# a R$ 10.000 ou se ocorrer fora do horário comercial (antes das 9h ou depois das 18h). 
# Dada uma transação como `transacao = {'valor': 12000, 'hora': 20}`, verifique se ela é suspeita.

### Exercício 6. Contagem de Palavras em Textos
# Objetivo:** Dado um texto, contar quantas vezes cada palavra única aparece nele.

# texto = "Hoje e nossa segunda aula do bootcamp , bootcamp de python"

# palavras = texto.split(" ")

# print(palavras)

# contagem_de_palavras = {}

# for palavra in palavras:
#     if palavra in contagem_de_palavras:
#         contagem_de_palavras[palavra] = + 1
#     else:
#         contagem_de_palavras[palavra] = 1 

# print(contagem_de_palavras)


### Exercício 7. Normalização de Dados
# Objetivo:** Normalizar uma lista de números para que fiquem na escala de 0 a 1.

### Exercício 8. Filtragem de Dados Faltantes
# Objetivo:** Dada uma lista de dicionários representando dados de usuários, filtrar aqueles que têm um campo específico faltando

### Exercício 9. Extração de Subconjuntos de Dados
# Objetivo:** Dada uma lista de números, extrair apenas aqueles que são pares.

### Exercício 10. Agregação de Dados por Categoria
# Objetivo:** Dado um conjunto de registros de vendas, calcular o total de vendas por categoria.

### Exercícios com WHILE

### Exercício 11. Leitura de Dados até Flag
# Ler dados de entrada até que uma palavra-chave específica ("sair") seja fornecida.

### Exercício 12. Validação de Entrada
# Solicitar ao usuário um número dentro de um intervalo específico até que a entrada seja válida.

### Exercício 13. Consumo de API Simulado
# Simular o consumo de uma API paginada, onde cada "página" de dados é processada em loop até que não haja mais páginas.

### Exercício 14. Tentativas de Conexão
# Simular tentativas de reconexão a um serviço com um limite máximo de tentativas.

### Exercício 15. Processamento de Dados com Condição de Parada
# Processar itens de uma lista até encontrar um valor específico que indica a parada.
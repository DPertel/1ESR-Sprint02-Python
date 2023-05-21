# Função de mensagem de umidade do ar
def transmitir_mensagem_umidade(umidade):
    if umidade > 80:
        return "A umidade está alta. Certifique-se de se manter hidratado."
    elif umidade >= 50 and umidade <= 80:
        return "A umidade está em um nível ideal, segundo a OMS. Aproveite o dia!"
    elif umidade >= 20 and umidade < 50:
        return "A umidade está em um nível de atenção, segundo a OMS."
    else:
        return "A umidade está baixa. É um nível compatível com o do Deserto do Saara, por exemplo. Tenha cuidado com o ressecamento da pele."
    
# Função de mensagem de qualidade do ar
def transmitir_mensagem_monoxido(monoxido):
    if monoxido >= 50:
        return "Há níveis perigosos de monóxido de carbono no ar. Evite a exposição prolongada."
    elif monoxido >= 30 and monoxido < 50:
        return "Há uma quantidade moderada de monóxido de carbono no ar. Mantenha-se atento."
    else:
        return "A quantidade de monóxido de carbono está dentro dos níveis seguros."

# Função de mensagem de volume
def transmitir_mensagem_volume(volume):
    if volume >= 85:
        return "O volume está muito alto. Proteja seus ouvidos utilizando protetores auriculares."
    elif volume >= 60 and volume < 85:
        return "O volume está em um nível moderado. Aprecie a música!"
    else:
        return "O volume está dentro dos limites seguros."

# Função de verificação de número
def verifica_num(frase):
    num1 = input(frase)
    while not num1.isnumeric():
        num1 = input(frase)
    num1 = int(num1)
    return num1


def verificar_acesso():
    opcao = input("Deseja criar um cadastro ou acessar o serviço? (cadastro/serviço): ")
    while opcao not in ["cadastro", "serviço"]:
        opcao = input("Opção inválida. Deseja criar um cadastro ou acessar o serviço? (cadastro/serviço): ")
    
    if opcao == "cadastro":
        nome = input("Digite seu nome: ")
        ano_nascimento = verifica_num("Digite seu ano de nascimento: ")
        email = input("Digite seu e-mail: ")
        cidade = input("Digite sua cidade: ")
        return nome, ano_nascimento, email, cidade
    elif opcao == "serviço":
       return    
    else:
        print("Opção inválida.")

dados_cadastro = verificar_acesso()

# Verificação se os dados do cadastro foram retornados
if dados_cadastro:
    nome, ano_nascimento, email, cidade = dados_cadastro

bool = True

print("="*100)
print("Bem-vindo a LifeSustent. Monitoramento Ambiental em tempo real.\nAqui vamos verificar qualidade da umidade, do ar e da sonoridade em cidades inteligentes.")
print("="*100)

while bool:
    # Solicitar condições ao usuário
    print("")
    umidade = verifica_num("Digite a umidade do ar (em %): ")
    monoxido = verifica_num("Digite o nível de monóxido de carbono (em ppm): ")
    volume = verifica_num("Digite o volume em decibéis: ")

    # Transmitir mensagens de acordo com as condições
    mensagem_umidade = transmitir_mensagem_umidade(umidade)
    mensagem_monoxido = transmitir_mensagem_monoxido(monoxido)
    mensagem_volume = transmitir_mensagem_volume(volume)

    # Exibir mensagens para o usuário
    print("")
    print("="*100)
    print("De acordo com os dados de nosso banco de dados, com apoio das informações divulgadas da OMS e OSHA:")
    print(mensagem_umidade)
    print(mensagem_monoxido)
    print(mensagem_volume)
    print("="*100)

    # Perguntar se deseja continuar realizando outras análises
    sair = input("\nVocê deseja realizar outra analise (s/n)? ")
    while not sair in ["s", "n"]:
        sair = input("\nVocê deseja realizar outra analise (s/n)? ")

    if sair == "s":
        bool = True
    else:
        print(f'\nSr(a) {nome} obrigado por utilizar nosso serviço!\nVocê saiu.')
        bool = False
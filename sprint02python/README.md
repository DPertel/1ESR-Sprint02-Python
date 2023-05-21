SPRINT 02 - PYTHON
- Deivison Pertel – RM 550803
- Eduardo Akira Murata – RM 98713
- Guilherme Jacob Soares da Costa – RM 84581
- Fabrizio El Ajouri Romano – RM 550410
- Wesley Souza de Oliveira – RM 97874

--- 

# LifeSustent - Monitoramento Ambiental
Este código implementa um programa de monitoramento ambiental em tempo real chamado LifeSustent. O programa permite ao usuário verificar a qualidade da umidade do ar, o nível de monóxido de carbono e o volume sonoro em uma determinada cidade.

---

## Funções
### Função transmitir_mensagem_umidade(umidade)
Esta função recebe um valor de umidade como entrada e retorna uma mensagem relacionada à umidade do ar.

Se a umidade for maior que 80, a função retorna: "A umidade está alta. Certifique-se de se manter hidratado."
Se a umidade estiver entre 50 e 80 (inclusive), a função retorna: "A umidade está em um nível ideal, segundo a OMS. Aproveite o dia!"
Se a umidade estiver entre 20 e 50 (exclusive), a função retorna: "A umidade está em um nível de atenção, segundo a OMS."
Caso contrário, se a umidade for menor que 20, a função retorna: "A umidade está baixa. É um nível compatível com o do Deserto do Saara, por exemplo. Tenha cuidado com o ressecamento da pele."

---

### Função transmitir_mensagem_monoxido(monoxido)
Esta função recebe um valor de monóxido de carbono como entrada e retorna uma mensagem relacionada à qualidade do ar.

Se o valor de monóxido de carbono for maior ou igual a 50, a função retorna: "Há níveis perigosos de monóxido de carbono no ar. Evite a exposição prolongada."
Se o valor de monóxido de carbono estiver entre 30 e 50 (exclusive), a função retorna: "Há uma quantidade moderada de monóxido de carbono no ar. Mantenha-se atento."
Caso contrário, se o valor de monóxido de carbono for menor que 30, a função retorna: "A quantidade de monóxido de carbono está dentro dos níveis seguros."

---

### Função transmitir_mensagem_volume(volume)
Esta função recebe um valor de volume sonoro como entrada e retorna uma mensagem relacionada ao volume.

Se o volume for maior ou igual a 85, a função retorna: "O volume está muito alto. Proteja seus ouvidos utilizando protetores auriculares."
Se o volume estiver entre 60 e 85 (exclusive), a função retorna: "O volume está em um nível moderado. Aprecie a música!"
Caso contrário, se o volume for menor que 60, a função retorna: "O volume está dentro dos limites seguros."

---

### Função verifica_num(frase)
Esta função recebe uma frase como entrada e solicita ao usuário que digite um número. Ela verifica se o valor inserido é um número válido e retorna o número inteiro. Caso o valor inserido não seja um número válido, a função solicita novamente a entrada do usuário até que um número seja fornecido.

---

### Função verificar_acesso()
Esta função solicita ao usuário se deseja criar um cadastro ou acessar o serviço. O usuário pode escolher entre as opções "cadastro" ou "serviço". A função valida a entrada do usuário e, se a opção escolhida for "cadastro", solicita o nome, ano de nascimento, e-mail e cidade do usuário. Em seguida, retorna esses dados como uma tupla (nome, ano_nascimento, email, cidade). Se a opção escolhida for "serviço", a função retorna None.

---

## Fluxo do programa
O programa inicia solicitando ao usuário que escolha entre criar um cadastro ou acessar o serviço. Se a opção escolhida for "cadastro", são solicitados os dados do usuário (nome, ano de nascimento, e-mail e cidade). Caso contrário, o programa prossegue sem solicitar esses dados.

Em seguida, o programa exibe uma mensagem de boas-vindas e explica o propósito do serviço. Após isso, inicia-se um loop no qual o usuário pode realizar análises do ambiente.

Dentro do loop, são solicitadas as condições ambientais (umidade do ar, nível de monóxido de carbono e volume sonoro) por meio da função verifica_num(). Em seguida, são transmitidas mensagens relacionadas a essas condições usando as funções transmitir_mensagem_umidade(), transmitir_mensagem_monoxido() e transmitir_mensagem_volume(). As mensagens são exibidas na tela.

Depois disso, o programa pergunta ao usuário se ele deseja realizar outra análise. Se a resposta for "s", o loop continua e uma nova análise pode ser feita. Se a resposta for "n", o loop é interrompido e uma mensagem de saída é exibida, mencionando o nome do usuário (caso tenha feito cadastro) e agradecendo-o por usar o serviço.

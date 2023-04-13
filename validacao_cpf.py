import tkinter as tk

def validar_cpf():
    cpf9 = entrada_cpf.get().replace(".", "").replace("-", "")

    if not cpf9.isdigit() or len(cpf9) not in [9, 11]:
        saida_cpf.set("CPF inválido")
    else:
        if len(cpf9) == 9: #verifica se foi digitado 9 numero
            soma = sum([int(cpf9[i]) * peso for i, peso in enumerate(range(10, 1, -1))])
            """
            sum([int(cpf9[i]) * peso for i, peso in enumerate(range(10, 1, -1))]) -- 
            
           . A sintaxe de list comprehension ([expressão for item in lista])
            é usada para iterar sobre os elementos do CPF e calcular o valor da soma de cada produto de dígito e peso.
            A expressão dentro da list comprehension é int(cpf9[i]) * peso,
            que multiplica o valor do dígito convertido em inteiro (int(cpf9[i])) pelo peso correspondente (peso). 
            A variável i é o índice do dígito no CPF e é obtida pela função enumerate(), e a variável peso é o valor do peso correspondente,
             que é obtido pela função range().
             Dessa forma, a multiplicação ocorre dentro do loop for, 
             e as variáveis i e peso são declaradas e atribuídas a cada iteração do loop, de acordo com a lógica de iteração da função enumerate().
            """
            resto = soma % 11
            dv1 = 0 if resto < 2 else 11 - resto# foi utilizado um if ternário, onde dv1 é igual a 0 caso o resto seja menor que 2.

            cpf10 = cpf9 + str(dv1)# foi atribuido a variavel cpf10 o valor da variavel cpf9 concatenado com o dv1.
            soma = sum([int(cpf10[i]) * peso for i, peso in enumerate(range(11, 1, -1))])
            resto = soma % 11
            dv2 = 0 if resto < 2 else 11 - resto

            saida_cpf.set(f"Os dois últimos dígitos do CPF são: {dv1}{dv2}")
        else: #SE O USUARIO DIGITOU 11 DIGITOS ENTÃO DEVERÁ SER EXECUTADO O BLOCO DE COMANDOS ABAIXO...
            soma = sum([int(cpf9[i]) * peso for i, peso in enumerate(range(10, 1, -1))])#POR MAIS QUE TENHAM 11 DIGITOS AQUI, O CÓDIGO SÓ IRÁ PEGAR OS 9 PRIMEIROS.
            resto = soma % 11
            dv1 = 0 if resto < 2 else 11 - resto

            soma = sum([int(cpf9[i]) * peso for i, peso in enumerate(range(11, 1, -1))])
            resto = soma % 11
            dv2 = 0 if resto < 2 else 11 - resto
            dois_dgt = str(dv1) + str(dv2)#CONCATENA O DV1 COM O DV2
            if int(''.join([cpf9[-2], cpf9[-1]])) == int(dois_dgt):#VERIFICA SE OS DOIS ULTIMOS DIGITOS SÃO IGUAIS A CONCATENAÇÃO DO DV1 COM O DV2.
                saida_cpf.set("CPF válido")
            else:
                saida_cpf.set("CPF inválido")

# Cria a janela
janela = tk.Tk()
janela.title("Validação de CPF")

# Inicializa a variável que guarda a saída do programa
saida_cpf = tk.StringVar()

# Cria os widgets da janela
label_cpf = tk.Label(janela, text="Digite o CPF:")
entrada_cpf = tk.Entry(janela)
botao_validar = tk.Button(janela, text="Validar", command=validar_cpf)
label_saida = tk.Label(janela, textvariable=saida_cpf)

# Posiciona os widgets na janela
label_cpf.pack()
entrada_cpf.pack()
botao_validar.pack()
label_saida.pack()

# Inicia o loop de eventos da janela
janela.mainloop()
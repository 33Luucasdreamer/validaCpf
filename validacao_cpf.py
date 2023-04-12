import tkinter as tk

def validar_cpf():
    cpf9 = entrada_cpf.get().replace(".", "").replace("-", "")

    if not cpf9.isdigit() or len(cpf9) not in [9, 11]:
        saida_cpf.set("CPF inválido")
    else:
        if len(cpf9) == 9:
            soma = sum([int(cpf9[i]) * peso for i, peso in enumerate(range(10, 1, -1))])
            resto = soma % 11
            dv1 = 0 if resto < 2 else 11 - resto

            cpf10 = cpf9 + str(dv1)
            soma = sum([int(cpf10[i]) * peso for i, peso in enumerate(range(11, 1, -1))])
            resto = soma % 11
            dv2 = 0 if resto < 2 else 11 - resto

            saida_cpf.set(f"Os dois últimos dígitos do CPF são: {dv1}{dv2}")
        else:
            soma = sum([int(cpf9[i]) * peso for i, peso in enumerate(range(10, 1, -1))])
            resto = soma % 11
            dv1 = 0 if resto < 2 else 11 - resto

            soma = sum([int(cpf9[i]) * peso for i, peso in enumerate(range(11, 1, -1))])
            resto = soma % 11
            dv2 = 0 if resto < 2 else 11 - resto
            dois_dgt = str(dv1) + str(dv2)
            if int(''.join([cpf9[-2], cpf9[-1]])) == int(dois_dgt):
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
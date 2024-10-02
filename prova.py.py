import tkinter as tk  # Importa o módulo tkinter

# Função para converter centímetros para metros


def converter():
    cm = entry_cm.get()  # Obtém o valor em centímetros do campo de entrada
    if cm.isnumeric():  # Verifica se o valor inserido é numérico
        cm = float(cm)  # Converte para float
        metros = cm / 100  # Converte para metros
        # Atualiza o rótulo com o resultado
        label_resultado.config(text=f"{cm} cm é igual a {metros} m")
    else:
        label_resultado.config(
            text="Por favor, insira um número válido.")  # Mensagem de erro


# Criação da janela principal
janela = tk.Tk()  # Cria uma nova instância da janela
janela.title("Conversor de Centímetros para Metros")  # Título da janela
janela.geometry("400x200")  # Tamanho da janela

# Rótulo de instrução
label_instrucoes = tk.Label(janela, text="Insira o valor em centímetros:")
# Adiciona o rótulo à janela com espaço vertical
label_instrucoes.pack(pady=10)

# Campo de entrada para centímetros
entry_cm = tk.Entry(janela)  # Cria um campo de entrada
entry_cm.pack(pady=10)  # Adiciona o campo à janela com espaço vertical

# Botão para realizar a conversão
botao_converter = tk.Button(
    janela, text="Converter", command=converter)  # Cria o botão
botao_converter.pack(pady=10)  # Adiciona o botão à janela com espaço vertical

# Rótulo para mostrar o resultado
# Cria um rótulo vazio para exibir resultados
label_resultado = tk.Label(janela, text="")
label_resultado.pack(pady=10)  # Adiciona o rótulo à janela com espaço vertical

# Inicia o loop da interface gráfica
janela.mainloop()  # Mantém a janela aberta

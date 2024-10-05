import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

receitas = {
    'Macarrão com Molho de Tomate': ['macarrão', 'molho de tomate', 'óleo'],
    'Frango Grelhado': ['frango', 'óleo'],
    'Batata Frita': ['batata', 'óleo'],
    'Batata Frita com Queijo': ['batata', 'queijo', 'óleo'],
    'Brigadeiro de Colher': ['nescau', 'leite condensado', 'chocolate'],
    'Brigadeiro': ['nescau', 'chocolate', 'leite condensado', 'chocolate granulado'],
    'Cachorro Quente': ['pão', 'salsicha', 'molho de tomate'],
    'Lasanha': ['massa', 'molho de tomate', 'queijo', 'presunto'],
    'Lasanha Bolonhesa': ['massa', 'molho', 'queijo', 'presunto', 'carne moída'],
    'Bolo de Cenoura': ['farinha de trigo', 'cenoura', 'fermento', 'ovo', 'manteiga', 'açúcar'],
    'Bolo de Laranja': ['farinha de trigo', 'laranja', 'fermento', 'ovo', 'manteiga', 'açúcar'],
    'Bolo de Chocolate': ['farinha de trigo', 'chocolate', 'nescau', 'fermento', 'ovo', 'manteiga', 'açúcar'],
    'Brownie': ['farinha de trigo', 'nescau', 'açúcar', 'ovo', 'manteiga'],
    'Bife a Cavalo': ['bife', 'carne', 'ovo'],
    'Frango à Milanesa': ['frango', 'farinha de trigo', 'ovo', 'queijo'],
    'Farofa com Casca de Abacaxi': ['casca de abacaxi', 'cenoura', 'farinha de mandioca', 'cebola', 'azeite'],
    'Salada Panzanella': ['azeite', 'pão', 'pepino', 'tomate', 'cebola', 'manjericão', 'vinagre'],
    'Ovos com Carne Moída Bolonhesa': ['óleo', 'ovo', 'carne moída', 'folha de salsa'],
    'Grão-de-bico com Frango ao Molho': ['óleo', 'frango', 'cebola', 'alho', 'tomate', 'grão-de-bico', 'folha de salsa'],
    'Pimentão Recheado': ['óleo', 'cebola', 'carne moída', 'arroz', 'tomate', 'pimentão'],
    'Fritada de Macarrão': ['ovo', 'queijo', 'macarrão', 'óleo', 'tomate', 'folhas de manjericão']
}

receitas_passos = {
    'Brigadeiro de Colher': [
        'Adicione o leite condensado e 5 colheres de achocolatado na panela',
        'Cozinhe em fogo médio e mexa até que o brigadeiro comece a desgrudar da panela',
        'Coloque o brigadeiro em um recipiente e deixe esfriar'
    ],
    'Bolo de Cenoura': [
        'Adicione no liquidificar as cenouras cortadas, os ovos e a manteiga e misture',
        'Acrescente o açúcar e bata por 5 minutos',
        'Em uma tijela ou batedeira, adiciona a farinha de trigo e misture novamente',
        'Acrescente o fermento e misture lentamente com a colher',
        'Unte uma forma com a manteiga',
        'Despeje toda a mistura na forma untada',
        'Asse em um forno preaquecido a 180° graus por aproximadamente 40 minutos'
    ]
}
class AplicacaoReceitas:
    def __init__(self, root):
        self.root = root
        self.root.title("Recipe finder")
        self.root.geometry("600x400")  
        self.root.iconbitmap("Icone.ico")  

        #Adicionar Imagem

        images = Image.open("Jackin.png")
        images = images.resize((200, 200))
        corre = ImageTk.PhotoImage(images)
        
        corre_label = tk.Label(root, image=corre)
        corre_label.images = corre
        corre_label.pack(pady=10)
        corre_label.place(x=30, y=220)

        #AjustarLayout

        #self.root.configure(bg="#363636")

        self.titulo_label = tk.Label(root, text="Recipe Finder", font=("Times New Roman", 25),)
        self.titulo_label.pack(pady=10)

        self.ingredientes_label = tk.Label(root, text="Seja Bem-Vindo \n\n Digite os ingredientes (separados por vírgula):", font=("Arial", 14))
        self.ingredientes_label.pack(pady=30)
        
        #Entrada

        self.ingredientes_entry = tk.Entry(root, width=50, font=("Arial", 10))
        self.ingredientes_entry.pack(pady=10)
        
        #Botão de Procurar

        self.procurar_button = tk.Button(root, text="Procurar por Pratos", command=self.procurar_pratos, relief=tk.GROOVE, bg="#4CAF50", fg="white")
        self.procurar_button.pack(pady=20)
        
    def procurar_pratos(self):
        ingredientes_cliente = set(map(str.strip, self.ingredientes_entry.get().split(',')))

        pratos_encontrados = []
        for prato, ingredientes_prato in receitas.items():
            if  ingredientes_cliente.issubset(set(ingredientes_prato)):
                pratos_encontrados.append(prato)

        if pratos_encontrados:
            mensagem = f"Receitas possíveis: {', '.join(pratos_encontrados)}" 
            resposta = messagebox.askquestion("Receitas", mensagem + "\nDeseja continuar?")
            if resposta == 'yes':
                self.mostrar_ingredientes(pratos_encontrados)
                print("O usuário deseja continuar!")
            else:
                print("O usuário escolheu não continuar.")
        else:
            resposta = messagebox.askquestion("Receitas", "Nenhuma receita possível encontrada. Tente outros ingredientes.\n\nDeseja continuar?")
            if resposta == 'yes':
                print("O usuário deseja continuar!")
            else:
                print("O usuário escolheu não continuar.")
                root.destroy()

    def pergunta_continuar(self):
        resposta = messagebox.askquestion("Continuar?", "Deseja continuar?")
        if resposta == 'yes':
            print("O usuário deseja continuar!")
        else:
            print("O usuário escolheu não continuar.")

    def mostrar_ingredientes(self, pratos):
        janela_ingredientes = tk.Toplevel(self.root)
        janela_ingredientes.title("Ingredientes")

        for prato in pratos:
            label_prato = tk.Label(janela_ingredientes, text=prato, font=("Arial", 14, "bold"))
            label_prato.pack(pady=5)

            ingredientes_prato = ', '.join(receitas[prato])
            label_ingredientes = tk.Label(janela_ingredientes, text=f"Ingredientes: {ingredientes_prato}")
            label_ingredientes.pack(pady=5)

            botao_receita = tk.Button(janela_ingredientes, text="Mostrar Receita", command=lambda p=prato: self.mostrar_receita(p))
            botao_receita.pack(pady=10)

        botao_voltar = tk.Button(janela_ingredientes, text="Voltar à Tela Inicial", command=janela_ingredientes.destroy)
        botao_voltar.pack(pady=10)

    def mostrar_receita(self, prato):
        
        janela_receita = tk.Toplevel(self.root)
        janela_receita.title(f"Receita de {prato}")

        label_prato = tk.Label(janela_receita, text=prato, font=("Arial", 14, "bold"))
        label_prato.pack(pady=5)

        etapas_receita = receitas_passos.get(prato, ["Receita não disponível"])
        for i, etapa in enumerate(etapas_receita, start=1):
            label_etapa = tk.Label(janela_receita, text=f"Passo {i}: {etapa}")
            label_etapa.pack(pady=5)

        botao_voltar = tk.Button(janela_receita, text="Voltar aos Ingredientes", command=janela_receita.destroy)
        botao_voltar.pack(pady=10)
    
if __name__ == "__main__":
    root = tk.Tk()
    app = AplicacaoReceitas(root)
    root.mainloop()
# Cafeteria.py

# Lista para guardar dados
clientes = []
produtos = []
pedidos = []

# Menu Principal
def menu():
    while True:
        print("\n===== Menu da Cafeteria =====")
        print("1: Cadastrar Produtos")
        print("2: Listar Produtos")
        print("3: Cadastrar Clientes")
        print("4: Listar Clientes")
        print("5: Registrar Pedidos")
        print("6: Listar Pedidos")
        print("7:Buscar produto por nome")
        print("8: Remover Produto")
        print("9:Atualizar Produto")
        print("10: Relatorio de Vendas")
        print("11:Sair")

        opcao = input("Escolha uma opcao: ").strip()

        if opcao == "1":
            # cadastrar produto
            nome = input("nome do produto")
            try:
                preço = float(input("Preço do produto"))
                produto = {"nome": nome, "preço": preço }
                produtos.append(produto)
                print("Sucesso no cadastro do produto")
            except ValueError:
                print("Preço incorreto. Use números com ponto (.)")

        elif opcao == "2":
            # listar produtos
            if len(produtos) == 0:
                print("Não tem nenhum produto cadastrado ainda")
            else:
                print("\n===Produtos Cadastrados ===")
                for i, produto in enumerate(produtos):
                    print(f"{i+1}. {produto['nome']} - R$ {produto['preço']:.2f}")
            
           

        elif opcao == "3":
            #Cadastrar Clientes
            nome = input("nome do Cliente:") 
            telefone = input("telefone do cliente:")
            cliente = {"nome": nome, "telefone": telefone }
            clientes.append(cliente)
            print("Cadastro do cliente feito com sucesso!")

        elif opcao =="4":
            #LIstar Clientes
            if len(clientes) == 0:
                print("Não tem nenhum cliente cadastrado ainda")
            else:
                print("\n=== Clientes Cadastrados ===")
                for i, cliente in enumerate(clientes):
                    print(f"{i+1}. {cliente['nome']} - {cliente['telefone']}")

        elif opcao == "5":
            #Registrar Pedido
            sem_clientes = len(clientes) == 0
            sem_produtos = len(produtos) == 0

            if sem_clientes or sem_produtos:
                if sem_clientes:
                 print("Não tem nenhum cliente cadastrado" )
                if sem_produtos:
                    print("Não tem nenhum produto cadastrado")
                continue

            
            print("\n=== Clientes ===")
            for i, cliente in enumerate(clientes):
                 print(f"{i+1}. {cliente['nome']}")

            try:
               indice_cliente = int(input("Escolha um número pro cliente:")) - 1
               cliente_escolhido = clientes[indice_cliente]["nome"]
            except (ValueError, IndexError):
                print("Número de cliente incorreto")
                continue
            
            
            print("\n=== Produtos ===")
            for i, produto in enumerate(produtos):
                print(f"{i+1}. {produto['nome']} - R$ {produto['preço']:.2f}")

                mercadorias_pedidas = []
                total = 0

                while True:

                    escolha = input("Número do produto ( ou '0' para finalizar):")
                    if escolha == "0":
                        break
                    try:
                     indice_produto = int(escolha) - 1
                     produto_escolhido = produtos[indice_produto]
                     mercadorias_pedidas.append(produto_escolhido["nome"])
                     total += produto_escolhido["preço"]
                    except (ValueError, IndexError):
                        print("Produto incorreto")
                
                pedido = {
                    "Cliente": cliente_escolhido,
                    "Mercadorias": mercadorias_pedidas,
                    "Total": total

                }
                pedidos.append(pedido)
                print("Sucesso no registro do pedido!")


        elif opcao == "6":
            #Listar Pedidos
            if len(pedidos) == 0:
                print("Não tem pedido registrado ainda")
            else:
                print("\n=== Pedidos Registrados ===")
                for i, pedido in enumerate(pedidos):
                    print(f"{i+1}. Clientes: {pedido['cliente']}")
                    print(f"Mercadorias: {', '.join(pedido['produtos']) }")
                    print(f"Total: R$ {pedido['totsl']:.2f}")

                
                
        elif opcao == "7":
            # buscar produto por nome
            nome_busca = input("Nome do Produto: ")
            for produto in produtos:
                if nome_busca.lower() in produto["nome"].lower():
                    print(produto)

        elif opcao == "8":
          # remover produto
            for i, produto in enumerate(produtos):
                print(f"{i+1}. {produto['nome']}")
            try:
                indice = int(input("Número do produto para remover: ")) - 1
                if 0 <= indice < len(produtos):
                 produtos.pop(indice)
                 print("Sucesso em remover o produto")
                else:
                 print("Número incorreto")
            except ValueError:
              print("Entrada incorreta. Digite um número correto")

        elif opcao == "9":
        # Atualização do Produto
            for i, produto in enumerate(produtos):
                print(f"{i+1}. {produto['nome']} - R$ {produto['preco']}")
            try:
               indice = int(input("Número do produto: ")) - 1
               if 0 <= indice <  len(produtos):
                    novo_preco = float(input("Novo preço: "))
                    produtos[indice]["preco"] = novo_preco
                    print("Sucesso na atualização do produto!")
               else:
                    print("Número incorreto")
            except ValueError:
                    print("Entrada incorreta. Digite o número correto")
                        
        
                 
        elif opcao == "10":
         #Relatório de Vendas
            if len(pedidos) == 0:
                print("Não houve venda ainda")
            else:
                total_vendas = 0
                for pedido in pedidos:
                    total_vendas += pedido["total"]
                print(f"Total de vendas: R$ {total_vendas:.2f}")

        elif opcao == "11":
            #Sair do Sistema
            print("Sair do sistema")
            break

        else:
            #opção inexistente
            print("Opção inexistente. Tente novamente")

# Função Principal
menu()    

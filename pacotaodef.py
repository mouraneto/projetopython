# eu vou fazer as funções
import os
import time

estoque = {}


while True:
    try:
        menu = int(input('\nBem vindo(a) ao PaCoTãO\n Seu estoque online\n\n Digite:\n (1) Para adicionar um produto\n (2) Para revisar seu estoque\n (3) Para remover algum produto\n (4) Para limpar o estoque \n(0) Para sair\n-->'))

        def adicao():
            while True:
                produto = str(input("Digite o nome do produto:(aperte '0' para sair)\n"))
                if produto == '0':
                        os.system('cls')
                        break
                valor = int(input("Digite a quantidade do produto:"))
                estoque[produto] = valor
                print(estoque)
                time.sleep(1)
                os.system('cls')
                print(estoque)
        def revisao():
            os.system('cls')
            for i in estoque.keys():
                print(i)
                def total_produtos(estoque):
                    total=0
                    for quantidade in estoque.values():
                        total+= quantidade
                    return total
                quantidade_total = total_produtos(estoque)
                print("Quantidade total de produtos:", quantidade_total)
                time.sleep(2)
                input('Tecla enter para continuar')
                os.system('cls')
        def exclusao():
            os.system('cls')
            print(estoque)
            produto = str(input('Digite o nome do produto que deseja excluir: (Para sair, pressione Enter)'))
            del estoque[produto]  
            exclusao()
        def limpeza():
            os.system('cls')
            estoque.clear()
            print(estoque)
            time.sleep(1)
            os.system('cls')










        if menu == 1:
            adicao()
        elif menu == 2:
            revisao()
        elif menu == 3:
            exclusao()
        elif menu == 4:
            limpeza()
        elif menu == 0:
            os.system('cls')
            print('Obrigado por usar o PaCoTãO')
            time.sleep(1)
            break

    except ValueError:
        print('por favor, digite apenas números')
    except TypeError:
        print('type errssos')   
    except NameError:
        print('name error')
    except KeyError:
        print("não existe esse produto ou o estoque está vazio")
        time.sleep(1)
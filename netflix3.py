# A classe cliente deverá conter as seguintes informações:
# Nome, e-mail, plano do cliente
#
# A classe deverá permitir que o cliente altere o plano atual para basic ou premium ou vice-versa (upgrade ou downgrade). Em princípio, serão permitidos somente esses dois planos.
#
# Também deverá ser permitido que o cliente assista a um filme de acordo com o plano que ele assina.
# Se o plano do cliente for igual ao plano do filme, então ele poderá assistir o filme (exibir mensagem), caso contrário, se o plano do cliente for premium, ele também poderá ver o filme (exibir mensagem). Porém se o plano do cliente for o plano basic e o plano do filme for o premium, ele deverá fazer o upgrade para ver o filme (exibir mensagem).
#
# # Faça os testes de classe
# onde é criado um cliente com o plano basic;
# Exibido o plano do cliente;
#
# Cliente assistir a um filme do plano premium, sendo o plano do cliente basic
#
# Alteração de plano do cliente para premium;
#
# Cliente assistir a um filme do plano premium, sendo o plano do cliente premium (tendo feito upgrade)


# Vamos criar uma classe para clientes da Netflix
print("NETFLIX COM INPUTS")
# Pedir os atributos
nome = input("Informe o nome do cliente: ")
email = input("Informe o e-mail do cliente: ")
plano = input("Informe o plano do cliente (basic ou premium): ")
filme = input("Informe o filme para assistir: ")
plano_filme = input("Informe o plano do filme: ")

class Cliente:
    def __init__(self, nome, email, plano, filme, plano_filme):
        self.nome = nome
        self.email = email
        self.filme = filme
        self.plano_filme = plano_filme
        self.lista_planos = ["basic", "premium"]
        if plano in self.lista_planos:
            self.plano = plano
        else:
            raise Exception("Plano inválido") #indica que uma exceção ocorreu. A classe Cliente não será criada.

    def mudar_plano(self, novo_plano):
            if novo_plano in self.lista_planos:
                self.plano = novo_plano
            else:
                print("Plano inválido")

    def ver_filme(self, filme, plano_filme):
        if self.plano == plano_filme:
            return(f"Ver filme {filme}") #redirecionar para a página para o cliente assistir o filme
        elif self.plano == "premium":
            return(f"Ver filme {filme}")
        elif self.plano == "basic" and plano_filme == "premium":
            print("Faça upgrade para premium para ver esse filme")
            op = input("fazer upgrade (s/n): ")
            if op == 's':  # usuário deseja fazer upgrade?
                cliente1.mudar_plano("premium")
                return (f"Ver filme {filme}")
            # elif op == 'n':
            #     cliente1.mudar_plano("basic")
            #     return (f"Ver filme {filme}")
            # else: print('opção inválida')
        return("Plano inválido")

#Criar um objeto
cliente1 = Cliente(nome, email, plano, filme, plano_filme)

# Exibir o resultado
print("O resultado da consulta é: ", cliente1.nome, cliente1.ver_filme(filme, plano_filme))
# print("O plano do cliente é:", cliente.plano)
#
# # #Cliente assistir a um filme do plano premium, sendo o plano do cliente basic
# cliente.ver_filme("Harry Potter", "premium")
#
# # #no botão de upgrade
# # #Alteração de plano do cliente para premium;
# cliente.mudar_plano("confort")
# print(cliente.plano)
# #
# cliente.ver_filme("Harry Potter", "premium")
import cliente, empresa
lista=[]

def cadastrar():
    c = cliente.Cliente(None, None)
    c.nome = input("Digite seu nome: ")
    c.telefone = input("Digite seu telefone: ")
    if c.nome != None:
        print("Cliente cadastrado com sucesso!")
        lista.append(c)
        return c

def listar_clientes(lista):
    for i in lista:
        print(i.nome+", "+i.telefone)


def remover_cliente(lista, nome)
    for i in lista:
        if i.nome == nome:
            lista.remove(i)
    print(i.nome, "removido com sucesso!")

# listar_clientes(lista)

if __name__ == '__main__':

    cadastrar()

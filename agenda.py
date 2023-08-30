import os
agenda=[]
sair=False
while(sair==False):
    print("\n---- Agenda Telefônica ----")
    print("1 - Novo Contato")
    print("2 - Listar Contatos")
    print("3 - Editar Contato")
    print("4 - Excluir Contato")
    print("5 - Sair")
    opcao=int(input("Digite a opção desejada: "))

    if(opcao==1):                                           #Add novo contato
        novo_contato=[]
        nome=input("\nDigite o nome do contato:")
        novo_contato.append(nome)
        telefone=input("Digite o telefone do contato:")
        novo_contato.append(telefone)
        agenda.append(novo_contato)
        os.system('cls')
    
    if(opcao==2):
        for contato in agenda:
            print("\nNome:",contato[0],"Telefone:",contato[1],"\n")
    
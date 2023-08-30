import os
agenda=[]
sair=False
while(sair==False):                                                 #Loop principal
    print("\n---- Agenda Telefônica ----")
    print("1 - Novo Contato")
    print("2 - Listar Contatos")
    print("3 - Editar Contato")
    print("4 - Excluir Contato")
    print("5 - Sair")
    opcao=int(input("Digite a opção desejada: "))

    if(opcao==1):                                                   #Add novo contato
        novo_contato=[]
        nome=input("\nDigite o nome do contato:")
        novo_contato.append(nome)
        telefone=input("Digite o telefone do contato:")
        novo_contato.append(telefone)
        agenda.append(novo_contato)
        os.system('cls')
    
    if(opcao==2):                                                   #Exibir os contatos da agenda
        for contato in agenda:
            print("\nNome:",contato[0],"Telefone:",contato[1],"\n")
    
    if(opcao==3):                                                   #Editando os contatos da agenda
        nome=input("\nDigite o nome do contato a editar:")
        for i in range (len(agenda)):
            if(agenda[i][0]==nome):
                novo_nome=input("Digite um novo nome para o contato:")
                novo_telefone=input("Digite o novo número do contato:")
                agenda[i][0]=novo_nome
                agenda[i][1]=novo_telefone
                os.system('cls')
                break


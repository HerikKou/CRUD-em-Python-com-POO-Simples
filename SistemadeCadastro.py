class Main:
    def __init__(self,id,nome,email,idade):
        self.__id = id
        self.__nome = nome
        self.__email = email
        self.__idade = idade
    @property
    def nome(self):
        return self.__nome
    @nome.setter
    def nome(self,novoNome):
        self.__nome = novoNome

    @property
    def idade(self):
        return self.__idade 
    @idade.setter  
    def idade(self,novaIdade):
        self.__idade = novaIdade     
    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self,novoId):
        self.__id = novoId
    @property
    def email(self):
        return self.__email      
    @email.setter
    def email(self,novoEmail):
        self.__email = novoEmail     
    def toString(self):
       return f"ID: {self.id} | Nome: {self.nome} | Email: {self.email} | Idade: {self.idade}"

listaDeUsuarios=[]

while True:
    print("==Menu==")
    print("1-Cadastrar usuário")
    print("2-Buscar usuário por ID")
    print("3-Listar todos os usuários")
    print("4-Excluir Usuário")
    print("5-Sair")
    op = int(input("Digite sua opção:"))
    match op:
        case 1:
            id = int(input("Digite o ID do usuário:"))
            id2 = any(id == user.id for user in listaDeUsuarios)
            if(id2):
                print("Usuário já cadastrado")
                print("====")
              

            
            else:
                nome = input("Digite o nome do usuário")
                email = input("Digite o email do usuário")
                idade = int(input("Digite a idade do usuário:"))
                pessoas = Main(id,nome,email,idade)
                listaDeUsuarios.append(pessoas)
                for users in listaDeUsuarios:
                  print(users.toString())
                  print("====")
            print("Usuário Cadastrado com Sucesso!!") 
            print("====")     
            
        case 2: 
            if(not listaDeUsuarios):
                print("Nehum usuário cadastrado!!")
                print("====")
                
            id = int(input("Digite o ID do usuário:"))
            encontrado = False
            for users in listaDeUsuarios:
                if id == users.id:
                    print(users.toString())
                    encontrado = True
                   
                    print("====")
                    break
            if not encontrado:
             print("Usuário não encontrado!") 
             encontrado = False
             print("====")
            continue    
        case 3:
            if(not listaDeUsuarios):
                print("Nehum usuário cadastrado!!")
                print("====")
                continue
            for users in listaDeUsuarios:
                print(users.toString())
                print("====")
                  
        case 4:
            if(not listaDeUsuarios):
              print("Nehum usuário cadastrado!!")
              print("====")
              continue
            id = int(input("Digite o ID do usuário:"))
            encontrado = False
            for users in listaDeUsuarios:
                if id == users.id:
                    listaDeUsuarios.remove(users)
                    print("Usuário removido com sucesso!!")
                    encontrado = True
                    print("====") 
                    break 
            if not encontrado:
                print("Usuário não encontrado!") 
                print("====")
                continue
                   
                      
        case 5:
            print("Programa Encerrado")
            print("====")  
            break 

        case _:
            print("Opção inválida!")  
            print("====") 
            break             
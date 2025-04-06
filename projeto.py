class GerarExceção(Exception):   
    def __init__(self, mensagem) -> Exception:
        super().__init__(mensagem) 

class Cubo:

    def __init__(self):

        self.cubo = {
            0: [[None,None,None],[None,None,None],[None,None,None]],
            1: [[None,None,None],[None,None,None],[None,None,None]],
            2: [[None,None,None],[None,None,None],[None,None,None]],
            3: [[None,None,None],[None,None,None],[None,None,None]],
            4: [[None,None,None],[None,None,None],[None,None,None]],
            5: [[None,None,None],[None,None,None],[None,None,None]]
        }

        self.passos = [] # onde iremos armazenar todos os passos necessários para resolver o cubo

    # Esta função corrige a face girando-a no sentido anti horário
    def __corrigir_face_adjacente(self,face: list[list[str]]) -> list[list]: #utilizamos o _ para tornar o método privado utilizável somente pela classe

        linha_1 = face[0].copy() #criamos uma cópia da face, o que nos ajuda na hora de realizar a rotação
        linha_2 = face[1].copy() #pois a forma original não é perdida, logo ainda temos as informações
        linha_3 = face[2].copy() #necessárias para concluir o ajuste da face

        face[0][0] = linha_1[2]
        face[1][0] = linha_1[1]
        face[2][0] = linha_1[0]

        face[0][1] = linha_2[2]
        face[1][1] = linha_2[1]
        face[2][1] = linha_2[0]

        face[0][2] = linha_3[2]
        face[1][2] = linha_3[1]
        face[2][2] = linha_3[0]

        return face
        

    def rotacionar_uma_camada_no_sentido_anti_horário_na_horizontal(self, camada : int) -> None: #Horizontal(⬅️➡️)

        camada_face0 = copy(self.cubo[3][camada]) #aqui nós estamos salvando a camada dada como parâmetro
        camada_face1 = copy(self.cubo[0][camada]) #caso tenha sido escolhida a camada 1, por exemplo
        camada_face2 = copy(self.cubo[1][camada]) #então nós iremos salvar a camada 1 de todas as faces
        camada_face3 = copy(self.cubo[2][camada])

        self.cubo[0][camada] = camada_face0 # e logo em seguida realizamos as trocas, permitindo assim o nosso movimento
        self.cubo[1][camada] = camada_face1
        self.cubo[2][camada] = camada_face2
        self.cubo[3][camada] = camada_face3

        if camada == 0: #a face 4 é afetada

            self.cubo[4] = self.__corrigir_face_adjacente(self.cubo[4])


        elif camada == 2: #a face 5 é afetada

            self.cubo[5] = self.__corrigir_face_adjacente(self.cubo[5])


    def rotacionar_uma_camada_no_sentido_horário_na_horizontal(self, camada : int) -> None:

        self.rotacionar_uma_camada_no_sentido_anti_horário_na_horizontal(camada)
        self.rotacionar_uma_camada_no_sentido_anti_horário_na_horizontal(camada)
        self.rotacionar_uma_camada_no_sentido_anti_horário_na_horizontal(camada)

        #Rotacionar 3 vezes no sentido anti-horário equivale a rotacionar uma única vez no sentido horário


    def rotacionar_uma_coluna_no_sentido_anti_horário_na_vertical(self, coluna : int) -> None: #gira para frente
        if coluna in [0,1,2]:

            coluna0 = [self.cubo[0][0][coluna], self.cubo[0][1][coluna], self.cubo[0][2][coluna]] #aqui não estamos nos referindo a primeira coluna da primeira face, segunda coluna da primeira face etc. coluna1 é a primeira coluna
            coluna1 = [self.cubo[4][0][coluna], self.cubo[4][1][coluna], self.cubo[4][2][coluna]] #aqui não estamos nos referindo a primeira coluna da primeira face, segunda coluna da primeira face etc. coluna1 é a primeira coluna
            coluna2 = [self.cubo[2][0][coluna], self.cubo[2][1][coluna], self.cubo[2][2][coluna]] #da face 1, coluna2 é a primeira coluna da face superior (5), ou seja, é a sequência que iremos seguir. No caso de ser a primeira
            coluna3 = [self.cubo[5][0][coluna], self.cubo[5][1][coluna], self.cubo[5][2][coluna]] #é somente se a coluna que a pessoa escolher for a coluna 0.



            self.cubo[0][coluna][0] = coluna3[2]
            self.cubo[0][coluna][1] = coluna3[1]
            self.cubo[0][coluna][2] = coluna3[0]

            self.cubo[4][coluna][0] = coluna0[2]
            self.cubo[4][coluna][1] = coluna0[1]
            self.cubo[4][coluna][2] = coluna0[0]
            
            self.cubo[2][coluna][0] = coluna1[2]
            self.cubo[2][coluna][1] = coluna1[1]
            self.cubo[2][coluna][2] = coluna1[0]

            self.cubo[5][coluna][0] = coluna2[2]
            self.cubo[5][coluna][1] = coluna2[1]
            self.cubo[5][coluna][2] = coluna2[0]

            
        elif coluna in [3,4,5]:

            coluna = coluna - 3 #pois esta variável além de indicar a coluna, também serve para acessarmos os elementos na lista. Subtraimos 3, pois
            #os índices só vão até 2, ou seja, temos 3 índices por matriz: 0,1,2

            tabela_de_tradução = {0:2, 1:1,2:0} #na face 1 nós podemos acessar a coluna 2 somente acessando o índice 2 de cada linha, mas na face 4
            #é um pouco diferente. para que continuemos a linha reta, caso acessemos a coluna 0, então teremos que acessar a linha 2 da face 4.
            #aqui está sendo utilizado um dicionário para facilitar a conversão.

            coluna0 = [self.cubo[1][0][coluna], self.cubo[1][1][coluna], self.cubo[1][2][coluna]] #aqui não estamos nos referindo a primeira coluna da primeira face, segunda coluna da primeira face etc. coluna1 é a primeira coluna
            coluna1 = [self.cubo[4][tabela_de_tradução[coluna]][0], self.cubo[4][tabela_de_tradução[coluna]][1], self.cubo[4][tabela_de_tradução[coluna]][2]] #aqui não estamos nos referindo a primeira coluna da primeira face, segunda coluna da primeira face etc. coluna1 é a primeira coluna
            coluna2 = [self.cubo[3][0][coluna], self.cubo[3][1][coluna], self.cubo[3][2][coluna]] #da face 1, coluna2 é a primeira coluna da face superior (5), ou seja, é a sequência que iremos seguir. No caso de ser a primeira
            coluna3 = [self.cubo[5][tabela_de_tradução[coluna]][0], self.cubo[5][tabela_de_tradução[coluna]][1], self.cubo[5][tabela_de_tradução[coluna]][2]] #é somente se a coluna que a pessoa escolher for a coluna 0.


            self.cubo[0][0][coluna] = coluna3[2]
            self.cubo[0][1][coluna] = coluna3[1]
            self.cubo[0][2][coluna] = coluna3[0]

            self.cubo[4][tabela_de_tradução[coluna]][0] = coluna0[0]
            self.cubo[4][tabela_de_tradução[coluna]][1] = coluna0[1]
            self.cubo[4][tabela_de_tradução[coluna]][2] = coluna0[2]
            
            self.cubo[2][0][coluna] = coluna1[2]
            self.cubo[2][1][coluna] = coluna1[1]
            self.cubo[2][2][coluna] = coluna1[0]

            self.cubo[5][0][tabela_de_tradução[coluna]] = coluna2[0]
            self.cubo[5][1][tabela_de_tradução[coluna]] = coluna2[1]
            self.cubo[5][2][tabela_de_tradução[coluna]] = coluna2[2]

            if coluna == 0:
                self.__corrigir_face_adjacente(self.cubo[0])

            elif coluna == 2:
                self.__corrigir_face_adjacente(self.cubo[2]) #corrigimos rotacionando no sentido horário. Neste caso a face está invertida
                self.__corrigir_face_adjacente(self.cubo[0]) #então o movimento no sentido anti horário aqui não resolve, então nós chamamos
                self.__corrigir_face_adjacente(self.cubo[0]) #a função 3 vezes para rotacionarmos no sentido horário

        else:
            raise GerarExceção(f"{coluna} não é um número válido para uma coluna. Escolha uma coluna de 0 à 5.")


    def rotacionar_uma_coluna_no_sentido_horário_na_vertical(self, coluna : int) -> None: #Vertical(🔼🔽) #gira para trás

        if coluna in [0,1,2,3,4,5]:
            self.rotacionar_uma_coluna_no_sentido_anti_horário_na_vertical(coluna)
            self.rotacionar_uma_coluna_no_sentido_anti_horário_na_vertical(coluna)
            self.rotacionar_uma_coluna_no_sentido_anti_horário_na_vertical(coluna)
        else:
            raise GerarExceção(f"{coluna} não é um número válido para uma coluna. Escolha uma coluna de 0 à 5.") #ajudar o dev a encontrar o erro kkkk


    def verificar_se_a_cor_está_no_centro_da_face(self,face:list[list[str]],cor) -> bool:

        if cor == face[1][1]:
            return True
        else:
            return False
        

    def encontrar_o_centro(self,cor : str) -> int:
        
        f0 = self.verificar_se_a_cor_está_no_centro_da_face(self.cubo[0],cor)
        f1 = self.verificar_se_a_cor_está_no_centro_da_face(self.cubo[1],cor)
        f2 = self.verificar_se_a_cor_está_no_centro_da_face(self.cubo[2],cor)
        f3 = self.verificar_se_a_cor_está_no_centro_da_face(self.cubo[3],cor)
        f4 = self.verificar_se_a_cor_está_no_centro_da_face(self.cubo[4],cor)
        f5 = self.verificar_se_a_cor_está_no_centro_da_face(self.cubo[5],cor)

        if f0:
            return 0
        elif f1:
            return 1
        elif f2:
            return 2
        elif f3:
            return 3
        elif f4:
            return 4
        elif f5:
            return 5
        else:
            raise GerarExceção("O cubo inserido é inválido")


    def movimento_f(self) -> None:
        self.rotacionar_uma_coluna_no_sentido_horário_na_vertical(3)

    def movimento_f_linha(self) -> None:
        self.rotacionar_uma_coluna_no_sentido_anti_horário_na_vertical(3)

    def movimento_b(self) -> None:
        self.rotacionar_uma_coluna_no_sentido_horário_na_vertical(5)

    def movimento_b_linha(self) -> None:
        self.rotacionar_uma_coluna_no_sentido_anti_horário_na_vertical(3)

    def movimento_u(self) -> None:
        self.rotacionar_uma_camada_no_sentido_horário_na_horizontal(0)

    def movimento_u_linha(self) -> None:
        self.rotacionar_uma_camada_no_sentido_anti_horário_na_horizontal(0)

    def movimento_d(self) -> None:
        self.rotacionar_uma_camada_no_sentido_horário_na_horizontal(2)

    def movimento_d_linha(self) -> None:
        self.rotacionar_uma_camada_no_sentido_anti_horário_na_horizontal(2)

    def movimento_l(self) -> None:
        self.rotacionar_uma_coluna_no_sentido_horário_na_vertical(0)

    def movimento_l_linha(self) -> None:
        self.rotacionar_uma_coluna_no_sentido_anti_horário_na_vertical(0)

    def movimento_r(self) -> None:
        self.rotacionar_uma_coluna_no_sentido_horário_na_vertical(2)

    def movimento_r_linha(self) -> None:
        self.rotacionar_uma_camada_no_sentido_anti_horário_na_horizontal(2)

    def movimento_m(self) -> None:
        self.rotacionar_uma_coluna_no_sentido_horário_na_vertical(1)

    def movimento_m_linha(self) -> None: #esse movimento não existe oficialmente. É mais por organização
        self.rotacionar_uma_coluna_no_sentido_anti_horário_na_vertical(1)

    def movimento_e(self) -> None:
        self.rotacionar_uma_camada_no_sentido_horário_na_horizontal(1)

    def movimento_e_linha(self) -> None:
        self.rotacionar_uma_camada_no_sentido_anti_horário_na_horizontal(1)

    def movimento_s(self) -> None:
        self.rotacionar_uma_coluna_no_sentido_horário_na_vertical(1)

    def movimento_s_linha(self) -> None:
        self.rotacionar_uma_coluna_no_sentido_anti_horário_na_vertical(1)

    def movimento_x(self) -> None:
        self.girar_o_cubo_para_frente()

    def movimento_x_linha(self) -> None:
        self.girar_o_cubo_para_trás()

    def movimento_y(self) -> None:
        self.girar_o_cubo_no_sentido_anti_horário_na_horizontal()

    def movimento_y_linha(self) -> None:
        self.girar_o_cubo_no_sentido_horário_na_horizontal()

    def movimento_z(self) -> None:
        self.girar_o_cubo_no_sentido_anti_horário_na_vertical_para_o_lado()

    def movimento_z_linha(self) -> None:
        self.girar_o_cubo_no_sentido_horário_na_vertical_para_o_lado()


    def copiar_o_cubo_inteiro(self) -> dict[int,list[list[str]]]:
        return deepcopy(self.cubo)


    def girar_o_cubo_no_sentido_anti_horário_na_horizontal(self) -> None:

        cubo_cópia = self.copiar_o_cubo_inteiro()

        self.cubo[0] = cubo_cópia[3]
        self.cubo[1] = cubo_cópia[0]
        self.cubo[2] = cubo_cópia[1]
        self.cubo[3] = cubo_cópia[2]

        self.cubo[4] = self.__corrigir_face_adjacente(self.cubo[4])
        self.cubo[5] = self.__corrigir_face_adjacente(self.cubo[5])


    def girar_o_cubo_no_sentido_horário_na_horizontal(self) -> None:
        self.girar_o_cubo_no_sentido_anti_horário_na_horizontal()
        self.girar_o_cubo_no_sentido_anti_horário_na_horizontal()
        self.girar_o_cubo_no_sentido_anti_horário_na_horizontal()


    def girar_o_cubo_para_frente(self) -> None:
        self.rotacionar_uma_coluna_no_sentido_anti_horário_na_vertical(0)
        self.rotacionar_uma_coluna_no_sentido_anti_horário_na_vertical(1)
        self.rotacionar_uma_coluna_no_sentido_anti_horário_na_vertical(2)


    def girar_o_cubo_para_trás(self) -> None:
        self.girar_o_cubo_para_frente()
        self.girar_o_cubo_para_frente()
        self.girar_o_cubo_para_frente()


    def girar_o_cubo_no_sentido_anti_horário_na_vertical_para_o_lado(self) -> None:
        self.rotacionar_uma_coluna_no_sentido_anti_horário_na_vertical(3)
        self.rotacionar_uma_coluna_no_sentido_anti_horário_na_vertical(4)
        self.rotacionar_uma_coluna_no_sentido_anti_horário_na_vertical(5)


    def girar_o_cubo_no_sentido_horário_na_vertical_para_o_lado(self) -> None:
        self.girar_o_cubo_no_sentido_anti_horário_na_vertical_para_o_lado()
        self.girar_o_cubo_no_sentido_anti_horário_na_vertical_para_o_lado()
        self.girar_o_cubo_no_sentido_anti_horário_na_vertical_para_o_lado()


    def deixar_virada_para_cima_a_face_com_o_centro(self,cor : str) -> None:

        cor = self.encontrar_o_centro(cor)

        if cor == 0: #mapeando todos os casos possíveis
            self.girar_o_cubo_para_frente()
            self.passos.append("x")

        elif cor == 1:
            self.girar_o_cubo_no_sentido_anti_horário_na_horizontal()
            self.passos.append("y")

        elif cor == 2:
            self.girar_o_cubo_para_trás()
            self.passos.append("x'")

        elif cor == 3:
            self.girar_o_cubo_no_sentido_horário_na_horizontal()
            self.passos.append("y'")
            
        elif cor == 5:
            self.girar_o_cubo_para_frente()
            self.girar_o_cubo_para_frente()

            self.passos.append("x")
            self.passos.append("x")

        #não foi colocado um elif cor==4: pois nós queremos que a face fique na face 4, então esta verificação não faria sentido


    def verificar_se_a_cruz_branca_está_pronta(self) -> bool:

        if (self.cubo[4][0][1] == "branco" and
            self.cubo[4][1][0] == "branco" and
            self.cubo[4][1][2] == "branco" and
            self.cubo[4][2][1] == "branco"): 
            
            return True
        
        else:
            return False
        

    def encontrar_na_face_os_meios_da_cor_na_camada(self,cor : str,camada : int,face : list[list[str]]) -> list[int]:

        coordenadas = []

        if face[camada][0] == cor:
            coordenadas = [camada,0,None] #[camada,coluna,coluna do outro quadrado]

        if face[camada][2] == cor:

            if len(coordenadas) == 0: #se a lista não possuir nenhum elemento, então significa que a condição anterior foi falsa
                coordenadas = [camada,2,None]
            else:
                coordenadas[2] = 2

        if len(coordenadas) == 0: #ou seja, nós não encontramos nenhum centro da cor escolhida
            coordenadas = [None,None,None]

        return coordenadas


    def encontrar_os_meios_no_cubo_da_cor_na_camada(self,cor : str,camada : int) -> list[dict[str,int]]: #aplicável somente a faces 0,1,2,3. não funciona na face 4 nem 5.
        #para isso deve se girar o cubo antes de aplicar a função
        
        if camada not in [0,1,2]:
            raise GerarExceção("Camada inválida. Escolha uma camada entre 0 e 2")

        coordenadas : list[list[int]] = [] #o comentário de tipo é em relação ao que ela irá se tornar. Isso é somente para ajudar a IDE
        
        coordenadas.append(self.encontrar_na_face_os_meios_da_cor_na_camada(cor,1,self.cubo[0]))
        coordenadas[0].append(0)

        coordenadas.append(self.encontrar_na_face_os_meios_da_cor_na_camada(cor,1,self.cubo[1]))
        coordenadas[1].append(1)

        coordenadas.append(self.encontrar_na_face_os_meios_da_cor_na_camada(cor,1,self.cubo[2]))
        coordenadas[2].append(2)

        coordenadas.append(self.encontrar_na_face_os_meios_da_cor_na_camada(cor,1,self.cubo[3]))
        coordenadas[3].append(3)

        coordenadas_lista = []

        for coordenada in coordenadas:

            coordenada = { #traduzindo cada uma das informações em um dicionário para aumentar a legibilidade
                "camada" : coordenada[0],
                "coluna1" : coordenada[1],
                "coluna2" : coordenada[2],
                "face" : coordenada[3]
            }

            coordenadas_lista.append(coordenada)

        return coordenadas_lista


    def preparar_a_cruz_branca(self):
        
        if self.verificar_se_a_cruz_branca_está_pronta(): #só iremos formar a cruz branca se ela ainda não estiver formada
            
            self.deixar_virada_para_cima_a_face_com_o_centro("amarelo")

            coordenadas = self.encontrar_os_meios_no_cubo_da_cor_na_camada("branco",1)

            for coordenada in coordenadas:

                del coordenada["camada"]


                if coordenada["face"] == 0:
                    peso = 0 #por quanto teremos que adicionar para chegar a coluna real. no dicionário coordenadas nós temos, por exemplo, coluna
                    #0 na face 2, mas o problema é que em nosso sistema isso representa a coluna 3, ou seja, há uma discincronia. isso é para que
                    #ambos trabalhem da mesma forma.

                    sentido = 0 #isso indica que temos que girar no sentido anti horário. estamos usando números, pois eles são menos propensos
                    #a erros

                elif coordenada["face"] == 1:
                    peso = 3
                    sentido = 0

                elif coordenada["face"] == 2:
                    peso = 0
                    sentido = 1

                elif coordenada["face"] == 3:
                    peso = 3
                    sentido = 1


                if coordenada["coluna1"] != None:

                    if sentido == 0:
                        self.rotacionar_uma_coluna_no_sentido_anti_horário_na_vertical(coordenada["coluna1"] + peso)
                    else:
                        self.rotacionar_uma_coluna_no_sentido_horário_na_vertical(coordenada["coluna1"] + peso)

                if coordenada["coluna2"] != None: 

                    if sentido == 0:
                        self.rotacionar_uma_coluna_no_sentido_anti_horário_na_vertical(coordenada["coluna2"] + peso)
                    else:
                        self.rotacionar_uma_coluna_no_sentido_horário_na_vertical(coordenada["coluna2"] + peso)




    def resolver_o_cubo(self):

        print("==================Passos para resolver o cubo==================")
        print("1. Deixe a face com o centro amarelo virada para cima e a face com o centro azul virada para você")
       
        print()





    def verificar_se_o_cubo_é_válido(): #terminar <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
        pass


    def definir_cubo(self): #Esta é a função em que nós criamos o nosso cubo

        def casos(face):
            match face:
                case 0:
                    self.cubo[0][linha][coluna] = input(f"Digite a cor do quadrado presente nas seguintes coordenadas:\nface: {face}\nlinha: {linha}\ncoluna: {coluna}\n")

                case 1:
                    self.cubo[1][linha][coluna] = input(f"Digite a cor do quadrado presente nas seguintes coordenadas:\nface: {face}\nlinha: {linha}\ncoluna: {coluna}\n")

                case 2:
                    self.cubo[2][linha][coluna] = input(f"Digite a cor do quadrado presente nas seguintes coordenadas:\nface: {face}\nlinha: {linha}\ncoluna: {coluna}\n")

                case 3:
                    self.cubo[3][linha][coluna] = input(f"Digite a cor do quadrado presente nas seguintes coordenadas:\nface: {face}\nlinha: {linha}\ncoluna: {coluna}\n")
                    
                case 4:
                    self.cubo[4][linha][coluna] = input(f"Digite a cor do quadrado presente nas seguintes coordenadas:\nface: {face}\nlinha: {linha}\ncoluna: {coluna}\n")

                case 5:
                    self.cubo[5][linha][coluna] = input(f"Digite a cor do quadrado presente nas seguintes coordenadas:\nface: {face}\nlinha: {linha}\ncoluna: {coluna}\n")



        for face in range(0,7):
            for linha in range(0,3):
                for coluna in range(0,3):
                    casos(face)


    def mostrar_cubo(self):
        print(self.cubo[0])
        print(self.cubo[1])
        print(self.cubo[2])
        print(self.cubo[3])
        print(self.cubo[4])
        print(self.cubo[5])


    def verificar_se_a_face_está_resolvida(self,face):
        certos = 0
        acertos = 0

        primeiro = face[0][0]

        for linha in face:
            
            quantidade = count(primeiro,linha)
            if quantidade == 3:
                acertos = acertos + 1

        if acertos == 3:
            certos = certos + 1

        return certos


    def verificar_se_o_cubo_está_resolvido(self):

        acertos = 0

        acertos = acertos + self.verificar_se_a_face_está_resolvida(self.cubo[0])
        acertos = acertos + self.verificar_se_a_face_está_resolvida(self.cubo[1])
        acertos = acertos + self.verificar_se_a_face_está_resolvida(self.cubo[2])
        acertos = acertos + self.verificar_se_a_face_está_resolvida(self.cubo[3])
        acertos = acertos + self.verificar_se_a_face_está_resolvida(self.cubo[4])
        acertos = acertos + self.verificar_se_a_face_está_resolvida(self.cubo[5])

        if acertos == 6: #se todas as faces estão corretas
            return True
        else:
            return False                



def count(elemento,lista : list): #Portugol não tem o método count, então sou obrigado a recriá-lo

    quantidade = 0

    for posição in lista:
        if posição == elemento:
            quantidade = quantidade + 1

    return quantidade


def copy(objeto : dict | list): #portugol não tem suporte padrão ao copy. por esta razão estou recriando-o

    if type(objeto) == dict:

        chaves = objeto.keys()

        cópia = {}

        for chave in chaves:

            cópia[chave] = objeto[chave]


    elif type(objeto) == list:

        cópia = []

        for elemento in objeto:
            cópia.append(elemento)
   
    else:
        raise GerarExceção("Por favor insira um dado do tipo correto (list ou dict)")
    
    return cópia


def deepcopy(objeto : dict | list):

    if type(objeto) == dict:

        chaves = objeto.keys()

        cópia = {}

        for chave in chaves:
            
            cópia[chave] = deepcopy(objeto[chave])  # Chamada recursiva para garantir cópia profunda

        return cópia

    elif type(objeto) == list:

        cópia = []

        for elemento in objeto:

            if type(elemento) == list or type(elemento) == dict:
                cópia.append(deepcopy(elemento))  # Chamada recursiva para garantir cópia profunda
            else:
                
                cópia.append(elemento)

        return cópia

    else:
        return objeto


def len(iterável):
    quantidade = 0

    for elemento in iterável:
        quantidade = quantidade + 1

    return quantidade


def reverse(iterável):

    tamanho = len(iterável)

    invertido = [None] * tamanho

    posição = tamanho

    for elemento in iterável:

        posição = posição - 1

        invertido[posição] = elemento

    return invertido

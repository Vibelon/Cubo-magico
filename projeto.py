class GerarExceção(Exception):   
    def __init__(self, mensagem):
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
        

    def rotacionar_no_sentido_anti_horário_na_horizontal(self, camada : int) -> None: #Horizontal(⬅️➡️)

        camada_face0 = self.cubo[3][camada].copy() #aqui nós estamos salvando a camada dada como parâmetro
        camada_face1 = self.cubo[0][camada].copy() #caso tenha sido escolhida a camada 1, por exemplo
        camada_face2 = self.cubo[1][camada].copy() #então nós iremos salvar a camada 1 de todas as faces
        camada_face3 = self.cubo[2][camada].copy()

        self.cubo[0][camada] = camada_face0 # e logo em seguida realizamos as trocas, permitindo assim o nosso movimento
        self.cubo[1][camada] = camada_face1
        self.cubo[2][camada] = camada_face2
        self.cubo[3][camada] = camada_face3

        if camada == 0: #a face 4 é afetada

            self.cubo[4] = self.__corrigir_face_adjacente(self.cubo[4])


        elif camada == 2: #a face 5 é afetada

            self.cubo[5] = self.__corrigir_face_adjacente(self.cubo[5])


    def rotacionar_no_sentido_horário_na_horizontal(self, camada):

        self.rotacionar_no_sentido_anti_horário_na_horizontal(camada)
        self.rotacionar_no_sentido_anti_horário_na_horizontal(camada)
        self.rotacionar_no_sentido_anti_horário_na_horizontal(camada)

        #Rotacionar 3 vezes no sentido anti-horário equivale a rotacionar uma única vez no sentido horário



    def rotacionar_no_sentido_anti_horário_na_vertical(self, coluna : int):
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


    def rotacionar_no_sentido_horário_na_vertical(self, coluna): #Vertical(🔼🔽)

        if coluna in [0,1,2,3,4,5]:
            self.rotacionar_no_sentido_anti_horário_na_vertical(coluna)
            self.rotacionar_no_sentido_anti_horário_na_vertical(coluna)
            self.rotacionar_no_sentido_anti_horário_na_vertical(coluna)
        else:
            raise GerarExceção(f"{coluna} não é um número válido para uma coluna. Escolha uma coluna de 0 à 5.") #ajudar o dev a encontrar o erro kkkk


    def movimento_f(self):
        self.rotacionar_no_sentido_horário_na_vertical(3)

    def movimento_f_linha(self):
        self.rotacionar_no_sentido_anti_horário_na_vertical(3)

    def movimento_b(self):
        self.rotacionar_no_sentido_horário_na_vertical(5)

    def movimento_b_linha(self):
        self.rotacionar_no_sentido_anti_horário_na_vertical(3)

    def movimento_u(self):
        self.rotacionar_no_sentido_horário_na_horizontal(0)

    def movimento_u_linha(self):
        self.rotacionar_no_sentido_anti_horário_na_horizontal(0)

    def movimento_d(self):
        self.rotacionar_no_sentido_horário_na_horizontal(2)

    def movimento_d_linha(self):
        self.rotacionar_no_sentido_anti_horário_na_horizontal(2)

    def movimento_l(self):
        self.rotacionar_no_sentido_horário_na_vertical(0)

    def movimento_l_linha(self):
        self.rotacionar_no_sentido_anti_horário_na_vertical(0)

    def movimento_r(self):
        self.rotacionar_no_sentido_horário_na_vertical(2)

    def movimento_r_linha(self):
        self.rotacionar_no_sentido_anti_horário_na_horizontal(2)

    def movimento_m(self):
        self.rotacionar_no_sentido_horário_na_vertical(1)

    def movimento_m_linha(self): #esse movimento não existe oficialmente. É mais por organização
        self.rotacionar_no_sentido_anti_horário_na_vertical(1)

    def movimento_e(self):
        self.rotacionar_no_sentido_horário_na_horizontal(1)

    def movimento_e_linha(self):
        self.rotacionar_no_sentido_anti_horário_na_horizontal(1)

    def movimento_s(self):
        self.rotacionar_no_sentido_horário_na_vertical(1)

    def movimento_s_linha(self):
        self.rotacionar_no_sentido_anti_horário_na_vertical(1)


    def resolver_o_cubo(self):

        def encontrar_o_centro(cor : str) -> int:

            def verificar_se_a_cor_está_no_centro_da_face(face:list[list[str]]) -> bool:

                if cor == face[1][1]:
                    return True
                else:
                    return False
            
            f0 = verificar_se_a_cor_está_no_centro_da_face(self.cubo[0])
            f1 = verificar_se_a_cor_está_no_centro_da_face(self.cubo[1])
            f2 = verificar_se_a_cor_está_no_centro_da_face(self.cubo[2])
            f3 = verificar_se_a_cor_está_no_centro_da_face(self.cubo[3])
            f4 = verificar_se_a_cor_está_no_centro_da_face(self.cubo[4])
            f5 = verificar_se_a_cor_está_no_centro_da_face(self.cubo[5])

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
            
        print("==================Passos para resolver o cubo==================")
        print("1. Deixe a face com o centro amarelo virada para cima e a face com o centro azul virada para você")
        print("2. A face com o centro azul será a face 0")


        amarelo = encontrar_o_centro("amarelo")
        branco = encontrar_o_centro("branco")

        verde = encontrar_o_centro("verde")
        azul = encontrar_o_centro("azul")

        amarelo = encontrar_o_centro("vermelho")
        amarelo = encontrar_o_centro("laranja")

            
        


    def definir_cubo(self): #Esta é a função em que nós criamos o nosso cubo

        def casos(face):
            match face:
                case 0:
                    self.face0[linha][coluna] = input(f"Digite a cor do quadrado presente nas seguintes coordenadas:\nface: {face}\nlinha: {linha}\ncoluna: {coluna}\n")

                case 1:
                    self.face1[linha][coluna] = input(f"Digite a cor do quadrado presente nas seguintes coordenadas:\nface: {face}\nlinha: {linha}\ncoluna: {coluna}\n")

                case 2:
                    self.face2[linha][coluna] = input(f"Digite a cor do quadrado presente nas seguintes coordenadas:\nface: {face}\nlinha: {linha}\ncoluna: {coluna}\n")

                case 3:
                    self.face3[linha][coluna] = input(f"Digite a cor do quadrado presente nas seguintes coordenadas:\nface: {face}\nlinha: {linha}\ncoluna: {coluna}\n")
                    
                case 4:
                    self.face4[linha][coluna] = input(f"Digite a cor do quadrado presente nas seguintes coordenadas:\nface: {face}\nlinha: {linha}\ncoluna: {coluna}\n")

                case 5:
                    self.face5[linha][coluna] = input(f"Digite a cor do quadrado presente nas seguintes coordenadas:\nface: {face}\nlinha: {linha}\ncoluna: {coluna}\n")



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

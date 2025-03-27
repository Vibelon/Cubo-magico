class GerarExceção(Exception):   
    def __init__(self, mensagem):
        super().__init__(mensagem) 

class Cubo:

    def __init__(self):
        self.face0 = [[None,None,None],[None,None,None],[None,None,None]] #Portugol não possui listas dinâmicas, então preciso fazer assim para me aproximar ao máximo
        self.face1 = [[None,None,None],[None,None,None],[None,None,None]] #do portugol, com listas de tamanhos já pré definidos
        self.face2 = [[None,None,None],[None,None,None],[None,None,None]]
        self.face3 = [[None,None,None],[None,None,None],[None,None,None]]
        self.face4 = [[None,None,None],[None,None,None],[None,None,None]]
        self.face5 = [[None,None,None],[None,None,None],[None,None,None]]

    # Esta função corrige a face girando-a no sentido anti horário
    def __corrigir_face_adjacente(self,face: list[list]) -> list[list]: #utilizamos o _ para tornar o método privado utilizável somente pela classe

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

        camada_face0 = self.face3[camada].copy() #aqui nós estamos salvando a camada dada como parâmetro
        camada_face1 = self.face0[camada].copy() #caso tenha sido escolhida a camada 1, por exemplo
        camada_face2 = self.face1[camada].copy() #então nós iremos salvar a camada 1 de todas as faces
        camada_face3 = self.face2[camada].copy()

        self.face0[camada] = camada_face0 # e logo em seguida realizamos as trocas, permitindo assim o nosso movimento
        self.face1[camada] = camada_face1
        self.face2[camada] = camada_face2
        self.face3[camada] = camada_face3

        if camada == 0: #a face 4 é afetada

            self.face4 = self.__corrigir_face_adjacente(self.face4)


        elif camada == 2: #a face 5 é afetada

            self.face5 = self.__corrigir_face_adjacente(self.face5)


    def rotacionar_no_sentido_horário_na_horizontal(self, camada):

        self.rotacionar_no_sentido_anti_horário_na_horizontal(camada)
        self.rotacionar_no_sentido_anti_horário_na_horizontal(camada)
        self.rotacionar_no_sentido_anti_horário_na_horizontal(camada)

        #Rotacionar 3 vezes no sentido anti-horário equivale a rotacionar uma única vez no sentido horário



    def rotacionar_no_sentido_anti_horário_na_vertical(self, coluna : int):
        if coluna in [0,1,2]:

            coluna0 = [self.face0[0][coluna], self.face0[1][coluna], self.face0[2][coluna]] #aqui não estamos nos referindo a primeira coluna da primeira face, segunda coluna da primeira face etc. coluna1 é a primeira coluna
            coluna1 = [self.face4[0][coluna], self.face4[1][coluna], self.face4[2][coluna]] #aqui não estamos nos referindo a primeira coluna da primeira face, segunda coluna da primeira face etc. coluna1 é a primeira coluna
            coluna2 = [self.face2[0][coluna], self.face2[1][coluna], self.face2[2][coluna]] #da face 1, coluna2 é a primeira coluna da face superior (5), ou seja, é a sequência que iremos seguir. No caso de ser a primeira
            coluna3 = [self.face5[0][coluna], self.face5[1][coluna], self.face5[2][coluna]] #é somente se a coluna que a pessoa escolher for a coluna 0.



            self.face0[coluna][0] = coluna3[2]
            self.face0[coluna][1] = coluna3[1]
            self.face0[coluna][2] = coluna3[0]

            self.face4[coluna][0] = coluna0[2]
            self.face4[coluna][1] = coluna0[1]
            self.face4[coluna][2] = coluna0[0]
            
            self.face2[coluna][0] = coluna1[2]
            self.face2[coluna][1] = coluna1[1]
            self.face2[coluna][2] = coluna1[0]

            self.face5[coluna][0] = coluna2[2]
            self.face5[coluna][1] = coluna2[1]
            self.face5[coluna][2] = coluna2[0]


            
            
        elif coluna in [3,4,5]:

            coluna = coluna - 3 #pois esta variável além de indicar a coluna, também serve para acessarmos os elementos na lista. Subtraimos 3, pois
            #os índices só vão até 2, ou seja, temos 3 índices por matriz: 0,1,2

            coluna0 = [self.face1[0][coluna], self.face1[1][coluna], self.face1[2][coluna]] #aqui não estamos nos referindo a primeira coluna da primeira face, segunda coluna da primeira face etc. coluna1 é a primeira coluna
            coluna1 = [self.face4[coluna][0], self.face4[coluna][1], self.face4[coluna][2]] #aqui não estamos nos referindo a primeira coluna da primeira face, segunda coluna da primeira face etc. coluna1 é a primeira coluna
            coluna2 = [self.face3[0][coluna], self.face3[1][coluna], self.face3[2][coluna]] #da face 1, coluna2 é a primeira coluna da face superior (5), ou seja, é a sequência que iremos seguir. No caso de ser a primeira
            coluna3 = [self.face5[coluna][0], self.face5[coluna][1], self.face5[coluna][2]] #é somente se a coluna que a pessoa escolher for a coluna 0.



            self.face0[0][coluna] = coluna3[2]
            self.face0[1][coluna] = coluna3[1]
            self.face0[2][coluna] = coluna3[0]

            self.face4[0][coluna] = coluna0[2]
            self.face4[1][coluna] = coluna0[1]
            self.face4[2][coluna] = coluna0[0]
            
            self.face2[0][coluna] = coluna1[2]
            self.face2[1][coluna] = coluna1[1]
            self.face2[2][coluna] = coluna1[0]

            self.face5[0][coluna] = coluna2[2]
            self.face5[1][coluna] = coluna2[1]
            self.face5[2][coluna] = coluna2[0]

            if coluna == 0:
                self.__corrigir_face_adjacente(self.face0)

            elif coluna == 2:
                self.__corrigir_face_adjacente(self.face2) #corrigimos rotacionando no sentido anti horário. Neste caso a face está invertida
                self.__corrigir_face_adjacente(self.face0) #então o movimento no sentido anti horário aqui não resolve, então nós chamamos
                self.__corrigir_face_adjacente(self.face0) #a função 3 vezes para rotacionarmos no sentido horário

        else:
            raise GerarExceção(f"{coluna} não é um número válido para uma coluna. Escolha uma coluna de 0 à 5.")


    def rotacionar_no_sentido_horário_na_vertical(self, coluna): #Vertical(🔼🔽)

        if coluna in [0,1,2,3,4,5]:
            self.rotacionar_no_sentido_anti_horário_na_vertical(coluna)
            self.rotacionar_no_sentido_anti_horário_na_vertical(coluna)
            self.rotacionar_no_sentido_anti_horário_na_vertical(coluna)
        else:
            raise GerarExceção(f"{coluna} não é um número válido para uma coluna. Escolha uma coluna de 0 à 5.") #ajudar o dev a encontrar o erro kkkk


    def movimento_f():
        pass

    def movimento_f_linha():
        pass

    def movimento_b():
        pass

    def movimento_b_linha():
        pass

    def movimento_u():
        pass

    def movimento_u_linha():
        pass

    def movimento_d():
        pass

    def movimento_d_linha():
        pass

    def movimento_l():
        pass

    def movimento_l_linha():
        pass

    def movimento_r():
        pass

    def movimento_r_linha():
        pass

    def movimento_m():
        pass

    def movimento_e():
        pass

    def movimento_s():
        pass



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
        print(self.face0)
        print(self.face1)
        print(self.face2)
        print(self.face3)
        print(self.face4)
        print(self.face5)


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

        acertos = acertos + self.verificar_se_a_face_está_resolvida(self.face0)
        acertos = acertos + self.verificar_se_a_face_está_resolvida(self.face1)
        acertos = acertos + self.verificar_se_a_face_está_resolvida(self.face2)
        acertos = acertos + self.verificar_se_a_face_está_resolvida(self.face3)
        acertos = acertos + self.verificar_se_a_face_está_resolvida(self.face4)
        acertos = acertos + self.verificar_se_a_face_está_resolvida(self.face5)

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

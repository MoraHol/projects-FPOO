class AtributosMotos():
    pass
    marca = ""
    modelo = ""
    color = ""
    valor = 0.0
    cilindara = 0.0
    velocidad_max = 0.0

    def KawasakiNinjaH2R(self):
        ## objeto creado para definir atributos
        H2R = AtributosMotos

        ## Definicion de atributos para esta moto
        H2R.marca = "Kawasaki"
        H2R.modelo = "2017"
        H2R.color = "Gris-verde"
        H2R.valor = 64428.16
        H2R.cilindrada = 992
        H2R.velocidad_max = 400

        print("Esta son las caracteristicas de la Ninja H2R: \n")
        print("La marca de la moto es : " + H2R.marca)
        print("El modelo de la moto es : " + H2R.modelo)
        print("El color de la moto es : " + H2R.color)
        print("El valor de la moto es : US $ ", H2R.valor)
        print("La cilindrada de la moto es : ", H2R.cilindrada)
        print("La velocidad maxima de la moto es : ", H2R.velocidad_max, " Km/h \n")

    def DucatiMultistrada(self):
        Multistrada = AtributosMotos()

        ## Definicion de atributos para esta moto

        Multistrada.marca = "Ducati"
        Multistrada.modelo = "2016"
        Multistrada.color = "Roja"
        Multistrada.valor = 19895.19
        Multistrada.cilindrada = 1200
        Multistrada.velocidad_max = 299

        # impresion de atributos
        print("Esta son las caracteristicas de la Ducati Multistrada: \n")
        print("La marca de la moto es : " + Multistrada.marca)
        print("El modelo de la moto es : " + Multistrada.modelo)
        print("El color de la moto es : " + Multistrada.color)
        print("El valor de la moto es : US $", Multistrada.valor)
        print("La cilindrada de la moto es : ", Multistrada.cilindrada, "c.c")
        print("La velocidad maxima de la moto es : ", Multistrada.velocidad_max, " Km/h \n")

    def YamahaR1M(self):
        ## definicion del objeto
        R1M = AtributosMotos()
        ## Definicion de atributos para esta moto
        R1M.marca = "Yamaha"
        R1M.modelo = "2018"
        R1M.color = "Gris"
        R1M.valor = 25085.788
        R1M.cilindrada = 998
        R1M.velocidad_max = 350

        # impresion de atributos
        print("Esta son las caracteristicas de la Yamaha R1M: \n")
        print("La marca de la moto es : " + R1M.marca)
        print("El modelo de la moto es : " + R1M.modelo)
        print("El color de la moto es : " + R1M.color)
        print("El valor de la moto es : US $", R1M.valor)
        print("La cilindrada de la moto es : ", R1M.cilindrada, "c.c")
        print("La velocidad maxima de la moto es : ", R1M.velocidad_max, " Km/h" + "\n")

    def YamahaFZ(self):
        """ definicion de objeto"""
        FZ = AtributosMotos()

        # Definicion de atributos para esta moto
        FZ.marca = "Yamaha"
        FZ.modelo = "2017"
        FZ.color = "Gris-Azul"
        FZ.valor = 2200.475
        FZ.cilindrada = 149
        FZ.velocidad_max = 135

        # impresion de atributos
        print("Esta son las caracteristicas de la Yamaha FZ 2.0: \n")
        print("La marca de la moto es : " + FZ.marca)
        print("El modelo de la moto es : " + FZ.modelo)
        print("El color de la moto es : " + FZ.color)
        print("El valor de la moto es : US $", FZ.valor)
        print("La cilindrada de la moto es : ", FZ.cilindrada, "c.c")
        print("La velocidad maxima de la moto es : ", FZ.velocidad_max, " Km/h" + "\n")



class Atributos():
    pass
    # Creacion de objeto par llamar los atributos de las motos
    Atm = AtributosMotos()

    print("Acontinuacion se presentan los atributos de 4 motos Diferentes: \n")
    Atm.KawasakiNinjaH2R()
    Atm.DucatiMultistrada()
    Atm.YamahaR1M()
    Atm.YamahaFZ()

import classYoutube
class main:
    def __init__(self):
        self.clYT = classYoutube.classYoutube()

    def menu(self):
        i = 0
        while i < 1:
            print("1.- Youtube")
            #print("2.- Facebook")
            print("2.- Salir")

            opcion = input("Seleccione el modulo: ")

            if opcion == "1":
                self.clYT.menu()
            #elif opcion == "2":
                #o = ""
            else:
                opcion = input("¿Desea Salir? (S/N): ")
                if opcion.upper() == "S":
                    i = 2
                    print("ADIOS!!!")
                    exit()

prin = main()
prin.menu()
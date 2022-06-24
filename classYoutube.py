from pytube import YouTube
import classConfig
class classYoutube:
    def __init__(self):
        self.resolution = ""
        self.clConf = classConfig.classConfig()
        self.load()

    def menu(self):
        m = 0
        while m < 1:
            print("    ", "*"*100)
            print("     1.- Descargar Video")
            print("     2.- Descargar solo audio")
            print("     3.- Configurar")
            print("     4.- Regresar")
            print("    ", "*"*100)
            opcion = input("     Seleccione el modulo: ")
            if opcion == "1":
                self.video()
            elif opcion == "2":
                self.audio()
            elif opcion == "3":
                self.config()
            else:
                m = 3

    def video(self):
        link = input('     Ingresa el URL: ')
        yt = YouTube(link)
        yt.streams.filter(res=self.resolution).first().download()
        print('     Video Descargado!!', yt.title)

    def audio(self):
        link = input('     Ingresa el URL: ')
        yt = YouTube(link)
        yt.streams.filter(only_audio=True).first().download()
        print('     Audio Descargado', yt.title)

    def config(self):
        Resolution = ""
        Resolution = input("Ingrese la Resolución que desea descargar los videos (360p, 720p, 1080p):")
        self.clConf.configYoutube(Resolution)

    def load(self):
        self.clConf.load()
        lstConfig = []
        if len(self.clConf.lstConfig) > 0:
            lstConfig = self.clConf.lstConfig[0]
            x = lstConfig.configuracion
            for y in x:
                if y.nombre == "Resolution":
                    self.resolution = y.valor
        else:
            print("Se volvera a cargar la configuracion")
            self.clConf.createConfig()
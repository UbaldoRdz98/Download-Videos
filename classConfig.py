import json
class classConfig:
    def __init__(self):
        self.modulo = ""
        self.configuracion = []
        self.nombre = ""
        self.valor = ""
        self.lstConfig = []
        self.filename = "Config.JSON"

    def configYoutube(self, resolution):
        l = []
        n = classConfig()
        n.nombre = "Resolution"
        n.valor = resolution
        l.append(n)
        self.lstConfig[0].configuracion = l
        y = self.jsonCreate()

    def createConfig(self):
        l = []
        m = classConfig()
        m.modulo = "Youtube"
        n = classConfig()
        n.nombre = "Resolution"
        n.valor = "720p"
        l.append(n)
        m.configuracion = l
        self.lstConfig.append(m)
        y = self.jsonCreate()

    def load(self):
        self.lstConfig.clear()
        with open(self.filename, 'r') as openfile:
            json_object = json.load(openfile)

        for x in json_object:
            l = []
            m = classConfig()
            m.modulo = x["Modulo"]
            for y in x["Configuracion"]:
                n = classConfig()
                n.nombre = y["Nombre"]
                n.valor = y["Valor"]
                l.append(n)
            m.configuracion = l
            self.lstConfig.append(m)
        return self.lstConfig

    def jsonCreate(self):
        ls = []
        lc = []
        for x in self.lstConfig:
            for y in x.configuracion:
                lc.append({"Nombre": y.nombre, "Valor": y.valor})
            ls.append({"Modulo": x.modulo, "Configuracion": lc})
            lc = []
        
        with open(self.filename, "w") as file:
            json.dump(ls, file, indent = 4)
        valida = True
        m = 3
        return m
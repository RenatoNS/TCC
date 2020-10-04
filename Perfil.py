class Perfil:

    def personalizar(self, vector):
        sort = vector.sort()
        if (sort[4] == 0):
            perfil = "Conservador"
        elif (sort[4] == 1):
            perfil = "Conservador"
        elif (sort[4] == 2):
            perfil = "Moderado"
        else:
            perfil = "Agressivo"
        return perfil

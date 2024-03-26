class Ordenacao():

    def __init__(self, array_para_ordenar):
        self.array_para_ordenar = array_para_ordenar

    def ordena(self):
        hold = 0
        for i in range(len(self.array_para_ordenar)-1, 0, -1):
            for l in range(i):
                if self.array_para_ordenar[l] > self.array_para_ordenar[l+1]:
                    hold = self.array_para_ordenar[l]
                    self.array_para_ordenar[l] = self.array_para_ordenar[l+1]
                    self.array_para_ordenar[l+1] = hold
            
        return self.array_para_ordenar
    
    def to_string(self):
        convert_string = ''
        for i in range(len(self.array_para_ordenar)):
            if i != (len(self.array_para_ordenar) - 1):
                convert_string += str(self.array_para_ordenar[i]) + ','
            else:
                convert_string += str(self.array_para_ordenar[i])

        return convert_string


a = Ordenacao([10,5,5,4,3])

a.ordena()

print(a.to_string())
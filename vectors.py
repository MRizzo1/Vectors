# Python Program illustrate how
# to overload an binary + operator

class Vector:
    def __init__(self, vector=[]):
        if len(vector) > 1 and isinstance(vector[0], list) and len(vector[0]) > 1:
            raise ValueError(
                'El vector debe ser una fila o una columna.')

        self.vector = vector

    # adding two vectors
    def __add__(self, o):
        # if we are adding a number to a vector
        if isinstance(o, int) or isinstance(o, float):
            sumVector = []

            if (len(self.vector) == 0):
                return Vector(sumVector)

            if (not isinstance(self.vector[0], list)):
                for i in range(len(self.vector)):
                    sumVector.append(self.vector[i] + o)
                return Vector(sumVector)

            for i in range(len(self.vector)):
                sumVector.append([self.vector[i][0] + o])
            return Vector(sumVector)

        if (len(self.vector) == 0):
            return Vector([])

        # if not, we are adding two vectors
        if len(self.vector) != len(o.vector):
            raise ValueError(
                'Ambos vectores deben tener las mismas dimensiones')
        elif (isinstance(self.vector[0], list) and not isinstance(o.vector[0], list)) or (not isinstance(self.vector[0], list) and isinstance(o.vector[0], list)):
            raise ValueError(
                'Ambos vectores deben tener las mismas dimensiones (Uno es una columna y el otro es una fila)')

        sumVector = []

        if (not isinstance(self.vector[0], list) and not isinstance(o.vector[0], list)):
            for i in range(len(self.vector)):
                sumVector.append(self.vector[i] + o.vector[i])
            return Vector(sumVector)

        for i in range(len(self.vector)):
            sumVector.append([self.vector[i][0] + o.vector[i][0]])
        return Vector(sumVector)

    # substracting two vectors
    def __sub__(self, o):
        # if we are substracting a number to a vector
        if isinstance(o, int) or isinstance(o, float):
            subVector = []

            if (len(self.vector) == 0):
                return Vector(subVector)

            if (not isinstance(self.vector[0], list)):
                for i in range(len(self.vector)):
                    subVector.append(self.vector[i] - o)
                return Vector(subVector)

            for i in range(len(self.vector)):
                subVector.append([self.vector[i][0] - o])
            return Vector(subVector)

        if (len(self.vector) == 0):
            return Vector([])

        # if not, we are substracting two vectors
        if len(self.vector) != len(o.vector):
            raise ValueError(
                'Ambos vectores deben tener las mismas dimensiones')
        elif (isinstance(self.vector[0], list) and not isinstance(o.vector[0], list)) or (not isinstance(self.vector[0], list) and isinstance(o.vector[0], list)):
            raise ValueError(
                'Ambos vectores deben tener las mismas dimensiones (Uno es una columna y el otro es una fila)')

        subVector = []

        if (not isinstance(self.vector[0], list) and not isinstance(o.vector[0], list)):
            for i in range(len(self.vector)):
                subVector.append(self.vector[i] - o.vector[i])
            return Vector(subVector)

        for i in range(len(self.vector)):
            subVector.append([self.vector[i][0] - o.vector[i][0]])
        return Vector(subVector)

    # cross product of two vectors
    def __mul__(self, o):
        # if we are multiplying a number to a vector
        if isinstance(o, int) or isinstance(o, float):
            if len(self.vector) != 3:
                raise ValueError(
                    'El vector debe ser tridimensional')

            crossVector = []
            intVector = [o, o, o]

            if (not isinstance(self.vector[0], list)):
                crossVector.append(
                    self.vector[1] * intVector[2] - self.vector[2] * intVector[1])
                crossVector.append(
                    self.vector[2] * intVector[0] - self.vector[0] * intVector[2])
                crossVector.append(
                    self.vector[0] * intVector[1] - self.vector[1] * intVector[0])
                return Vector(crossVector)

            crossVector.append([
                self.vector[1][0] * intVector[2] - self.vector[2][0] * intVector[1]])
            crossVector.append([
                self.vector[2][0] * intVector[0] - self.vector[0][0] * intVector[2]])
            crossVector.append([
                self.vector[0][0] * intVector[1] - self.vector[1][0] * intVector[0]])
            return Vector(crossVector)

        # if not, we are multiplying two vectors
        if len(self.vector) != 3 or len(o.vector) != 3:
            raise ValueError(
                'Ambos vectores deben ser tridimensionales')

        if len(self.vector) != len(o.vector):
            raise ValueError(
                'Ambos vectores deben tener las mismas dimensiones')
        elif (isinstance(self.vector[0], list) and not isinstance(o.vector[0], list)) or (not isinstance(self.vector[0], list) and isinstance(o.vector[0], list)):
            raise ValueError(
                'Ambos vectores deben tener las mismas dimensiones (Uno es una columna y el otro es una fila)')

        crossVector = []
        if (not isinstance(self.vector[0], list) and not isinstance(o.vector[0], list)):
            crossVector.append(
                self.vector[1] * o.vector[2] - self.vector[2] * o.vector[1])
            crossVector.append(
                self.vector[2] * o.vector[0] - self.vector[0] * o.vector[2])
            crossVector.append(
                self.vector[0] * o.vector[1] - self.vector[1] * o.vector[0])
            return Vector(crossVector)

        crossVector.append([
            self.vector[1][0] * o.vector[2][0] - self.vector[2][0] * o.vector[1][0]])
        crossVector.append([
            self.vector[2][0] * o.vector[0][0] - self.vector[0][0] * o.vector[2][0]])
        crossVector.append([
            self.vector[0][0] * o.vector[1][0] - self.vector[1][0] * o.vector[0][0]])
        return Vector(crossVector)

    # dor product of two vectors
    def __mod__(self, o):
        # if we are multiplying a number to a vector
        if isinstance(o, int) or isinstance(o, float):
            mulVector = 0

            if (len(self.vector) == 0):
                return 0

            if (not isinstance(self.vector[0], list)):
                for i in range(len(self.vector)):
                    mulVector += self.vector[i] * o
                return mulVector

            for i in range(len(self.vector)):
                mulVector += self.vector[i][0] * o
            return mulVector

        if (len(self.vector) == 0):
            return 0

        # if not, we are multiplying two vectors
        if len(self.vector) != len(o.vector):
            raise ValueError(
                'Ambos vectores deben tener las mismas dimensiones')
        elif (isinstance(self.vector[0], list) and not isinstance(o.vector[0], list)) or (not isinstance(self.vector[0], list) and isinstance(o.vector[0], list)):
            raise ValueError(
                'Ambos vectores deben tener las mismas dimensiones (Uno es una columna y el otro es una fila)')

        dotVector = 0

        if (not isinstance(self.vector[0], list) and not isinstance(o.vector[0], list)):
            for i in range(len(self.vector)):
                dotVector += self.vector[i] * o.vector[i]
            return dotVector

        for i in range(len(self.vector)):
            dotVector += self.vector[i][0] * o.vector[i][0]
        return dotVector

    def __eq__(self, o):
        return self.vector == o.vector

    def __str__(self):
        if (len(self.vector) == 0):
            return "[]"

        strVector = "["


        for i in range(len(self.vector) - 1):
            strVector += str(self.vector[i]) + ", "
        strVector += str(self.vector[len(self.vector) - 1]) + "]"
        return strVector


    def __repr__(self):
        if (len(self.vector) == 0):
            return "[]"

        strVector = "["

        for i in range(len(self.vector) - 1):
            strVector += str(self.vector[i]) + ", "
        strVector += str(self.vector[len(self.vector) - 1]) + "]"
        return strVector
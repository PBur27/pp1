import random
class Arrays():

    @staticmethod
    def create(number, value):
        list = []
        for i in range(0, number):
            list.append(value)
        return list
    
    def createrand(number, m, n):
        list = []
        for i in range(0, number):
            list.append(random.randint(m,n))
        return list


arr = Arrays.create(5,2)
randarr = Arrays.createrand(8, 2, 8)

print(arr)
print(randarr)
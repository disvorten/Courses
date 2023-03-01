class Clasters:
    def __init__(self):
        self.cl = list(list())
    def add(self,mas):
        self.cl.append(mas)
    def amount(self):
        return len(self.cl)
    def printf(self):
        for row in self.cl:
            print(' '.join([str(elem) for elem in row]))

def main():
    cl = Clasters()
    with open('input.txt','r') as f:
        arr = [int(x) for x in next(f).split()]
        for line in f:
            mas = [int(x) for x in line.split()]

    N = arr[0];L = arr[1]
    temp = []
    temp.append(min(mas))
    mas.remove(min(mas))
    while(mas!= []):
        if(mas[mas.index(min(mas))]- temp[len(temp)-1] <= L):
            temp.append(min(mas))
            mas.remove(min(mas))
        else:
            var = temp.copy()
            cl.add(var)
            temp.clear()
            temp.append(min(mas))
            mas.remove(min(mas))
    if(len(temp) != 0):
        cl.add(temp)
    cl.printf()
    return cl

def printInF(cl):
    with open('output.txt', 'w') as f:
        f.write(str(cl.amount()))
        f.write('\n')
        for row in cl.cl:
            f.write(' '.join([str(elem) for elem in row]))
            f.write('\n')

cl = main()
printInF(cl)
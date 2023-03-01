class Graph:
    def __init__(self,N=1):
        self.gr = list(N*list())
    def add(self,mas,i):
        self.gr.insert(i,mas)
    def GetValue(self,i,j):
        return int(self.gr[i][j])
    def GetLen(self,i):
        return len(self.gr[i])
    def printf(self):
        for row in self.gr:
            print(' '.join([str(elem) for elem in row]))
class Mat:
    def __init__(self,N=1):
        self.mat = [[0] * N for i in range(N)]
    def change(self,i,j):
        self.mat[i][j] = 1
    def printf(self):
        for row in self.mat:
            print(' '.join([str(elem) for elem in row]))

def main():
    N = int(input())
    gr = Graph(N)
    for i in range(N):
        gr.add(input().split(),i)
    mat = Mat(N)
    for i in range(N):
        for j in range(gr.GetLen(i)):
            a = gr.GetValue(i,j)
            if(a>N or a<0):
                return
            elif(a==0):
                pass
            else:
                mat.change(i,a-1)
    mat.printf()

main()
"""
            mas.sort()
            temp = [mas[0]]
            for i in range(1,N):
                #print(temp)
                if(mas[i] - temp[0] <= L):
                    temp.append(mas[i])
                else:
                    var = temp.copy()
                    cl.add(var)
                    temp.clear()
                    temp.append(mas[i])
            if(len(temp) == 1):
                cl.add(temp)
            cl.printf()
"""
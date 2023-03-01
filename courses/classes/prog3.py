class Graph:
    def __init__(self,N=1):
        self.gr = list(N*list())
    def add(self,i,mas):
        self.gr.insert(i,mas)
    def printf(self):
        for row in self.gr:
            print(' '.join([str(elem) for elem in row]))
class Mat:
    def __init__(self,N=1):
        self.mat = [[0] * N for i in range(N)]
    def add(self,mas,i):
        self.mat.insert(i,mas)
    def GetValue(self,i,j):
        return int(self.mat[i][j])
    def printf(self):
        for row in self.mat:
            print(' '.join([str(elem) for elem in row]))

def main():
    N = int(input())
    mat = Mat(N)
    for i in range(N):
        mat.add(input().split(),i)
    gr = Graph(N)
    for i in range(N):
        mas = []
        for j in range(N):
            a = mat.GetValue(i,j)
            if(a>1 or a<0):
                return
            elif(a==0):
                pass
            else:
                mas.append(j+1)
        if(mas == []):
            gr.add(i,[0])
        else:
            gr.add(i,mas)
    gr.printf()

main()
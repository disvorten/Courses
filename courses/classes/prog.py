class Deck:
    def __init__(self):
        self.deck = list()
    def __str__(self):
        return f"{' '.join(str(x) for x in self.deck)}"
    def down(self,s):
        self.deck.append(s)
    def up(self,s):
        self.deck.insert(0,s)
    def fromDown(self):
        self.deck.pop()
    def fromUp(self):
        self.deck.pop(0)
    def GetLen(self):
        return len(self.deck)

def main():
    mas = []
    with open('input.txt', 'r') as f:
        for line in f:
            mas.append(line)

    deck = Deck()
    mas = [line.rstrip() for line in mas]

    for i in range(len(mas)):
        if (mas[i][0] == '+'):
            try:
                s = mas[i][1:3]
                deck.up(s)
            except IndexError:
                return('ERROR')
        elif (mas[i][0] == '#'):
            try:
                s = mas[i][1:3]
                deck.down(s)
            except IndexError:
                return('ERROR')
        elif (mas[i][0] == '^'):
            try:
                deck.fromUp()
            except IndexError:
                return('ERROR')
        elif (mas[i][0] == '/'):
            try:
                deck.fromDown()
            except IndexError:
                return('ERROR')

    if (deck.GetLen() == 0):
        return('EMPTY')
    else:
        return(deck)

def printf(deck):

    with open('output.txt','w') as f:
        if (deck == 'EMPTY'):
            f.write('EMPTY')
        else:
            s = f"{' '.join(str(x) for x in deck.deck)}"
            f.write(s)

deck = main()
printf(deck)

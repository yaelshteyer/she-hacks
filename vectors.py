from math import sqrt
repeat = 'Y'

class Vector(object):
    def __init__(self, letter, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self.letter = letter

    def __str__(self):
        return self.letter + ' = (' + str(self.a) + ',' + str(self.b) + ',' + str(self.c) + ')' 

    def create(self):
        for i in range(3):
            v = int(input('Enter dimension #' + str(i+1) + ':  '))
            vec.append(v)
    
    def magnitude(self):
        mag = sqrt(self.a**2 + self.b**2 + self.c**2)
        return round(mag,2)

    def addition(self, other):
        a = self.a + other.a
        b = self.b + other.b
        c = self.c + other.c
        return Vector(self.letter + '+' + other.letter, a, b, c)
    
    def subtraction(self, other):
        a = self.a - other.a
        b = self.b - other.b
        c = self.c - other.c
        return Vector(self.letter + '-' + other.letter, a, b, c)
    
    def dot_product(self, other):
        d = self.a * other.a + self.b * other.b + self.c * other.c
        return (self.letter + ' . ' + other.letter, d)

    def cross_product(self, other):
        a = self.b * other.c - self.c * other.b
        b = self.c * other.a - self.a * other.c
        c = self.a * other.b - self.b * other.a
        return Vector(self.letter + ' x ' + other.letter, a, b, c)

vecs=[]

while True:
    try:
        n = int(input("How many vectors would you like to make? "))
        if n > 0:
            break
    except:
        print("Invalid input. Please try again")

for j in range(n):
    letter = j + 117
    if letter > 122:
        letter -= 26
    dim = []
    print('\nVector #'+str(j+1))
    for i in range(3):
        while True:
            try:
                v = int(input('Enter dimension #' + str(i+1) + ':  '))
                dim.append(v)
                break
            except:
                print("Invalid input. Please try again")
    vec = Vector(chr(letter), dim[0], dim[1], dim[2])
    vecs.append(vec)
    
for i in range(len(vecs)):
    print('\n' + str(i + 1) + '.',vecs[i])


while repeat == 'Y':
    while True:
        try:
            s = input('\nSelect a task by typing in the matching letter: \na = magnitude\nb = vector addition\nc = vector subtraction\nd = dot product\ne = cross product\n').lower()
            if ord(s) > 96 and ord(s) < 102:
                break
        except:
            print("Invalid input. Please try again")
    if s == 'a':
        while True:
            try:
                vec1 = int(input('\nWhich vector would you like to use? (#) '))
                if vec1 > 0 and vec1 < (n + 1):
                    break
            except:
                print("Invalid input. Please try again")
                
        vec1 = vecs[vec1 - 1]
        print('|' + vec1.letter + '| = ',vec1.magnitude())
    else:
        if len(vecs) < 2:
            print('This task cannot be performed because only one vector was given')
        else:
            inps = []
            for i in range(2):
                while True:
                    try:
                        inp = int(input('\n'+ str(i + 1) + '. Which vectors would you like to use?'))
                        if inp < (n + 1) and inp > 0:
                            inps.append(inp - 1)
                            break
                    except:
                        print("Invalid input. Please try again")
                        
            if s == 'b':
                print(vecs[inps[0]].addition(vecs[inps[1]]))
            elif s == 'c':
                print(vecs[inps[0]].subtraction(vecs[inps[1]]))
            elif s == 'd':
                (v, r) = vecs[inps[0]].dot_product(vecs[inps[1]])
                print(v, '=', r)
            elif s == 'e':
                print(vecs[inps[0]].cross_product(vecs[inps[1]]))
    repeat = input('\nWant to go again? (Y/N) ').upper()

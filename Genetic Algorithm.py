print ("-------------------------Artificial Intelligence----------------------------")

import random
ulang1= 20
ind = []
pop=[]
pop1=[]
nilai=[]
nilai1=[]

def angka_biner():
    for i in range(3):
        a = []
        for j in range(3):
            x = random.randint(0, 1)
            a.append(x)
        ind.append(a)
    return ind
    print (ind)
            

def decode():
    ind = angka_biner()
    pop=[]
    for i in range(ulang1):
        pop1=[]
        print ("Individu ke-"+str(i))
        aa = (3-(-3)) / (2**(-1)+2**(-2)+2**(-3))
        bb = (ind[i][0]*(2**(-1))) + (ind[i][1]*(2**(-2))) + (ind[i][2]*(2**(-3)))
        x1 = -3 + (aa * bb)
        pop1.append(x1)
        print ("-nilai x1 = ", x1)
        #return x1
        cc = (2-(-2)) / (2**(-1)+2**(-2)+2**(-3))
        dd = (ind[i][3]*(2**(-1))) + (ind[i][4]*(2**(-2))) + (ind[i][5]*(2**(-3)))
        x2 = -2 + (cc * dd)
        pop1.append(x2)
        print ("-nilai x2 = ", x2)
        pop.append(pop1)

    return pop

def fitness(pop):
    y=pop
    nilai=[]
    for i in range(ulang1):
        x1=y[i][0]
        x2=y[i][1]
        print ("Individu ke-"+str(i))
        e = ((4-(2.1*x1**2)) + (x1**4)/3)
        f = (x1**2+(x1*x2))
        h = (-4+(4*x2**2)*x2**2)
        fn = e * f + h
        print ("   Nilai fitness = " , fn)
        nilai.append(fn)

    return nilai
 
def nilai_positif(nilai):
    m = max(nilai)
    ps1=[]
    for i in range(ulang1):
        print("nilai positif individu ke-"+str(i))
        n_positif = m - nilai[i]
        print(n_positif)
        ps1.append(n_positif)
    return ps1
        
def roulleteWheel(nilaiFitness):
    jumlah = sum(nilaiFitness)
    n_min = 0
    n_batas = random.uniform(0, jumlah)
    for i in range(ulang1):
        n_min += nilaiFitness[i]
        if (n_min >= n_batas):
            return i
        
def crossover (ot1, ot2):
    t_potong = 3
    for i in range(t_potong):
        ot1[i], ot2[i] = ot2[i], ot1[i]
    return ot1, ot2

def mutasi(child1, child2):
    total = 6
    for i in range(total):
        idx1 = random.uniform(0, 1)
        idx2 = random.uniform(0, 1)
        if (idx1 < 0.2):
            if(child1[i] == 1):
                child1[i]=0
            else :
                child1[i]=1
        if (idx1 < 0.2):
            if(child2[i] == 1):
                child2[i]=0
            else:
                child2[i]=1
    return child1, child2


satu=angka_biner()
print (satu)
dua=decode()
print (dua)
nilaiPositif = nilai_positif(fitness(dua))
print("NIlai fitness positif")
print(*nilaiPositif, sep="\n")
for i in range(ulang1) :
    ot1 = satu[roulleteWheel(nilaiPositif)].copy()
    ot2 = satu[roulleteWheel(nilaiPositif)].copy()
    print("*PARENT")
    print(ot1, ot2)
    print("*HASIL CROSSOVER")
    child1, child2 = crossover(ot1, ot2)
    print(child1, child2)
    child1, child2 = mutasi(child1, child2)
    print("*HASIL MUTASI")
    print(child1, child2)

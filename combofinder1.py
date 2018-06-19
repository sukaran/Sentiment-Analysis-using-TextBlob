import random 


Set=set([-12,3,4,5,6,-9,10,-19,-7,17])
SetSize=5
Resultlist=set()
iterations=10000




for i in range(iterations):
    Chromosome=tuple(random.sample(Set,SetSize))
    
    if sum(Chromosome)==0:
        Resultlist.add((Chromosome))
        
for r in Resultlist:
    print(r)
    
print("total sets\n",len(Resultlist))
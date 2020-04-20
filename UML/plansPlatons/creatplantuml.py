


import sys
from collections import defaultdict
import csv 

dirname="./UML/"

def makefile(actor,order,rows):
    with open(dirname+str(order)+"_"+actor+".du","w") as f :
        print("@startuml",file=f)
        print("",file=f)
        print("actor "+actor,file=f)
        for row in rows:
            if order>= int(row['order']) and actor==row['actor']:
                if row['UCLINK'] == "" :
                    print(row['actor']+" --> ("+row['UC']+") ",file=f)
                else:
                    print("("+row['UCLINK']+") <|-- ("+row['UC']+") : extends ",file=f)
        print("@enduml",file=f)

def makeactorsfile(actors):
    with open(dirname+"actors.du","w") as f :
        print("@startuml",file=f)
        print("",file=f)

        for actor in actors:
            print("actor "+actor,file=f)

        print("@enduml",file=f)


def makeGlobalfile(rows):
    s=set()
    with open(dirname+"global.du","w") as f :
        print("@startuml",file=f)
        print("",file=f)

        for row in rows:
            if row['actor'] not in s:
                s.add(row['actor'])
                print("actor "+row['actor'],file=f)
            if row['UCLINK'] == "" :
                 print(row['actor']+" --> ("+row['UC']+") ",file=f)
                 print("(login) <|-- ("+row['UC']+") ",file=f)
            else:
                print("("+row['UCLINK']+") <|-- ("+row['UC']+") : extends ",file=f)
        print("""
Utilisateur --|> AnalysteDidactitien
Membre --|> DirecteurScientifique
Utilisateur --|> Administrateur.Doyen
Utilisateur --|> Etudiant
Membre--|> President
Membre--|> Physionomiste
Membre--|> Enseignant
Utilisateur --|> Membre
""",file=f)
        print("@enduml",file=f)
    print("fichier "+dirname+"global.du créé" )

def createPlantUmlFromCsv(filename="concept.csv"):

    with open(filename,"r") as csvfile:
        reader=csv.DictReader(csvfile,delimiter='\t')
        rows=[row for row in reader]
        #print(rows)
    print("lecture terminé ")
    actors=set() 
    order= {}  
    actorUc= defaultdict(list)
    for row in rows:
        actors.add(row['actor'])
    makeGlobalfile(rows)
    #makeactorsfile(actors)
    #for a in actors:
        #makefile(a,4,rows)
    

def main(args):
    createPlantUmlFromCsv()
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))


sys.exit()

import string
def dijkstra(grafo,nodoPartenza,nodoArrivo):
    risultati=[]
    minore = 100 # un numero grande in modo da rendere verificata la selezione a riga 17
    for l1,l2,d in grafo:
        if l1==nodoPartenza and l2 ==nodoArrivo and d != -1:
            risultati.append((l1,l2,d))
        if l1==nodoPartenza and l2 ==nodoArrivo :
            for nodo1,nodo2,dist in grafo:
                if nodo1 == nodoPartenza and dist != -1 : 
                    tmpNodo = nodo2
                    ack = dijkstra(grafo,tmpNodo,nodoArrivo)
                    if ack is not None:
                        val = ack
                        risultati.append((l1,l2,val+dist))#distanza """
        for n in risultati:
            if(n[2] < minore):
                minore = n[2]
    return minore
def main():
    print ("Algoritmo di dijkstra !\n")
    numNodi=int(input("Quanti nodi vuoi inserire (max 26)  "))
    if numNodi > 26:
        print(" Scusa posso gestire al massimo 26 nodi ")
    else:
        lettere =string.ascii_lowercase[:26]
        grafo =[]
        for i in range(0,numNodi):
            for x in range(i,numNodi):
                if i != x:
                    dist = int(input("Inserire la distanza tra il nodo " + lettere[i]+ " e il nodo " + lettere[x]+" "))
                    grafo.append((lettere[i],lettere[x],dist))
        print ("Ok ho inserito i dati, eccoti il grafo ... \n")
        print([x for x in grafo])
        nodo1 = str(input("Inserisci il nome del primo nodo  "))
        nodo2 = str(input("Inserisci il nome del secondo nodo così calcolo la distanza  "))
        dist = dijkstra(grafo, nodo1,nodo2)
        print ( "Il costo del collegamento tra il nodo " + str(nodo1)+ " e il nodo " + str(nodo2) + " e' " + str(dist))
main() 

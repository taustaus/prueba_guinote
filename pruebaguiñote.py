#Programa de guiñote

import random as rd

#Crear una baraja y mezclar. El valor está ordenado. K = rey, J = sota, Q = caballo
valor = ["A", "3", "K", "J", "Q", "7", "6", "5", "4", "2"]
palo = ["O", "C", "E", "B"]
mazo = []
for j in palo:
    for i in valor:
        mazo.append(i+j)
rd.shuffle(mazo)

#Repartir 6 cartas a cada uno de los 4 jugadores
jugador = [[],[],[],[]]
for j in jugador:
    for i in range(6):
        j.append(mazo[0])
        mazo.remove(mazo[0])

#Definir la carta triunfo y su palo
carta_triunfo = mazo[0]
mazo.remove(mazo[0])
palo_triunfo = carta_triunfo[1]

#Definir quién sale
sale = rd.randrange(4)

#Definir tantos de la pareja par (jugadores 0 y 2) e impar (jugadores 1 y 3)
tantos = [0,0]

#Definir si se ha cantado en O, C, E, B
cantado = [False, False, False, False]

#Jugar las 4 bazas iniciales
baza = [[],[],[],[]]
for b in baza:
    #Cada jugador echa una carta
    for i in range(4):
        carta_jugada = rd.choice(jugador[(sale+i)%4])
        jugador[(sale+i)%4].remove(carta_jugada)
        b.append(carta_jugada)

        #Cada jugador roba una carta si hay cartas en el mazo, si no hay, roba la carta triunfo
        if len(mazo)>0:
            jugador[(sale+i)%4].append(mazo[0])
            mazo.remove(mazo[0])
        else:
            jugador[(sale+i)%4].append(carta_triunfo)
    
    #Analizar la baza para ver quién la gana
    gana = 0
    for i in range(1,4):
        #Si son del mismo palo, le ganan las que están antes en la escala de valor
        if b[gana][1] == b[i][1] and valor.index(b[gana][0]) > valor.index (b[i][0]):
            gana = i
        #Si no es de palo triunfo, le ganan las que sí son del palo triunfo
        if b[gana][1] != palo_triunfo and b[i][1] == palo_triunfo:
            gana = i

    #Sale el jugador que ha ganado la baza
    sale = (sale+gana)%4

    #Definir la pareja ganadora
    if sale == 0 or sale == 2:
        pareja = 0
    else:
        pareja = 1

    #Sumar tantos a la pareja ganadora
    for c in b:
        if c[0] == "A":
            tantos[pareja] = tantos[pareja] + 11
        elif c[0] == "3":
            tantos[pareja] = tantos[pareja] + 10
        elif c[0] == "K":
            tantos[pareja] = tantos[pareja] + 4
        elif c[0] == "Q":
            tantos[pareja] = tantos[pareja] + 2
        elif c[0] == "J":
            tantos[pareja] = tantos[pareja] + 3

    #Comprobar si la pareja ganadora canta con K y S del mismo palo si no se ha cantado antes. Suma 20, o 40 si es del palo de triunfo
    if pareja == 0:
        for j in [jugador[0],jugador[2]]:
            for c in j:
                if c[0] == "K":
                    for i in j:
                        if i[0] == "J":
                            if c[1] == i[1]:                           
                                if cantado[palo.index(c[1])] == False:
                                    if c[1] == palo_triunfo:
                                        tantos[pareja] = tantos[pareja] + 40
                                    else:
                                        tantos[pareja] = tantos[pareja] + 20
                                    cantado[palo.index(c[1])] = True        
    else:
        for j in [jugador[1],jugador[3]]:
            for c in j:
                if c[0] == "K":
                    for i in j:
                        if i[0] == "J":
                            if c[1] == i[1]:                           
                                if cantado[palo.index(c[1])] == False:
                                    if c[1] == palo_triunfo:
                                        tantos[pareja] = tantos[pareja] + 40
                                    else:
                                        tantos[pareja] = tantos[pareja] + 20
                                    cantado[palo.index(c[1])] = True
    print (sale)
    print (jugador)
    print (b)
    print (cantado)
    print(tantos)

print(palo_triunfo)

#Por hacer: jugar las 6 bazas de arrastre, cambiar el 7, contar las 10 últimas

# Classe che fornisce dei metodi per leggere randomicamente delle risposte
# ovvero singole linee di testo da un file

from random import randint
#answer_file=open('answers/why.answers', 'r')

class AnswerScan:

    def carica_risposte(answer_file):
        lista_risposte = []
        for line in answer_file.readlines():
            lista_risposte.append(line)

        print (lista_risposte)
        return lista_risposte

    def scegli_riposta(lista_risposte):
        rand = randint(0, len(lista_risposte)-1)
        print (rand)
        risposta = lista_risposte[rand]
        return risposta

    def genera_risposta(answer_file):
        risultato = scegli_riposta(carica_risposte(answer_file))
        return risultato

#print(risultato)
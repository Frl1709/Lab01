# Leggo le domande del file e restituisce un lista di oggetti domanda

import random
import operator
from domanda import Domanda


def leggiDomande(fileDaLeggere):
    domande = []
    with open(fileDaLeggere, 'r', encoding='utf-8') as file:
        lines = file.read().splitlines()
        for i in range(0, len(lines), 7):
            testo_domanda = lines[i]
            livello_difficolta = int(lines[i + 1])
            risposta_corretta = lines[i + 2]
            risposte_errate = lines[i + 3:i + 6]
            domande.append(Domanda(testo_domanda, livello_difficolta, risposta_corretta, risposte_errate))
    return domande


def gioca_trivia(domande):
    punteggio = 0
    livello_difficolta = 0
    while True:
        domanda = random.choice([d for d in domande if d.livello == livello_difficolta])
        lista_domande = domanda.stampa_domanda()
        risposta_utente = int(input("Inserisci il numero della risposta corretta: ")) - 1
        if risposta_utente >= 4:
            print("Inserire un numero da 1 a 4")
            risposta_utente = int(input("Inserisci il numero della risposta corretta: ")) - 1

        valore_risposta = lista_domande[risposta_utente]
        if domanda.verifica_risposta(valore_risposta):
            punteggio += 1
            livello_difficolta += 1
            print("Risposta corretta!")
            if livello_difficolta == max([domanda.livello for domanda in domande]) +1:
                break
        else:
            print(f"Risposta sbagliata! La risposta corretta era: {lista_domande.index(domanda.rispostaCorretta) + 1}")
            break
    return punteggio


def ordina_lista_di_tuple(lista_di_tuple):
    def chiave_ordinamento(tupla):
        return tupla[1]

    return sorted(lista_di_tuple, key=chiave_ordinamento, reverse=True)


def aggiornaPunteggi(fileDaLeggere, nickname, punteggio):
    with open(fileDaLeggere, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    str = {}
    for i in lines:
        line = i.strip().split()
        str[line[0]] = int(line[1])
    str[nickname] = punteggio
    sorted_items = sorted(str.items(), key=lambda x: x[1], reverse=True)
    with open(fileDaLeggere, 'w', encoding='utf-8') as file1:
        for nick in sorted_items:
            file1.write(f"{nick[0]} {nick[1]}\n")


if __name__ == "__main__":
    domande = leggiDomande("domande.txt")
    punteggio = gioca_trivia(domande)
    nickname = input("Inserisci il tuo nickname: ")
    aggiornaPunteggi("punti.txt", nickname, punteggio)
    print(f"Punteggio: {punteggio}")
    print(f"Nickname: {nickname}")

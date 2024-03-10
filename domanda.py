import random


class Domanda:
    def __init__(self, testo, livello, rispostaCorretta, risposteErrate):
        self.testo = testo
        self.livello = livello
        self.rispostaCorretta = rispostaCorretta
        self.risposteErrate = risposteErrate

    def stampa_domanda(self):
        print(f"Livello {self.livello}) {self.testo}")
        risposte_totali = self.risposteErrate[:]
        risposte_totali.append(self.rispostaCorretta)
        random.shuffle(risposte_totali)
        for i, risposta in enumerate(risposte_totali):
            print(f"        {i+1}. {risposta}")
        return risposte_totali

    def verifica_risposta(self, risposta_utente):
        if risposta_utente == self.rispostaCorretta:
            return True
        else:
            return False
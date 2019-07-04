from pyswip import *
from ast import *
class Prover:
    def __init__(self):
        self.prolog = Prolog()
        prolog.consult("prover.pl")

    def addLemma(self, lemma):
        prolog.query("addLemma({})".format(AST.stringify(lemma)))

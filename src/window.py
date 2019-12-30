from tkinter import *
from tkinter.scrolledtext import ScrolledText
import re

class MainView:
    def __init__(self):
        self.window = Tk()
        self.window.title("Prolog - python theorem prover")
        self.window.geometry('970x600')
        self.window.resizable(False, False)
        self.terms = []
        self.predicates = []

    def run(self):
        self.draw()
        self.window.mainloop()

    def draw(self):

        # Create widgets
        self.output = ScrolledText(self.window, width=130, height=30, state='disabled')
        self.forallButton = Button(self.window, text="forall", command=self.forallButton_Click)
        self.existsButton = Button(self.window, text="exists", command=self.existsButton_Click)
        self.andButton = Button(self.window, text="and", command=self.andButton_Click)
        self.orButton = Button(self.window, text="or", command=self.orButton_Click)
        self.notButton = Button(self.window, text="not", command=self.notButton_Click)
        self.impliesButton = Button(self.window, text="implies", command=self.impliesButton_Click)
        self.openParenthesisButton = Button(self.window, text="(", command=self.openParenthesisButton_Click)
        self.closeParenthesisButton = Button(self.window, text=")", command=self.closeParenthesisButton_Click)
        self.predicateButton = Button(self.window, text="predicate", command=self.predicateButton_Click)
        self.input = Entry(self.window,width=90, font="Calibri 12")
        self.addAxiomButton = Button(self.window, text="Add axiom", command=self.addAxiomButton_Click)
        self.addLemmaButton = Button(self.window, text="Add lemma", command=self.addLemmaButton_Click)
        self.showAxiomButton = Button(self.window, text="Show axiom", command=self.showAxiomButton_Click)
        self.showLemmaButton = Button(self.window, text="Show lemma", command=self.showLemmaButton_Click)
        self.cleanButton = Button(self.window, text="Clean", command=self.cleanButton_Click)
        self.proveButton = Button(self.window, text="Prove!", command=self.proveButton_Click)
        
        # Positioning the widgets 
        self.output.grid(column=0, row=0, padx=(20,20), pady=(20,20), columnspan=18)
        self.forallButton.grid(column=0, row=1, padx=(20,20), pady=(0,0), columnspan=2)
        self.existsButton.grid(column=2, row=1, padx=(20,20), pady=(0,0), columnspan=2)
        self.andButton.grid(column=4, row=1, padx=(20,20), pady=(0,0), columnspan=2)
        self.orButton.grid(column=6, row=1, padx=(20,20), pady=(0,0), columnspan=2)
        self.notButton.grid(column=8, row=1, padx=(20,20), pady=(0,0), columnspan=2)
        self.impliesButton.grid(column=10, row=1, padx=(20,20), pady=(0,0), columnspan=2)
        self.openParenthesisButton.grid(column=12, row=1, padx=(20,20), pady=(0,0), columnspan=2)
        self.closeParenthesisButton.grid(column=14, row=1, padx=(20,20), pady=(0,0), columnspan=2)
        self.predicateButton.grid(column=16, row=1, padx=(20,20), pady=(0,0), columnspan=2)
        self.input.grid(column=0, row=2, padx=(20,20), pady=(20,20), columnspan=18)
        self.showAxiomButton.grid(column=0, row=3, padx=(20,20), pady=(0,0), columnspan=3)
        self.showLemmaButton.grid(column=3, row=3, padx=(20,20), pady=(0,0), columnspan=3)
        self.addAxiomButton.grid(column=6, row=3, padx=(20,20), pady=(0,0), columnspan=3)
        self.addLemmaButton.grid(column=9, row=3, padx=(20,20), pady=(0,0), columnspan=3)
        self.cleanButton.grid(column=12, row=3, padx=(20,20), pady=(0,0), columnspan=3)
        self.proveButton.grid(column=15, row=3, padx=(20,20), pady=(0,0), columnspan=3)
        
        self.input.focus_set()

    def forallButton_Click(self):
        addQuantifierView = AddQuantifierView(self, 'forall', self.terms)
        addQuantifierView.run()

    def existsButton_Click(self):
        addQuantifierView = AddQuantifierView(self, 'exists', self.terms)
        addQuantifierView.run()

    def andButton_Click(self):
        self.write('and ')

    def orButton_Click(self):
        self.write('or ')

    def notButton_Click(self):
        self.write('not ')

    def impliesButton_Click(self):
        self.write('implies ')

    def openParenthesisButton_Click(self):
        self.write('(')
    
    def closeParenthesisButton_Click(self):
        self.write(')')

    def predicateButton_Click(self):
        addPredicateView = AddPredicateView()
        addPredicateView.run()

    def showAxiomButton_Click(self):
        pass
    
    def addAxiomButton_Click(self):
        pass
    
    def showLemmaButton_Click(self):
        pass

    def addLemmaButton_Click(self):
        pass

    def cleanButton_Click(self):
        pass

    def proveButton_Click(self):
        pass

    def write(self, formula):
        self.input.insert(END, formula)

class AddQuantifierView:
    def __init__(self, root, quantifier, terms):
        self.root = root
        self.window = Toplevel(root.window)
        self.window.title("Select Terms")
        self.window.geometry('375x320')
        self.window.resizable(False, False)
        self.quantifier = quantifier
        self.terms = terms

    def draw(self):
        # Create widgets
        self.newButton = Button(self.window, text="New", command=self.newButton_Click)
        self.termsList = Listbox(self.window, selectmode='multiple', width=30, height=15)
        self.termListScrollbar = Scrollbar(self.termsList, orient="vertical")
        self.okButton = Button(self.window, text="Ok", command=self.okButton_Click)
        self.cancelButton = Button(self.window, text="Cancel", command=self.cancelButton_Click)
        
        # Positioning the widgets 
        self.newButton.grid(column=0, row=0, padx=(20,20), pady=(20,20))
        self.termsList.grid(column=1, row=0, padx=(20,20), pady=(20,20), rowspan=5, columnspan=3)
        self.okButton.grid(column=1, row=5, padx=(20,20), pady=(0,0))
        self.cancelButton.grid(column=2, row=5, padx=(20,20), pady=(0,0))
        
        # Set the behavior
        self.termsList.insert(END, *self.terms)

    def run(self):
        self.draw()
        self.window.mainloop()

    def newButton_Click(self):
        newTermView = NewTermView(self)
        newTermView.run()
        
    def okButton_Click(self):
        itemList = ', '.join([self.termsList.get(item) for item in self.termsList.curselection()])
        self.root.write('{} {}. '.format(self.quantifier, itemList))
        self.window.destroy()

    def cancelButton_Click(self):
        self.window.destroy()

    def addTerm(self, term):
        self.terms.append(term)
        self.termsList.insert(END, *term)

class NewTermView:
    def __init__(self, root):
        self.root = root
        self.window = Toplevel(root.window)
        self.window.title("New Term")
        self.window.geometry('400x120')
        self.window.resizable(False, False)
        
    def draw(self):
        # Create widgets
        self.input = Entry(self.window,width=35, font="Calibri 12")
        self.okButton = Button(self.window, text="Ok", command=self.okButton_Click)
        self.cancelButton = Button(self.window, text="Cancel", command=self.cancelButton_Click)
        
        # Positioning the widgets 
        self.input.grid(column=0, row=0, padx=(20,20), pady=(20,20), columnspan=8)
        self.okButton.grid(column=3, row=5, padx=(20,20), pady=(0,0))
        self.cancelButton.grid(column=4, row=5, padx=(20,20), pady=(0,0))
        
        # Additional initial behavior
        self.window.bind('<Return>', self.okButton_Click)
        self.input.focus_set()

    def run(self):
        self.draw()
        self.window.mainloop()

    def okButton_Click(self):
        termsList = self.inspect(self.input.get())
        if(termsList):
            for term in termsList: 
                self.root.addTerm(term)
            self.window.destroy()
        else:
            messagebox.showerror('Error', 'The terms format are incorrect. Please try again.')
    
    def cancelButton_Click(self):
        self.window.destroy()

    def inspect(self, terms):
        unclosed = False
        string = ''
        for letter in terms:
            if letter == '(': 
                string += letter
                unclosed = True
            elif letter == ')':
                string += letter
                unclosed = False
            elif letter == ',' and not unclosed:
                string += ';'
            else:
                string += letter
        string = re.sub(' +', ' ',string)
        if string != '' and not unclosed:
            newTerms = string.split(';')
            finalList = []
            for newTerm in newTerms:
                print(newTerm)
                if not (newTerm == '' or newTerm in self.root.terms):
                    print('adentro')
                    finalList.append(newTerm)
            return newTerms
        else:
            return []
    
class AddPredicateView:
    def __init__(self):
        pass

    def run(self):
        pass
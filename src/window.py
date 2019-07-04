from tkinter import *
from tkinter.scrolledtext import ScrolledText

class Window:
    def __init__(self):
        self.window = Tk()
        self.window.title("Prolog - python theorem prover")
        self.window.geometry('800x600')
        self.window.resizable(False, False)


    def run(self):
        self.draw()
        self.window.mainloop()

    def draw(self):
        # Create the widgets
        self.output = ScrolledText(self.window, width=105, height=30)
        self.forallButton = Button(self.window, text="forall", command=self.forallButton_Click)
        self.existsButton = Button(self.window, text="exists", command=self.existsButton_Click)
        self.andButton = Button(self.window, text="and", command=self.andButton_Click)
        self.orButton = Button(self.window, text="or", command=self.orButton_Click)
        self.impliesButton = Button(self.window, text="implies", command=self.impliesButton_Click)
        self.openParenthesisButton = Button(self.window, text="(", command=self.openParenthesisButton_Click)
        self.closeParenthesisButton = Button(self.window, text=")", command=self.closeParenthesisButton_Click)
        self.predicateButton = Button(self.window, text="predicate", command=self.predicateButton_Click)
        self.input = Entry(self.window,width=75, font="Calibri 12")
        self.addAxiomButton = Button(self.window, text="Add axiom", command=self.addAxiomButton_Click)
        self.addLemmaButton = Button(self.window, text="Add lemma", command=self.addLemmaButton_Click)
        self.cleanButton = Button(self.window, text="Clean", command=self.cleanButton_Click)
        self.proveButton = Button(self.window, text="Prove!", command=self.proveButton_Click)
        

        # Positioning the widgets 
        self.output.grid(column=0, row=0, padx=(20,20), pady=(20,20), columnspan=8)
        self.forallButton.grid(column=0, row=1, padx=(20,20), pady=(0,0))
        self.existsButton.grid(column=1, row=1, padx=(20,20), pady=(0,0))
        self.andButton.grid(column=2, row=1, padx=(20,20), pady=(0,0))
        self.orButton.grid(column=3, row=1, padx=(20,20), pady=(0,0))
        self.impliesButton.grid(column=4, row=1, padx=(20,20), pady=(0,0))
        self.openParenthesisButton.grid(column=5, row=1, padx=(20,20), pady=(0,0))
        self.closeParenthesisButton.grid(column=6, row=1, padx=(20,20), pady=(0,0))
        self.predicateButton.grid(column=7, row=1, padx=(20,20), pady=(0,0))
        self.input.grid(column=0, row=2, padx=(20,20), pady=(20,20), columnspan=8)
        self.addAxiomButton.grid(column=0, row=3, padx=(20,20), pady=(0,0), columnspan=2)
        self.addLemmaButton.grid(column=2, row=3, padx=(20,20), pady=(0,0), columnspan=2)
        self.cleanButton.grid(column=4, row=3, padx=(20,20), pady=(0,0), columnspan=2)
        self.proveButton.grid(column=6, row=3, padx=(20,20), pady=(0,0), columnspan=2)
        
    def forallButton_Click(self):
        pass
    
    def existsButton_Click(self):
        pass
        
    def andButton_Click(self):
        pass

    def orButton_Click(self):
        pass

    def impliesButton_Click(self):
        pass
    
    def openParenthesisButton_Click(self):
        pass
    
    def closeParenthesisButton_Click(self):
        pass

    def predicateButton_Click(self):
        pass

    def addAxiomButton_Click(self):
        pass
    
    def addLemmaButton_Click(self):
        pass

    def cleanButton_Click(self):
        pass

    def proveButton_Click(self):
        pass
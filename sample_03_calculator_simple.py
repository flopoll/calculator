from tkinter import ttk, Tk, END

def buttonPlusClick():
    zahl1 = float (entry1.get())                #Zahl1 von Eingabefeld holen
    zahl2 = float (entry2.get())                #Zahl2 von Eingabefeld holen
    lErgebnis.config(text=str (zahl1+zahl2))    #Anzeige im Ergebnisfeld

def buttonMinusClick():
    zahl1 = float (entry1.get())                #Zahl1 von Eingabefeld holen
    zahl2 = float (entry2.get())                #Zahl2 von Eingabefeld holen
    lErgebnis.config(text=str (zahl1-zahl2))    #Anzeige im Ergebnisfeld

def buttonMultiplyClick():
    zahl1 = float (entry1.get())                #Zahl1 von Eingabefeld holen
    zahl2 = float (entry2.get())                #Zahl2 von Eingabefeld holen
    lErgebnis.config(text=str (zahl1*zahl2))    #Anzeige im Ergebnisfeld

def buttonDivideClick():
    zahl1 = float (entry1.get())                #Zahl1 von Eingabefeld holen
    zahl2 = float (entry2.get())                #Zahl2 von Eingabefeld holen    
    lErgebnis.config(text=str (zahl1/zahl2))    #Anzeige im Ergebnisfeld

def buttonModulorClick():
    zahl1 = float (entry1.get())                #Zahl1 von Eingabefeld holen
    zahl2 = float (entry2.get())                #Zahl2 von Eingabefeld holen    
    lErgebnis.config(text=str (zahl1%zahl2))    #Anzeige im Ergebnisfeld

def buttonClearClick():
    entry1.delete (0, last=END)
    entry2.delete (0, last=END)
    lErgebnis.config(text="")
    
#Root Fenster erstellen
root = Tk()

#Fenstertitel
root.title("Taschenrechner")

#Label
lZahl1 = ttk.Label(root, text="Zahl 1: ", background="red")
lZahl1.grid(row=0, column=0, padx=5, pady=5)                         #sticky=east,west,.. auch möglich

lZahl2 = ttk.Label(root, text="Zahl 2: ", background="red")
lZahl2.grid(row=2, column=0, padx=5, pady=5)

lErgebnisText = ttk.Label(root, text="Ergebnis: ", background="red")
lErgebnisText.grid(row=5, column=0, padx=5, pady=5)

lErgebnis = ttk.Label(root, text="", background="grey", width= 8)
lErgebnis.grid(row=5, column=1, padx=5, pady=5)

#Eingabefelder
entry1 = ttk.Entry(root, background="white", width=8)
entry1.grid(row=0, column=1, padx=5, pady=5)

entry2 = ttk.Entry(root, background="white", width=8)
entry2.grid(row=2, column=1, padx=5, pady=5)

#Operatoren-Buttons
bPlus = ttk.Button(root, text=" + ", width=2, command=buttonPlusClick)
bPlus.grid(row=0, column=2, padx=5, pady=5)

bMinus = ttk.Button(root, text=" - ", width=2, command=buttonMinusClick)
bMinus.grid(row=1, column=2, padx=5, pady=5)

bMultiply = ttk.Button(root, text=" * ", width=2, command=buttonMultiplyClick)
bMultiply.grid(row=2, column=2, padx=5, pady=5)

bDivide = ttk.Button(root, text=" : ", width=2,command=buttonDivideClick)
bDivide.grid(row=3, column=2, padx=5, pady=5)

bModulor = ttk.Button(root, text=" % ", width=2,command=buttonModulorClick)
bModulor.grid(row=4, column=2, padx=5, pady=5)

bClear =  ttk.Button(root, text=" C ", width=2, command=buttonClearClick)
bClear.grid(row=5, column=2, padx=5, pady=5)  

#mainloop-Methode zeigt auf das Root-Fenster; Fenster bleibt solange offen bis x gedrückt wird
root.mainloop()
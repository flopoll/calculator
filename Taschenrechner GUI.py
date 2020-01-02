from tkinter import ttk, Tk, END
#from tkinter import *
#Popup durch "messagebox"

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
    

def buttonSumClick():
    entry1.delete (0, last=END)
    entry2.delete (0, last=END)
    lErgebnis.config(text="")

#Root Fenster erstellen
root = Tk()

#Fenstertitel
root.title("Taschenrechner")

#Fenstergröße
root.geometry("800x500")

#Buttons
bPlus = ttk.Button(root, text=" + ", width=2, command=buttonPlusClick)
bPlus.grid(row=8, column=3, padx=5, pady=5)

bMinus = ttk.Button(root, text=" - ", width=2, command=buttonMinusClick)
bMinus.grid(row=7, column=3, padx=5, pady=5)

bMultiply = ttk.Button(root, text=" * ", width=2, command=buttonMultiplyClick)
bMultiply.grid(row=6, column=3, padx=5, pady=5)

bDivide = ttk.Button(root, text=" / ", width=2, command=buttonDivideClick)
bDivide.grid(row=5, column=3, padx=5, pady=5)

bClear = ttk.Button(root, text=" CE/C ", width=2, command=buttonClearClick)
bClear.grid(row=4, column=3, padx=5, pady=5)

bSum = ttk.Button(root, text=" = ", width=30, command=buttonSumClick)            ### !!!Summencommand muss noch definiert werden!!! ###
bSum.grid(row=9, column=1, padx=5, pady=5)


#Zahlen-Buttons
bEins = ttk.Button(root, text=" 1 ", width=2, command=buttonPlusClick)
bEins.grid(row=8, column=0, padx=5, pady=5)

bZwei = ttk.Button(root, text=" 2 ", width=2, command=buttonPlusClick)
bZwei.grid(row=8, column=1, padx=5, pady=5)

bDrei = ttk.Button(root, text=" 3 ", width=2, command=buttonPlusClick)
bDrei.grid(row=8, column=2, padx=5, pady=5)

#Eingabefelder
entry1 = ttk.Entry(root, background="white", width=30)
entry1.grid(row=0, column=1, padx=5, pady=5)


#mainloop-Methode zeigt auf das Root-Fenster; Fenster bleibt solange offen bis x gedrückt wird
root.mainloop()
##----------------
# Interface for Voting App (ThatSettlesIt!)
# Started: 16 June 2018
# B. Zurowski

import tkinter as tk
from tkinter import ttk
import pandas as pd
import votingAlgs

#to do: Create Voting GUI as class, then
#  instantiates
class ThatSettlesIt:
    def __init__(self, master):
        self.master = master
        master.title("ThatSettlesIt!")
        master.geometry('600x400')


#Click of button should execute voting_alg
def settleIt():
    winner=votingAlgs.choice("prefs.csv",algmenu.get())
    winnerResult.configure(text=winner)

#Click of ShowIt button shows data to the right
def showIt():
    pass
    # df1 = pd.read_csv("prefs.csv")
    # datadisplay.configure(text=pd.to_string())

#Setting up the layout and appearance of the GUI
root = tk.Tk()
gui = ThatSettlesIt(root)

#Choice of file to import for Preferences
filelabel = tk.Label(root,text="Preference File:")
filelabel.grid(column=0, row=0)
filebox = tk.Entry(root)
filebox.grid(column=1, row=0)

#Drop-down menu for Social Choice method
thelabel = tk.Label(root,text="Choice Method:")
thelabel.grid(column=0, row=1)
algmenu = ttk.Combobox(root)
algmenu['values'] = ('Plurality', 'Coombs', 'Runoff', 'Borda')
algmenu.grid(column=1, row=1)

#Result of social choice Algorithm
winnerLabel = tk.Label(root, text="Your winner is:")
winnerLabel.grid(column=0, row=3)
winnerResult = tk.Label(root, text="")
winnerResult.grid(column=1, row=3)

#Button to execute the social choice algorithm and
# pick a winner.
#!/usr/bin/env python3
settlebutton = tk.Button(root, text="SettleIt!", command=settleIt)
settlebutton.grid(column=1, row=2)

#Button to show our data (preferences)
datadisplay = tk.Label(root, text="")
displaybutton = tk.Button(root, text="Show me!", command=showIt)
displaybutton.grid(column=1, row=4)

root.mainloop()

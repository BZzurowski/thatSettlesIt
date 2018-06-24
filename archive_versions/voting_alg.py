# Program for Ranked Choice Voting Algorithms
# B. Zurowski
# November 2, 2017
# Last updated: 14 June 2018

# This is very dumb code!
# It does not handle ties
# It does not generalize to lists of any length (just 3)
# You CAN add more voters to the list, but must stick with ordering R C T
#   and follow the example.

# 1. Read in Ranked lists
# 2. Apply voting algorithm
# 3. Determine Results and Report

import numpy as np
import pandas as pd

#At present, lists must take R,C,T
prefframe = pd.read_csv("prefs.csv")
print(prefframe)

#---Begin Coombs function: does iterated elimination of most last-place votes.
def coombs(prefList):
    while(len(prefList[0])> 1):
        #Rounds elimination
        Tcount = 0
        Rcount = 0
        Ccount = 0
        # for each row, count number of last place votes for each candidate
        for row in prefList:
            if row[-1] == "T":
                Tcount += 1
            elif row[-1] == "R":
                Rcount += 1
            elif row[-1] == "C":
                Ccount += 1
    # Eliminate the candidate with highest number of last-place votes.
        # What if there's a tie?
    #Determine the candidate with most last place:
        if Tcount == max(Tcount, Rcount, Ccount):
            elim1 = "T"
        elif Rcount == max(Tcount, Rcount, Ccount):
            elim1 = "R"
        else: elim1 = "C"
    ###Eliminate them from each list in the prefList holder array:
        for row in prefList:
            for elem in row:
                if elem == elim1:
                    del row[row.index(elem)]
    return prefList[0][0]
#------End Coombs function-------

##----Plurality function: winner gets most first-place votes-----
def plurality(ballots):

    Tcount = 0
    Rcount = 0
    Ccount = 0
# for each row, count number of first place votes for each candidate
    for row in ballots:
        if row[0] == "T":
            Tcount += 1
        elif row[0] == "R":
            Rcount += 1
        elif row[0] == "C":
            Ccount += 1

###Determine the candidate with most first place:
    if Tcount == max(Tcount, Rcount, Ccount):
        winner = "T"
    elif Rcount == max(Tcount, Rcount, Ccount):
        winner = "R"
    else: winner = "C"

    return winner
###------end of Plurality Function--------------

##----Runoff Function: progressively eliminates choices with least first-place votes----
def runoff(ballots):

    while(len(ballots[0])> 1):
        #Rounds elimination
        Tcount = 0
        Rcount = 0
        Ccount = 0
        # for each row, count number of first place votes for each candidate
        for row in ballots:
            if row[0] == "T":
                Tcount += 1
            elif row[0] == "R":
                Rcount += 1
            elif row[0] == "C":
                Ccount += 1

        #print(Tcount, Rcount, Ccount)
    # Eliminate the candidate with highest number of last-place votes.
        # What if there's a tie?
    #Determine the candidate with most last place:
        if Tcount == min(Tcount, Rcount, Ccount):
            elim1 = "T"
        elif Rcount == min(Tcount, Rcount, Ccount):
            elim1 = "R"
        else: elim1 = "C"
        #print(elim1)
    ###Eliminate them from each list in the prefList holder array:
        for row in ballots:
            for elem in row:
                if elem == elim1:
                    del row[row.index(elem)]

        break
    return prefList[0][0]
#------End runoff function-------



# DATA:  Ranked Lists
inputList = [["R", "C", "T"],["R", "C", "T"],["R", "C", "T"],
    ["C", "R", "T"], ["C", "R", "T"], ["C", "R", "T"],
["T", "R", "C"], ["T", "C", "R"], ["T", "C", "R"], ["T", "C", "R"]]


#prefArray = np.asarray(inputList)

# We will apply Coombs rule algorithm to this list of lists
prefList = list(inputList)
coombsWinner = coombs(prefList)

#Declare the winner (we should have one candidate remaining
#there is a way to describe a condition to verify this, with row length
print("The Coombs winner is "+coombsWinner)


inputList = [["R", "C", "T"],["R", "C", "T"],["R", "C", "T"],
    ["C", "R", "T"], ["C", "R", "T"], ["C", "R", "T"],
["T", "R", "C"], ["T", "C", "R"], ["T", "C", "R"], ["T", "C", "R"]]

prefList2 = list(inputList)
pluralityWinner = plurality(prefList2)

print("The Plurality winner is "+pluralityWinner)

inputList = [["R", "C", "T"],["R", "C", "T"],["R", "C", "T"],
    ["C", "R", "T"], ["C", "R", "T"], ["C", "R", "T"],
["T", "R", "C"], ["T", "C", "R"], ["T", "C", "R"], ["T", "C", "R"]]

prefList3 = list(inputList)
runoffWinner = runoff(prefList3)

print("The Runoff winner is "+runoffWinner)

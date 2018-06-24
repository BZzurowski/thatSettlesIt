# Program for Ranked Choice Voting Algorithms
# B. Zurowski
# November 2, 2017
# Last updated: 17 June 2018

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
import random

#---Begin Coombs function: does iterated elimination of most last-place votes.
def coombs(prefData):
#we write for prefData in DataFrame format
    num_rows = prefData.shape[0]
    num_columns = prefData.shape[1]

    if (num_columns == 1):
        return prefData.iloc[0][0]
    else:
# Eliminate the candidate with highest number of last-place votes.
# What if there's a tie?
        elim = prefData.iloc[:,-1].value_counts().idxmax()
        reduced = prefData.replace(elim,np.nan)

#Create a new dataframe with the elim candidate missing
#Then pass that dataframe recursively to this function.
        shrunkArray = reduced.stack().values.reshape(num_rows, num_columns-1)
        shrunkData = pd.DataFrame(shrunkArray)
        return coombs(shrunkData)
#------End Coombs function-------

# ##----Plurality function: winner gets most first-place votes-----
def plurality(ballots):
#Determine the candidate with most first place:
    winner = ballots.iloc[:,0].value_counts().idxmax()
    return winner
# ###------end of Plurality Function--------------

# ##----Runoff Function: progressively eliminates choices with least first-place votes----
# PROBLEM HERE NOW

def runoff(ballots):
    num_rows = ballots.shape[0]
    num_columns = ballots.shape[1]

    if (num_columns == 1):
        return ballots.iloc[0][0]
    else:
        # Eliminate the candidate with lowest number of first-place votes
        # What if there's a tie? (There is!): Check for ties first
        #Step 1: Are there ties for last place?
        #What if someone gets ZERO votes?
        min_count = min(ballots.iloc[:,0].value_counts())
        losers = np.where(ballots.iloc[:,0].value_counts()==min_count)
        print(losers)
        loser = random.choice(losers)
        print(elim)
             #If ties:
        # else: #If no ties:
        #elim = ballots.iloc[:,0].value_counts().idxmin()
        elim = ballots.iloc[:,0].value_counts().loser
        #Continue now, ties broken and elim selected:
        reduced = ballots.replace(elim,np.nan)
        shrunkArray = reduced.stack().values.reshape(num_rows, num_columns-1)
        shrunkData = pd.DataFrame(shrunkArray)
        return runoff(shrunkData)
# #------End runoff function-------

#--------Counter function----------
# Provides counts of 1st, 2nd, 3rd place votes from
#   strict ranked choice ballots
def vote_counts(ballots):
    print(ballots)
    num_rows = ballots.shape[0]
    num_columns = ballots.shape[1]
    candidates = np.unique(ballots)
    counts = pd.DataFrame(index=candidates)
    #set counts data DataFrame
    for col in range(num_columns):
        counts[col] = ballots.iloc[:,col].value_counts()

    #format data to integers
    counts = counts.fillna(0).astype(int)
    return counts


#----Borda count Function
def borda(ballots):
    counts = vote_counts(ballots)
    print(counts)
    num_candidates = counts.shape[0]
    #initialize
    borda_count = pd.DataFrame(index=counts.index)
    borda_count[0] = 0
    print(borda_count)
    # Use points 3,2,1 if 3 candidates
    for col in range(num_candidates):
        borda_count[0] += (num_candidates-col)*counts.values[:,col]
        #print(borda_count)
    print(borda_count)
    winner = borda_count.idxmax().values[0]
    return winner
#----end Borda count

#---Single Transferable vote
def stv(ballots):
    return 0
#----end STV-------


def choice(filename, choice_method):
    prefframe = pd.read_csv("prefs.csv")
    preflist = pd.DataFrame(prefframe)
    print(preflist)
    if choice_method == 'Coombs':
        winner = coombs(preflist)
    elif choice_method == 'Plurality':
        winner = plurality(preflist)
    elif choice_method == 'Runoff':
        winner = runoff(preflist)
    else: #borda_count
        winner = borda(preflist)
    return winner

##Run through

#prefframe = pd.read_csv("prefs.csv")
#borda(prefframe)

# #At present, lists must take R,C,T
# print(prefframe)
# #prefframe serves as a "permanent" copy of the preferences
#
# # We will apply Coombs rule algorithm to this list of lists
# preflist = pd.DataFrame(prefframe)
# coombsWinner = coombs(preflist)
# print("The Coombs winner is "+coombsWinner)
#
# #Simple plurality winner (most first place votes)
# pluralityWinner = plurality(preflist)
# print("The Plurality winner is "+pluralityWinner)
#
# runoffWinner = runoff(preflist)
# print("The Runoff winner is "+runoffWinner)

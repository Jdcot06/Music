import csv
import random


csv = open("songs.csv")
if "Twenty One Pilots" in csv != True:
    csv = open("C:\Users\jdcot\OneDrive\Documents\GitHub\Music\songs.csv")
    if "Twenty One Pilots" in csv != True:
        csv = open("songs.csv","wt",newline="")
        csv.write(""""Artist","Song Name","Album","UK Release Date"
"Twenty One Pilots","Ride","Blurryface","11/04/2016"
"My Chemical Romance","Welcome to the Black Parade","The Black Parade","12/09/2006"
"Panic! At the Disco","I Write Sins Not Tragedies","A Fever You Can’t Sweat Out","27/02/2006"
"Electric Light Orchestra","Mr. Blue Sky","Out Of The Blue","28/01/1978"
"Isabelle Hyde","Stay Positive? In this Economy?","Embracing Entropy","24/05/2019"
"Eminem","The Real Slim Shady","The Marshall Mathers LP","18/04/2000"
"Michael Jackson ","Thriller","Thriller","30/11/1982"
"Grandson","Blood//Water","Blood//Water","27/10/2017"
"Ed Sheeran","Perfect","Divide","26/09/2017"
"Sophia Mills","Coffee Breath","All My Pals","27/08/2020"
"Craig David","Walking Away","Born To Do it","20/11/2000"
"Linkin Park","High Voltage","Hybrid Theory","26/01/2001"
"Twenty One Pilots","Redecorate","Scaled and Icy","20/05/2021"
"Cavetown","Sweet tooth","Sleepyhead","14/02/2020"
"Twenty One Pilots","Ode to Sleep","Regional at Best","08/07/2011"
"Nirvana","Smells Like Teen Spirit","Nevermind","10/09/1991"
"Prodigy","Smack My Bitch Up","Fat of the Land","17/11/1997"
"YUNGBLUD","Polygraph Eyes","YUNGBLUD","19/01/2018" """)

csv.readline(random.randint(1,max(csv)))

print(csv)

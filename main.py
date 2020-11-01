import datetime
day = datetime.datetime.now()
print(day.strftime("%A"))
from datetime import datetime
import webbrowser
import time

if day.strftime("%A") == "Sunday":
    with open('data/days/day1.txt', 'r') as day:
        print("today is sunday")
        links = day.readlines()      
elif day.strftime("%A") == "Monday":
    with open('data/days/day2.txt', 'r') as day:
        print("today is Monday")            
        links = day.readlines()      
elif day.strftime("%A") == "Tuesday":
    with open('data/days/day3.txt', 'r') as day:
        print("today is Tuesday")            
        links = day.readlines()  
elif day.strftime("%A") == "Wednesday":
    with open('data/days/day4.txt', 'r') as day:
        print("today is Wednesday")            
        links = day.readlines()     
elif day.strftime("%A") == "Thursday":
    with open('data/days/day5.txt', 'r') as day:
        print("today is Thursday")           
        links = day.readlines()    
elif day.strftime("%A") == "Friday": 
    with open('data/days/day6.txt', 'r') as day:
        print("today is Friday") 
        links = day.readlines()      
elif day.strftime("%A") == "Saturday":
    with open('data/days/day7.txt', 'r') as day:
        print("today is Saturday")
        links = day.readlines()

while True:
    now = datetime.now()
    current_time = now.strftime("%H:%M") #cals the time

    if current_time == "08:15":
        webbrowser.open(links[0])  #link 1
        time.sleep(120)  

    elif current_time == "09:00":
        webbrowser.open(links[1])  #link 2
        time.sleep(120)  

    elif current_time == "10:15":
        webbrowser.open(links[2])  #link 3
        time.sleep(120)  

    elif current_time == "11:00":
        webbrowser.open(links[3])  #link 4
        time.sleep(120)  
    
    elif current_time == "11:50":
        webbrowser.open(links[4])  #link 5
        time.sleep(120)

    elif current_time == "12:50":
        webbrowser.open(links[5])  #link 6
        time.sleep(120)  

    elif current_time == "13:40":
        webbrowser.open(links[6])  #link 7
        time.sleep(120)  

    elif current_time == "14:30":
        webbrowser.open(links[7])  #link 8
        time.sleep(120)  

    elif current_time == "16:00":
        webbrowser.open(links[8])  #link 9
        time.sleep(120)   

    elif current_time == "16:45":
        webbrowser.open(links[9])  #link 10
        time.sleep(120)

    elif current_time == "17:30":
        webbrowser.open(links[10])  #link 11
        time.sleep(120) 

    else:
        time.sleep(10) #end
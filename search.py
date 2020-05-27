#from typing import Dict, Any

import requests
import json
import maya

import cgitb
import cgi

cgitb.enable() #This will show any errors on your webpage

inputs = cgi.FieldStorage() #REMEMBER: We do not have inputs, simply a button to run the program. In order to get inputs, give each one a name and call it by inputs['insert_name']

print ("Content-type: text/html") #We are using HTML, so we need to tell the server

print #Just do it because it is in the tutorial :P

print ("<title> MyPythonWebpage </title>")

print ("Whatever you would like to print goes here, preferably in between tags to make it look nice")
#from operator import itemgetter, attrgetter, methodcaller
#from datetime import datetime, date, time


while True:
    user = input(str('Введите юзеркод :'))
    if user == 'q':
        break
    response = requests.get(
    'https://app.arenum.games/tournaments/matches?userCode=' + user + '&start=2020-05-01T00:00:00.000Z&end=2020-06-01T00:00:00.000Z')

    data = response.json()
    sorted_data= {}

    for match in data:
        dt = maya.parse(match['startedAt']).local_datetime()
        dt1= dt.strftime('%d-%m-%Y %H:%M')
        response1 = requests.get('https://app.arenum.games/tournaments/' + match['tournamentCode'])
        data1 = response1.json()
        data2 = data1['tournamentData']
        data3 = data2['name']
        sorted_data.update({match['tournamentCode']:dt1 +" " +data3})

    sort = sorted(sorted_data.items(),key=lambda p:p[1],reverse=False)
    for sorted_match in sort:
        if sorted_match == ' ':
            print('Данный пользователь не участвовал в турнирах')
        print(sorted_match)
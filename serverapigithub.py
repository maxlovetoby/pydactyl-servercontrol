from pydactyl import PterodactylClient
import json
import time
import os
import subprocess
import importlib


print("ATTEMPTING CONNECTION...")
# Create a client to connect to the panel and authenticate with your API key.
client = PterodactylClient('API ENDPOINT GOES HERE', 'API KEY GOES HERE')

# Get a list of all servers the user has access to
my_servers = client.client.list_servers()

# Get the unique identifier for the first server.
srv_id = my_servers[0]['identifier']
print("CONNECTION ESTABLISHED")

def panic():
        print("*********************************")
        print("***    PANIC MODE ACTIVATED   ***")
        print("*********************************")
        srv_utilization = client.client.get_server_utilization(srv_id)
        print(json.dumps(srv_utilization, indent=4))
        print("")
        print("")
        t = time.localtime()
        current_time = time.strftime("%H:%M:%S", t)
        print(current_time)
        print("")
        print("")
        print("Running Normal Shutdown")
        print("SENDING STOP COMMAND")
        print("")
        client.client.send_power_action(srv_id, 'stop')
        print("STOP COMMAND RECIVED")
        print("NORMAL SHUTDOWN ATTEMPT - TIME DELAY(5 SECONDS)")
        time.sleep(5)
        print("If the Server Has Shutdown normally, the kill command wont do anything")
        time.sleep(2.5)
        print("SENDING KILL COMMAND")
        print("")
        client.client.send_power_action(srv_id, 'kill')
        print("KILL COMMAND RECIVED")
        print("KILL COMMAND TIME DELAY(3 SECONDS)")
        print("PRINTING SYSTEM STATUS------------")
        srv_utilization = client.client.get_server_utilization(srv_id)
        print(json.dumps(srv_utilization, indent=4))
        print("SENDING START COMMAND")
        client.client.send_power_action(srv_id, 'start')
        print("START COMMAND SENT")
        print("Attempting to send to main menu")
        print("Opening Crash Protection Program")
        crashprot()

def crashprot():
        print("*********************************")
        print("***    CRASH PROTECTION OPEN  ***")
        print("*********************************")
        while True:
         time.sleep(3.6)
         dontcrash = client.client.get_server_utilization(srv_id)
         t = time.localtime()
         current_time = time.strftime("%H:%M:%S", t)
         print(current_time)
         print(dontcrash["cpu"]["current"])
         print("--------------")
         
         while dontcrash["cpu"]["current"] > 106.5:
                 print("******************************************")
                 print("******************************************")
                 print("***   AUTO CRASH PROTECTION - SERVERE  ***")
                 print("******************************************")
                 print("******************************************")
                 client.client.send_power_action(srv_id, 'kill')
                 print("*********************************")
                 print("***     KILL COMMAND SENT     ***")
                 print("*********************************")
                 panic()
         while dontcrash["cpu"]["current"] > 100:
                 print("*********************************")
                 print("***   AUTO CRASH PROTECTION   ***")
                 print("*********************************")
                 panic()
         while dontcrash["cpu"]["current"] > 86:
                 print("******************************************")
                 print("***   HIGH SERVER LOAD - CHECK SERVER  ***")
                 print("******************************************")
                 crashprot()
         while dontcrash["cpu"]["current"] < 0:
                 print("SERVER NOTICED OFFILINE, SENDING BOOT COMMAND")
                 print("SENDING START COMMAND")
                 print("")
                 client.client.send_power_action(srv_id, 'start')
                 print("START COMMAND RECIVED")
                 print("TIME DELAY(3 SECONDS)")
                 time.sleep(3)
                 print("---OPENING CRASH PROTECTION---")
                 print("")
                 crashprot()
        
        
                
                 
                 
                 
         
         
                

        

def menu():
        print ("")
        print("*****************************")
        print("***      SERVER - Menu    ***")
        print("*****************************")
        print("")
        print ("1. Turn On")
        print ("2. Turn Off")
        print ("3. Restart")
        print ("4. JSON Stats")
        print ("5. CLEAR ALL EFFECTS")
        print ("6. Raw Stats")
        print ("panic. Does a more authentic job of shutting down the server.")
        print ("kill. FORCE STOP")
        print ("7. Crash Protection")
        print ("kickall. KICKS ALL PLAYERS")
        adq2m = input("Please select")
        if adq2m == "1":
           print("SENDING START COMMAND")
           print("")
           client.client.send_power_action(srv_id, 'start')
           print("START COMMAND RECIVED")
           menu()
        if adq2m == "2":
            print("SENDING STOP COMMAND")
            print("")
            client.client.send_power_action(srv_id, 'stop')
            print("STOP COMMAND RECIVED")
            menu()
        if adq2m == "4":
           srv_utilization = client.client.get_server_utilization(srv_id)
           print(json.dumps(srv_utilization, indent=4))
           menu()
        if adq2m == "6":
           srv_utilization = client.client.get_server_utilization(srv_id)
           print(srv_utilization)
           menu()
        if adq2m == "5":
            client.client.send_console_command(srv_id, 'effect @a clear')
        if adq2m == "kill":
           print("SENDING KILL COMMAND")
           print("")
           client.client.send_power_action(srv_id, 'kill')
           print("KILL COMMAND RECIVED")
           menu()
        if adq2m == "3":
           restart()
        if adq2m == "panic":
                panic()
        if adq2m == "7":
           crashprot()
        if adq2m == "kickall":
           client.client.send_console_command(srv_id, 'kick @a All players have been kicked. Please rejoin as soon as possible.')
        

def restart():
        print("SENDING USER NOTICE")

        print("USER NOTICE SENT - WAITING 10 SECONDS")
        time.sleep(10)
        print("SENDING STOP COMMAND")
        print("")
        client.client.send_power_action(srv_id, 'stop')
        print("STOP COMMAND RECIVED")
        print("TIME DELAY (3 SECONDS)")
        time.sleep(3)
        print("SENDING START COMMAND")
        print("")
        client.client.send_power_action(srv_id, 'start')
        print("START COMMAND RECIVED")
        print("GOING TO MAIN MENU")
        time.sleep(1)
        print("")
        menu()
        

menu()



        

        

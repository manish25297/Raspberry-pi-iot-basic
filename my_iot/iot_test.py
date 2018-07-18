#import the requests library 
import requests

#to get the user input 
#=raw_input()

#to send the input value from requests library using get method
#requests.get("https://goutiest-workloads.000webhostapp.com/?bulb=on")
#requests.get("https://goutiest-workloads.000webhostapp.com/?temprature=56")
a=requests.get("https://goutiest-workloads.000webhostapp.com/bulb.txt")
print a.content
a1=requests.get("https://goutiest-workloads.000webhostapp.com/temprature.txt")
print a1.content

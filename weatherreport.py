import wttr
import requests

#take the user input for the city
city=input("enter city name")
print(city)

#displaying of the user inputted city
print("Displaying weather report for :" + city)

#fetching the weather report from the servers and getting the cities
url='https://wttr.in/{}'.format(city)
res=requests.get(url)

#printing the results
print(res.text)
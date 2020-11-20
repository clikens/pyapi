#!/usr/bin/env python3
import requests

def main():
  mytoken = 'EXAMPLE_REPLACE_ME_WITH_YOUR_CUSTOM_TOKEN'
  myapi = "https://fonoapi.freshpixl.com/v1/getlatest"
  mybuiltapi = myapi + "?token=" + mytoken
  
  ## ask user for a brand to search on
  brand = input("What brand of device are you searching for?")
  brand = "&brand=" + brand
  
  ## translate our JSON response to a series of Python lists and dictionaries
  myjson = requests.get(mybuiltapi + brand).json()
  
  ## Display a list of what inside our JSON
  for x in myjson:
    print(x)
  
if __name__ == '__main__':
  main()


#!/usr/bin/python3
import requests
import time


## Define NEOW URL 
NEOURL = "https://api.nasa.gov/neo/rest/v1/feed?"

def main():
    # datere = re.compile("\d{4}
    ## first I want to grab my credentials
    with open("/home/student/pyapi/nasa.creds", "r") as mycreds:
        nasacreds = mycreds.read()
    ## remove any newline characters from the api_key
    nasacreds = "api_key=" + nasacreds.strip("\n")        

    ## update the date below, if you like
    datein = input("start date (yyyy-mm-dd):  ").strip()
    
    ## the value below is not being used in this
    ## version of the script
    # enddate = "end_date=END_DATE"

    # make a request with the request library
    neodata = requests.get(NEOURL + datein + "&" + nasacreds).json()
    
    print(neodata)

    hazard = []
    astrodate = []
    astrodist = []

    for date in neodata['near_earth_objects'].keys():
        for astro in neodata['near_earth_objects'][date]:
            if astro['is_potentially_hazardous_asteroid']:
                print("HAZARD!!!")
                hazard.append(astro)
                astrodate.append(date)
                astrodist.append(astro['close_approach_data']['miss_distance']['miles'])

    if len(hazard) != 0:
        print(f"There were {len(hazard)} potentially hazardous asteroids near Earthdurint {datein}  time period")
        for x in range(0,len(astrodate)):
            print(f"Astro on {astrodate[x]}) was {astrodist[x]} miles away from Rarth.")
    else:
        print(f"No potentially hazardous asteroid were near Earth for {datein}.")







    # strip off json attachment from our response
    #neodata = neowrequest.json()

    ## display NASAs NEOW data
    print(neodata)

if __name__ == "__main__":
    main()



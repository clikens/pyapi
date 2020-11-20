#!/usr/bin/env python3
""" Author: RZFeeser || Alta3 Research
Gather data returned by various APIs published on OMDB, and cache in a local SQLite DB
"""

import json
import sqlite3
import requests

# Define the base URL
OMDBURL = "http://www.omdbapi.com/?"

# search for all movies containing string
def movielookup(mykey, searchstring):
    mtype = ['movie', 'series', 'episode']

    if searchstring in mtype:
        try:
            ## open URL to return 200 response
            resp = requests.get(f"{OMDBURL}apikey={mykey}&s={searchstring}")
            ## read the file-like object decode JSON to Python data structure
            return resp.json()
         except:
            return False

    try:
        ## open URL to return 200 response
        resp = requests.get(f"{OMDBURL}apikey={mykey}&s={searchstring}")
        ## read the file-like object decode JSON to Python data structure
        return resp.json()
    except:
        return False

def trackmeplease(datatotrack):
    conn = sqlite3.connect('mymovie.db')
    try:
        conn.execute('''CREATE TABLE IF NOT EXISTS MOVIES (TITLE TEXT PRIMARY KEY NOT NULL, YEAR INT  NOT NULL);''')

        # loop through the list of movies that was passed in
        for data in datatotrack:
            conn.execute("INSERT INTO MOVIES (TITLE,YEAR) VALUES (?,?)",(data.get("Title"), data.get("Year")))
            conn.commit()

        print("Database operation done")
        conn.close()
        return True
    except:
        return False

# Read in API key for OMDB
def harvestkey():
    with open("/home/student/omdb.key") as apikeyfile:
        return apikeyfile.read().rstrip("\n") # grab the api key out of omdb.key

def printlocaldb():
    pass
    #cursor = conn.execute("SELECT * from MOVIES")
    #for row in cursor:
    #    print("MOVIE = ", row[0])
    #    print("YEAR = ", row[1])


def main():

    print("Particulating Splines...")

    # read the API key out of a file in the home directory
    mykey = harvestkey()

    # initialize answer
    answer = "go"

    while True:
        answer = ""
        while answer == "":
            print("""\n**** Welcome to the OMDB Movie Client and DB ****
            ** Returned data will be written into the local database **
            1) Search for All Movies Containing String
            2) Search for TYPE: <movie|series|episode>
            99) Exit""")

            answer = input("> ")

        if answer == "1":
            searchstring = input("Search all movies in the OMDB. Enter search string: ").strip()
            resp = movielookup(mykey, searchstring)["Search"]
            if resp:
                # display the results
                print(resp)
                # write the results into the database
                trackmeplease(resp)
            else:
                print("That search did not return any results.")

        if answer =="2":
            searchstring = input("Search all movies by TYPE. movie, series, episode ").strip().lower()


        elif answer == "99":
            print("See you next time!")
            break

if __name__ == "__main__":
    main()


"""

    Title: pysports_queries
    Author: Robin Sebbag
    Date: 11/21/2021
    Description: Test program for executing queries in pysports database.

"""

# Import Statements
import mysql.connector
from mysql.connector import errorcode

config = {
    "user": "pysports_user",
    "password": "T1sPaS$w0rdsucks",
    "host": "localhost",
    "database": "pysports",
    "raise_on_warnings": True
}

try:
    """ try/catch block for handling potential MySQL database errors """ 

# Connect to the pysports database 
    db = mysql.connector.connect(**config) 

    cursor = db.cursor()

    # Select query from the team table 
    cursor.execute("SELECT team_id, team_name, mascot FROM team")

    # Get the results from the cursor object 
    teams = cursor.fetchall()

    print("\n  -- DISPLAYING TEAM RECORDS --")
    
    # Iterate over the teams data set and display the results 
    for team in teams: 
        print("  Team ID: {}\n  Team Name: {}\n  Mascot: {}\n".format(team[0], team[1], team[2]))

    # Select query for the player table 
    cursor.execute("SELECT player_id, first_name, last_name, team_id FROM player")

    # Get the results from the cursor object 
    players = cursor.fetchall()

    print ("\n  -- DISPLAYING PLAYER RECORDS --")

    # Iterate over the players data set and display the results
    for player in players:
        print("  Player ID: {}\n  First Name: {}\n  Last Name: {}\n  Team ID: {}\n".format(player[0], player[1], player[2], player[3]))

    input("\n\n  Press any key to continue... ")

except mysql.connector.Error as err:
    """ handle errors """

    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("  The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("  The specified database does not exist")

    else:
        print(err)

finally:
    """ Close the connection to MySQL """

    db.close()

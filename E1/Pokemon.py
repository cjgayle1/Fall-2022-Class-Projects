# File: Pokemon.py
# Description: Given 2 team rosters of Pokemon, remove duplicate matchups
#       Follow heuristics so that the resulting teams have strong Pokemon
#       Ensure resulting rosters are still the same size.
# Student Name: 
# Student UT EID: 
# Course Name: 
# Unique Number: 

from asyncio.windows_events import NULL
import sys

# DO NO EDIT THIS CLASS DEFINITION
class Pokemon(object):
    kind = ""
    strength = 0

    def __init__(self, kind, strength):
        self.kind = kind
        self.strength = strength

    def __str__(self):
        return "{" + self.kind + ", " + str(self.strength) + "}"


# Input: two lists a, b of Pokemon which are guaranteed to be the same length
# Output: nothing is returned. a, b are edited so that there are no Pokemon of
#  the same kind in the same index, and so that both have the same length.
#  Further rules are followed according to T1: Pokemon documentation.
def updateTeams(a, b):
    # YOUR CODE GOES HERE
    # Feel free to add helper functions as needed
    for i in range(len(a)):
        if(a[i].kind == b[i].kind):
            if(a[i].strength > b[i].strength):
                b[i] = NULL
            else:
                a[i] = NULL

    print("Missing Code in updateTeams")


# BE CAREFUL EDITING ANYTHING BELOW THIS LINE

# Input: list [string1, string2] representing kind, strength of a Pokemon respectively
# Precondition: string2 should be convertable to int
# Output: Pokemon initialized with the indicated kind and strength
def buildPokemon(t):
    return Pokemon(t[0], int(t[1]))

def main():
    # read in team size
    k = int(sys.stdin.readline().strip())

    # read in each team, convert to Pokemon
    # note that Pokemon kind may not include whitespace
    teamA = [buildPokemon(sys.stdin.readline().strip().split()) for i in range(k)]
    teamB = [buildPokemon(sys.stdin.readline().strip().split()) for j in range(k)]
    
    # update rosters according to given rules
    updateTeams(teamA, teamB)

    # output updated roster
    print("Team A Updated Roster:")
    for p in teamA:
        print(str(p))
    print("Team B Updated Roster:")
    for p in teamB:
        print(str(p))

if __name__ == "__main__":
    main()

#  File: Cipher.py

#  Description: This program provides defines a function for a partucular type of
# encryption and well as funciton which can decrypt it. 

#  Student Name: Kai Pang-Whitsett

#  Student UT EID:ktp577

#  Partner Name: Chris Gayle

#  Partner UT EID: cjg4283

#  Course Name: CS 313E

#  Unique Number: 52535

#  Date Created: 9/10/2022

#  Date Last Modified: 9/10/2022


import sys
import math as m




# Input: strng is a string of 100 or less of upper case, lower case, 
#        and digits
# Output: function returns an encrypted string 
def encrypt(string):
    s = len(string)
    M = m.ceil(m.sqrt(s))

# makes grid with letters (and asterisks when necessary)
    str_list_start = list(string) + ['*' for i in range(M ** 2 - s)]
    grid0 = [str_list_start[i:i + M] for i in range(M ** 2) if i % M == 0]
# flips elements of grid along horizontal axis
    grid1 = [row for row in grid0[::-1]]
# inverses the elements of the grid
    grid2 = [[grid1[i][j] for i in range(M)] for j in range(M)]
# creates 1D list out of rows of the transformed list then joins it to return a string
    '''
    print()
    print(grid2[0])
    print(grid2[1])
    print(grid2[2])
    print(grid2[3])
    print()
    '''
    str_list_final = [grid2[i][j] for i in range(M) for j in range(M) if grid2[i][j] != '*']
    return ''.join(str_list_final)




# Input: strng is a string of 100 or less of upper case, lower case, 
#        and digits
# Output: function returns an encrypted string 
def decrypt(string):
    s = len(string)
    M = m.ceil(m.sqrt(s))
    
# idk how to make this work properly
    '''
    grid0 = [['' for i in range(4)] for j in range(4)]
    i = 0
    for col in range(M)[::-1]:
        for row in range(M):
            
            if i < len(string):
                grid0[row][col] = string[i]
                i += 1
            else:
                grid0[row][col] = "*"


    print(grid0[0])
    print(grid0[1])
    print(grid0[2])
    print(grid0[3])
    print()
    '''
# inverses the elements of the grid
    grid1 = [[grid0[i][j] for i in range(M)] for j in range(M)]
# flips elements of grid along horizontal axis
    grid2 = [row for row in grid1[::-1]]

# creates 1D list out of rows of the transformed list then joins it to return a string
    str_list = [grid2[i][j] for i in range(M) for j in range(M) if grid2[i][j] != '*']
    return ''.join(str_list)



def test_cases():
    assert encrypt
def main():
    P = sys.stdin.readline().strip()
    Q = sys.stdin.readline().strip()
    
    print(encrypt(P))
    print(decrypt(Q))




if __name__ == "__main__":
    main()

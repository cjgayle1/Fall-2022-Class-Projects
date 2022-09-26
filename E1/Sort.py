# File: Sort.py  
# Description: Sort a string by occurrences of the characters.

# Student Name:
# Student UT EID:
# Course Name: CS 313E
# Unique Number:

# Input: any valid string
# Output: a string s in descending order based on the number of occurrences of the characters. Break ties of the same value by letting the character with the greater ASCII value come first 
import sys

def charFreq(s, char):
    count = 0
    for i in range(len(s)):
        if(s[i] == char):
            count += 1
    return[count, char]

def frequencySort(s):
    unique = set(s)
    chars = []
    for char in unique:
        chars.append(charFreq(s, char))

    sort = sorted(chars, key= lambda k: chars[0], reverse=True)

    # d = dict()
    # d[0] = []
    # print(d[0])
    # for i in range(len(chars)):
    #     d[chars[i][0]] = append(chars[i][1])

    # res = ""
    # for i in range(len(d)):
    #     d[i] = sorted(d[i], key= lambda k: ord(d[i][k]))
    #     for j in range(len(d[i])):
    #         res += d[i][j]


    # ordList = []
    # for i in range(len(chars)):
    #     ordList.append([chars[i][0],ord(chars[i][1]), chars[i][1]])

    # sort = sorted(ordList, key= lambda k: ordList[1], reverse=True)
    # sort = sorted(ordList, key= lambda k: ordList[0], reverse=True)
    # res = []
    # for i in range(chars[0] - 1):
    #     if(chars[i] == chars[i + 1]):
    #         if(ord(sort[i]) > ord(sort[i + 1]):
    #             res.append(sort[i])
    
    
    res = ""
    for i in range(len(sort)):
        for j in range(sort[i][0]):
            res += str(sort[i][1])

    res = res[::-1]

    return res

    # final = ""
    # for i in range(len(unique) - 1):
    #     if(chars[i][0] == chars[i+1][0]):
            
    # TODO: Implement me!
   
   
def main():
    #read the input file from stdin
    string = sys.stdin.readline().strip()
    while(string != ''):
        print(frequencySort(string))
        string = sys.stdin.readline().strip()


# This line above main is for grading purposes. It will not affect how
# your code will run while you develop and test it.
# DO NOT REMOVE THE LINE ABOVE MAIN
if __name__ == "__main__":
    main()


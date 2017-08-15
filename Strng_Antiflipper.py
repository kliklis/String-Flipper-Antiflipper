# -*- coding: utf-8 -*-
"""
String_flipper.py
@author: Kostas Klimantakis
"""

import os

#flipped chars
F_chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']+['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'v', 'W', 'X', 'Y', 'Z']+[' ','!','@','#','$','%','^','&','*','(',')','-','=','_','+','`','~',',','.','<','>','/','?','[',']','{','}','\\','|',';',':','\'','"']+['0','1','2','3','4','5','6','7','8','9']

#normal chars
N_chars = ['V', 'q', '>', 'p', '3', 'j', '6', 'y', '!', '1', 'K', '|', 'w', 'u', 'o', 'd', 'b', 'J', 's', 'l', 'n', '^', 'm', 'x', 'R', 'z']+['V', '8', '>', 'C', '3', 'J', '6', 'H', 'I', '1', 'K', '7', 'w', 'u', 'O', 'd', 'b', 'R', 'S', 'l', 'n', '^', 'm', 'X', 'λ', 'z']+[' ','i','@','#','$','%','v','&','.',')','(','_','=','-','+',',','~','`','*','>','<','\\','?',']','[','}','{','/','|',';',':',',',',,']+['0','τ','2','E','4','5','','L','8','6']

def Main():
    print("\nWelcome to Word_(anti)Flipper!")
    menu()
        
def menu():
    answer= input("\nDo you want to GIVE AN UNPUT (1), READ FROM A FILE (2) or EXIT (0) ? ")
    while answer!='1' and answer!='2' and answer!='0':
        answer= input("\nDo you want to GIVE AN UNPUT (1), READ FROM A FILE (2) or EXIT (0) ? ")

    if answer=='0':
        exit()
    elif answer=='1':
        answer='y'
        while answer=='y':
            input_str = input("\nGive the string you want to anti-flip: ")
            antiFlip(input_str)
    elif answer=='2':
        print("\n(The input file should be in this program's directory)")
        answer='y'
        while(answer=='y'):
            antiFlip(readProblem())
        
#returns the whole problem in a string
def readProblem():
    #opens the input file (file must be in the same dir)
    fname = input("\nGive the .txt file name:")
    
    while not os.path.exists(fname):
        print("File not found.PLease try again.")
        fname = input("File name:")
    infile = open(fname,"r")
    #starts reading from infile file
    mystr = infile.read()
    print(mystr)
    #close inflie
    infile.close()
    return mystr

def antiFlip(input_str):
    antiFlipped_str=''
    for i in input_str:
        ilch_flag=0
        j=0
        while (str(i)!=N_chars[j] and j<len(N_chars)):
            if j>=len(N_chars)-1:
                print("\n",i," is an illegal character!",sep="")
                ilch_flag=1
                break
            j=j+1
        if ilch_flag==0:
            position = j
            antiFlipped_str= str(F_chars[j]) + antiFlipped_str
    if ilch_flag==0:        
        print("\nThe anti-flipped string is:",antiFlipped_str)

    if ilch_flag==0:
        export2txt(antiFlipped_str)
    
    answer=''
    ans_c=0
    while answer!='y' and answer!='n':
        if ans_c==0: answer = input("\nDo you want to anti-flip another string? (y=YES,n=NO) ")
        elif ans_c==2: answer = input("\nAre you f*cking kinding me!?\nI SAID!..Do you want to anti-flip another string??? (y=YES,n=NO)")
        elif ans_c==5:
            answer = input("\nPlease press any key...AND GET YOUR A$$ OUTTA HERE!!!")
            exit()
        else: answer = input("\nI SAID!..Do you want to anti-flip another string?? (y=YES,n=NO)")
        ans_c=ans_c+1
    if answer=='n': Main()
    #elif answer=='y': Main()
        
    
    return ilch_flap

def export2txt(txt):
    answer=''
    while answer!='y' and answer!='n':
        answer=input("\nDo you want to export the anti-flipped string? (y=YES,n=NO)")
    if answer=='y':
        outfile = open("antiflipped_out.txt",'w')
        deleteContent("antiflipped_out.txt")
        outfile.write(txt)
        outfile.close()
        print("\nThe string has been exported successfully in antiflipped_out.txt!")

def deleteContent(f):
    with open(f, "w"):
        pass
    

if __name__ == '__main__':
    Main()

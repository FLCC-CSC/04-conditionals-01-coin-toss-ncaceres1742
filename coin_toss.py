# FILE NAME - coin_toss.py
# NAME: Norgie Caceres
# DATE: 10/03/2025
# BRIEF DESCRIPTION:  This script will randomly generate a coin toss and print out either heads or tails.


# 1. Make sure you fill out the comments above
# 2. Write your code in the proper spot
# 3. Be sure to answer the Reflection Questions and Attestation below
# 4. The Sample Output has been included in this code for your convenience
########## ENTER YER CODE BELOW THIS LINE ##########

import random

heads = 50


print("===== Coin Flipper =====")
coin_toss = random.randrange(0, 100)

if coin_toss  <= heads:
    print("Heads")
else:
    print("Tails")








########### END YER CODE ABOVE THIS LINE ###########


########################################
#          SAMPLE OUTPUT
########################################
'''
===== Coin Flipper =====
Heads
'''



'''
===== Coin Flipper =====
Tails
'''


########################################
#          REFLECTION QUESTIONS
########################################

'''

1. What was the hardest part of completing this lab? 

I struggled with finding a way to display the "Coin Flipper" output independently of the statement logic.
It was challenging to se[earate the print funcionality from the if/else statement.





'''

########################################
#            ATTESTATION
########################################
'''
It is critical in this class that you understand the concepts as we explore them because
those concepts are required understanding for entry level programming. Reliance on resources
like AI and internet sites like Chegg, CourseHero, StackOverflow, and general Google results
may impede your understanding. Please rate how well you understand the concepts in this lab: 
[ ] I understand very little about this lab.
[ ] I am about 50/50 on this lab; I get parts of it but not the whole picture.
[x ] I pretty much get it.
[ ] I'm solid. Totally got it.
'''

import random
import time
time.sleep(2)
n=random.randint(1,10)
print("The number is Locked ! Now Guess IT...".rjust(60," "))
c=3
while c!=0:
    a=int(input())
    if a==n:
        print(".....CONGRATULATIONS....".rjust(40," "))
        print("you won".rjust(30," "))
        break
    elif a>n:
        print("You are close a bit! But it Greater than the number")
        print("TRY AGAIN".rjust(30," "))
        print()
    else:
        print("You are close a bit! But it Lesser than the number")
        print("TRY AGAIN".rjust(30," "))
        print()
    c-=1
    if c==0:
        print()
        print("<<GAME OVER>>".rjust(35," "))
        print("SORRY!..BETTER LUCK NEXT TIME")

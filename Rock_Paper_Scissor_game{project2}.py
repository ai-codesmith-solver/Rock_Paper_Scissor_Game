import random
import pyfiglet


# Create ASCII banner
ban = pyfiglet.figlet_format("Rock Paper Scissor")


# Print in blue and yellow colour using ANSI escape code
BLUE = "\033[94m"
RESET = "\033[0m"
YELLOW = "\033[93m"
GREEN = "\033[92m"
RED = "\033[91m"
CYAN = "\033[96m"
MAGENTA = "\033[95m"

print(BLUE + ban + RESET)
print(YELLOW + "=" * 50)
print("       Welcome to Rock Paper Scissor Game!       ")
print("=" * 50 + RESET)



def game():
    print("""
Let's Start the game:
    Rock - R/r
    Paper - P/p
    Scissor - S/s     
    """)

    try_dic={"r":-1,"p":0,"s":1}
    rev_dict={-1:"Rock",0:"Paper",1:"Scissor"}

    you_score=0
    comp_score=0

    rounds = int(input(MAGENTA+"Enter how many rounds you want to play: "+RESET))
    while rounds<=0:
        print(RED+"\nInvalid Input"+RESET)
        rounds = int(input(MAGENTA+"\nEnter how many rounds you want to play: "+RESET))
        if rounds>=1:
            break


    for i in range(1,rounds+1):
        print()
        print(CYAN + f"--- Round {i} ---" + RESET)
    
        user_input=input("Enter your choice(R/P/S):").lower()
        while user_input not in try_dic: # for vaild input
            user_input = input("Invalid input! Please enter R, P, or S: ").lower()

        print()

        you=try_dic[user_input]
        computer=random.choice([-1,0,1])


    

        print(f"You chose: {rev_dict[you]}")
        print(f"Computer chose: {rev_dict[computer]}")
        print()
        
        #main logic

        if (computer==you):
            print(YELLOW + "It is a Draw!" + RESET)
            you_score+=1
            comp_score+=1
        else:
            if(computer==-1 and you==0):
                print(GREEN + "You won this round!" + RESET)
                you_score+=1

            elif(computer==-1 and you==1):
                print(RED + "You lost this round!" + RESET)
                comp_score+=1

            elif(computer==0 and you==-1):
                print(RED + "You lost this round!" + RESET)
                comp_score+=1

            elif(computer==0 and you==1):
                print(GREEN + "You won this round!" + RESET)
                you_score+=1

            elif(computer==1 and you==-1):
                print(GREEN + "You won this round!" + RESET)
                you_score+=1

            elif(computer==1 and you==0):
                print(RED + "You lost this round!" + RESET)
                comp_score+=1

            else:
                print("Something is wrong!")

        print()
        print("Scoreboard: ")
        print(f"Your score is: {you_score}")
        print(f"Computer score is: {comp_score}")
        

    # Final Summary
    print("\n" + YELLOW + "=" * 50 + RESET)
    print(CYAN + "        🎮 GAME OVER - FINAL RESULTS 🎮        " + RESET)
    print(YELLOW + "=" * 50 + RESET)
    print()
    print(f"Final Score: You= {you_score} | Computer= {comp_score}")
    print()
 
    #position check
    if you_score > comp_score:
        print(GREEN + "🎉 Congratulations! You are the Winner! 🎉" + RESET)
    elif comp_score > you_score:
        print(RED + "😢 Better luck next time! Computer wins." + RESET)
    else:
        print(YELLOW + "🤝 It's a Draw Overall!" + RESET)



    #Retry option 
    retry=input("\nDo you want to retry (Yes/No):  ").lower()

    if retry=="yes":
        game()
    else:
        print("Thnaks for playing! 👋")



game()# to satrt the program
    


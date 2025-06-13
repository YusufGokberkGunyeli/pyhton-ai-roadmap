print("GOD BLESS AMERICA THIS IS THE MAIN TERMINAL OF THE ROBCO")
import  time    
def countdown(message):
    i = 10
    while i != 0:
        print(f"{i}")
        i -= 1
        t = 1
        time.sleep(t)
        if i == 0:
            print(f"{message}")
while True:
    try:
        password = int(input("WHAT IS THE PASSWORD OF THE OVERSEER? "))
        if password == 12345:
            print("WELCOME HOME OVERSEER")
            break
        else:
            print("ACCESS DENIED. PLEASE TRY AGAIN")
    except ValueError:
        print("INVALID SYNTAX, ONLY NUMBERS ARE ALLOWED")

Q = str(input("HELLO WELCOME TO MAIN TERMINAL OF ROBCO MAY I HAVE YOUR NAME? "))
def operators():
    print("1. DESTROY THE WORLD")
    print("2. RELEASE THE CURE OF THE RADIATION THE WORLD  ")
    print("3. ACTIVATE ALL OF THE ROBCO ASSISTANTS")
    print("4. TELL THE STORY OF THE ROBCO")        
operators() 

Q2 = int(input(f"HELLO {Q} HOW ARE YOU, IS THERE ANYTHING I CAN DO FOR YOU? "))
if Q2 == 4:
    print("Robert House founded the company after he was cheated out of his inheritance by his brother. By 2047, thanks" \
    " to his business acumen, technical genius, and a Commonwealth Institute of Technology degree, it was one of the most"
    " profitable corporations on Earth. Its rise was aided by a Byzantine internal structure: The 27 year old House" \
    " deliberately structured the company like a maze, to obfuscate his role and allow RobCo to effectively hide" \
    " their practices. The company's aggressive expansion policies coupled with the high quality of their products" \
    " have given it a practical monopoly in crucial segments of the software market. By 2075, their Unified Operating System," \
    " MF Boot Agent, and RETROS BIOS were the de facto industry standard for terminals and mainframes across the 13" \
    " Commonwealths. Within a year, their RobcOS became the standard for military-grade security systems as well." \
    " Their broad range of robots, including the eyebot, protectron, and sentry bot lines were one of the most common" \
    " types of robotics before the War, rivaled only by General Atomics International's own product lines. In certain" \
    " fields, however, RobCo was unmatched. One of those was Robert Mayflower's Stealth Boy, reverse engineered" \
    "sometime between 2066 and 2077 from captured Chinese technology. Of course, the company was concerned about its" \
    " public image: A sinister megacorporation does not inspire confidence or loyalty. To educate the public and make" \
    " it friendlier to the American consumer, RobCo invested in exhibits and intense public relations campaigns, like" \
    " the joint RobCo/General Atomics exposition at the Museum of Technology.")
if Q2 == 1:
    print("1. YES")
    print("2. NO")
    Q3 = int(input("Are you sure? "))
    if Q3 == 1:
        print("STARING COUNTDOWN TO DESTROY THE WORLD")
        countdown("CONGRATULATIONS YOU DESTROYED THE WORLD")

if Q2 == 2:
    print("1 - ALL HEADQUARTES OF ENCLAVE")
    print("2 - ALL HEADQUARTES OF BOS")
    print("3 - ALL HEADQUARTES OF NCR")
    print("4 - ALL HEADQUARTES OF INSTITUTE")
    print("5 - NO I DON'T LOVE THEM")
    Q4 = int(input(("IS THERE ANY SPECIFIC PLACE YOU WANT TO CURE? ")))
    if Q4 == 1:
        countdown("CONGRATULATIONS ALL HEADQUARTES OF ENCLAVE ARE HEALED")

    elif Q4 == 2:
        countdown("CONGRATULATIONS ALL HEADQUARTES OF BOS ARE HEALED")

    elif Q4 == 3:
        countdown("CONGRATULATONS ALL HEADQUARTES OF NCR ARE HEALED")
    elif Q4 == 4:
        countdown("CONGRATULATONS ALL HEADQUARTES OF INSTITUTE ARE HEALED")
    elif Q4 == 5:
        countdown("HEALING ALL OVER THE WORLD INSTEAD OF THESE PLACES")
if Q2 == 3:
    print("ACTIVATING ALL OF THE ROBCO ASSISTANTS")
    print("PLEASE WAIT...")
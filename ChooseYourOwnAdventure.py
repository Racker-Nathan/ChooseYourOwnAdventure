import os
import time

def intro():
    os.system('cls')
    name = input('Hello!  This is a test of the intro screen!  Input your name!\n')
    step = "0"
    thebeginning(name, step)
    return

def thebeginning(name, step):
    step = "1"
    os.system('cls')
    choice = input('Please keep in mind ' + name + ' I\'m not a programmer by trade, so don\'t put in stupid answers or this thing will probably break. Answer with 1 2 or 3  Onwards!\n\n'
    'You wake up, the room is pitch black.  It\'s freezing cold, your toes like little icicles.  Your dog is asleep in it\'s bed. \n'
    'Your dog wakes up and runs to the door, barking wildly.  What do you do?\n\n'
    '1. Ignore it, stupid dog is just barking at the wind...\n'
    '2. Open the window and jump out, something\'s not right\n'
    '3. Follow your dog, he\'s a good boy and knows what\'s up\n\n'
    'Your Choice: '
    )
    if choice == "3":
        followthedog(name, step)
    elif choice == "2":
        imanidiot(name, step)
    elif choice == "1":    
        oblivious(name, step)
    else:
        errorcatch(name, step)
    return

def followthedog(name, step):
    step = "2"
    os.system('cls')
    choice = input('You get out of bed, arms reaching out feeling in front of you.  You reach the wall, feeling along until you get to the door.\n'
    'You reach out and open the door, it slowly squeaks open and your dog sprints off into the dark towards the front door, barking frantically\n'
    'As you walk down the hallway, you hear a large *THUD* from a room on the left.\n'
    'What do you do?\n\n'
    '1. Investigate the Thud\n'
    '2. Follow the dog, something\'s at the door\n'
    '3. Find your gun in the closet\n\n'
    'Your Choice: ')
    if choice == "3":
        exit
    else:
        errorcatch(name, step)
    return

def imanidiot(name, step):
    os.system('cls')
    print('Did you really just jump out the window?  Alright then.  You jump, you fall, you break a leg, you freeze to death, you die.\n\n'
    'GAME OVER\n\n'
    )
    time.sleep(5)
    gameover(name, step)
    return

def oblivious(name, step):
    return

def gameover(name, step):
    startover = input('Did you want to start over?\n'
    'y/N: '
    )
    if startover == "y":
        thebeginning(name, step)
    elif startover == "Y":
        thebeginning(name, step)
    elif startover == "N":
        print('Ok!  Goodbye!')
        time.sleep(2)
        exit
    elif startover == "n":
        print('Ok!  Goodbye!')
        time.sleep(2)
        exit
    else:
        os.system('cls')
        print('Please enter either y or N')
        time.sleep(2)
        gameover(name)

def errorcatch(name,step):
    os.system('cls')
    print('Something went wrong, and you ended up here ' + name + '.  Probably because you put something in that is not a 1 2 or 3.  Attempting to put you back where you were.')
    time.sleep(3)
    if step == "1":
        thebeginning(name,step)
    if step == "2":
        followthedog(name,step)
    else:
        exit

def main():
    intro()

main()

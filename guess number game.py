from random import shuffle
mylist=['','o','']
def shuffle_list(mylist):
   shuffle(mylist)
   return(mylist)
shuffle_list(mylist)
def player_guess ():
    guess=''
    while guess not in ['0','1','2']:
        guess=input("pick a number from 0,1,or 2:")
    return int(guess)
player_guess()

def check_guess(mylist,guess):
    if mylist[guess]== 'o':
        print("Correct")
    else:
        print("wrong!!")
        print(mylist)
mylist=['','o','']
mixedup_list=shuffle_list(mylist)
guess=player_guess()
check_guess(mixedup_list,guess)
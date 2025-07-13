from colorama import Fore
from os import *
from time import *

while True:
  
  data={}
  
  print(Fore.BLACK +"**************",Fore.CYAN+"Welcome to Silent Auction Program",Fore.BLACK +"**************")
  
  while True:
  
    print()
    
    name=input(Fore.RESET+"Enter your name: ")
    print()
    bid=int(input("Enter your Bid: "))
    print()
    data[name]=bid
  
    rerun=input("Are there any more bidders?[yes/no]\n")
    
    system("clear")
    
    if rerun=='yes':
      continue
    elif rerun=='no':
      break
    else:
      print()
      print('Error!!!!!')
  
  bids=[]

  print()
  print("Here is the list of bidders:\n")
  print(data)
  sleep(4)
  
  for i in data:
    bids.append(data[i])
  
  max_bid=max(bids)
  
  system('clear')
  sleep(1)
  print()
  print("Analizing Bids..........")
  
  sleep(3)
  system('clear')
  print()
  print("Finding Winner..........")
  sleep(5)
  print()
  
  for i in data:
    if max_bid==data[i]:
      print(f"The Winner of Silent Auction is {i} with a bid of {max_bid}")
      break
  
  print()
  print()
  
  print(Fore.BLACK + "*********",
        Fore.BLUE + "Thanks for playing the Silent Auction",
        Fore.BLACK + "*********")
  
  print()
  
  print(Fore.BLACK + "***********",
        Fore.LIGHTBLUE_EX + "Developer is Tejvir Chauhan",
        Fore.BLACK + "***********")

  re_auctioned=input("You want to play one  more auction[y/n]: ")

  if re_auctioned=='Y' or re_auctioned=='y':
    continue
  else:
    print("Good Bye")
    break

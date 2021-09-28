#!/usr/bin/python3

import random
from progress.bar import Bar

#Simulate a coin flip process
def coin():
  coin_value = random.randint(1,2) 
  if coin_value == 1: 
    return "head"
  else: 
    return "tail"

# Flip this coin 10 times
def flip_10_coins(): 
  lst = []
  for i in range(0,10):
    res = coin()
    lst.append(res)
  return lst

# Flip this coin 10 times -- method #2
def flip_10_coins_2():
  lst = []
  counter = 0
  while counter < 10:
    res = coin()
    lst.append(res)
    counter += 1
  return lst


# Flip this coin n times
def flip_N_coins():
  n = int(input("how many times you want to flip this coin --> ")) 
  lst = []
  counter = 0
  while counter < n:
    res = coin()
    lst.append(res)
    counter += 1
  return lst

# Flip until we have 10 HEADS
def ten_heads(): 
  
  num_heads = 0
  num_tails = 0
  counter = 0
  while num_heads < 10: 
    res = coin()
    counter += 1
    if res == "head":
      num_heads += 1
    else:
      num_tails += 1 

  print("you have %d heads, and %d tails, and you flipped %d times" %(num_heads, num_tails, counter))
  return num_heads, num_tails, counter

# Flip the coin until you have 10 heads in a row
def ten_heads_streak():
  streak_head = 0
  counter = 0
  while streak_head < 10:
    counter += 1
    res = coin()
    if res == "head":
      streak_head +=1
    else: 
      streak_head = 0
  print(f"you have flipped {counter} times\nyou have {streak_head} heads")
  return counter

# Flip the coin until you have N streaks either heads or tails; 
def N_streaks():
  n = int(input("how many streaks do you need? --> "))
  streak_head = 0
  streak_tail = 0
  counter = 0
  while streak_head < n  and streak_tail < n: 
    res = coin()
    print(res)
    if res == "head":
      streak_tail = 0
      streak_head += 1
      counter +=1
    else:
      streak_head = 0
      streak_tail +=1
      counter +=1
  print("you have flipped the coin %d times" %counter) 
  print(f"you get a streak heads of {streak_head}")
  print(f"you get a streak tails of {streak_tail}")
  return counter 

if __name__ == "__main__":
  try:
    while True:
      print("="*30)
      print("0, Flip 1 coin")
      print("1. Flip 10 times")
      print("2. Flip n times")
      print("3. Ten heads")
      print("4. Ten HEADS streak")
      print("5. N HEADS Streak")
      usr_input = int(input())
      print("Selection:%d" %(usr_input))
      print("="*30)
     
      if usr_input == 0:
        print(coin())
      if usr_input ==1:
        print(flip_10_coins())
      elif usr_input == 2:
        print(flip_N_coins())
      elif usr_input == 3:
        print(ten_heads())
      elif usr_input == 4:
        print(ten_heads_streak())
      elif usr_input == 5:
        print(N_streaks())
      else:
          with Bar('flipping:', max = 10) as bar: 
             print(N_streaks())
             bar.next()
  except ValueError:
    print("Input not valid") 

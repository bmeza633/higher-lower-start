from game_data import data
import random
from art import logo, vs
from replit import clear
top_score = 0
def pick_random():
  """Picks a random choice from the data and returns it"""
  return random.choice(data)

def compare(follow_a, follow_b):
  """This function compares the followers of both options and returns the option letter."""
  if follow_a > follow_b:
    return "a"
  elif follow_a < follow_b:
    return "b"
  else:
    return "Error"


  
def game():
  option_a = pick_random()
  option_b = pick_random()
  score = 0
  end_of_game = False
  while end_of_game == False:
  #Pick one random keys and assign one to A 
  
    name_a = option_a["name"]
    follow_a = option_a["follower_count"]
    description_a = option_a['description']
    country_a = option_a['country']
    
    # Pick one random key and assign it to B
    
    name_b = option_b["name"]
    follow_b = option_b["follower_count"]
    description_b = option_b['description']
    country_b = option_b['country']
    #Display both options

    #code below is here to prevent picking the same thing twice so you compare the same thing.
    if name_a == name_b:
      option_b = pick_random()
      name_b = option_b["name"]
      follow_b = option_b["follower_count"]
      description_b = option_b['description']
      country_b = option_b['country']
      
    #Ask after displaying B if it is lower or higher in followers
    print(logo)
    print(f"""Compare A: {name_a}, a {description_a}, from {country_a}. """)
    print(vs)
    print(f"""Against B: {name_b}, a {description_b}, from {country_b}. """)

    
    asking = input("Who has more followers? Type 'A' or 'B': ").lower()
    winner = compare(follow_a, follow_b)

    # The code below compares our choice with the answer of who is greater. Using 'a' and 'b' as the comparison methods.
    # example asking I say 'a' winner launches compare function which compares a and b to see which is greater and returns the letter if the letter is 'a' then asking and winner are equal if 'b' has more than the statement is false and you lose.
    
    if asking == winner:
      score += 1
      clear()
      print (f"Thats right. Score is:{score} ")
      option_a = option_b
      option_b = pick_random()
      
    
      # print(option_a)
      # print(option_b)
    else:
      clear()
      print (f"Sorry thats wrong. Final Score:{score} ")
      again = input("Would you like to play again? type 'y' or'n': ")
      end_of_game = True
      if again == "y":
        clear()
        game()
      else:
        print("Gameover... ")
        
  
    
    # If wrong end game there and display score
  
  # if correct add one to score

game()

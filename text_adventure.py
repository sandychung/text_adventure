
print("You are a poor single mother living in America.")

def wait_for_enter(text):
    user_input= input(text)

user_input = input("Your child is sick. Do you want to go to the hospital or keep her at home? ")
if user_input == "hospital":
    wait_for_enter("she gets medicine")
    wait_for_enter("she gets better")
    wait_for_enter ("Your daughter will have to get a job to pay medical expenses")

elif user_input == "home":
    wait_for_enter("she gets her medicine")
    wait_for_enter("She eventually gets worse and dies")
    wait_for_enter ("You pay for funeral expenses")
print("you are even more poorer than before ")
print("one day later")
print ("your boss has seen your dedication to your work")
    wait_for_enter("Do you go to the mall or go to the bank?")
if user_input == "mall":
    wait_for_enter("you get yourself a pair of new boots")
if user_input == "bank":
    wait_for_enter(" you get robbed and loose your month's salary")

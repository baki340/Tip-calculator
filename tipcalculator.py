print("Welcome to the tip calculator!")

bill = float(input("What was the total bill?\n$"))

tip_percent = int(input("how much tip percent would you like to give? 10, 12, 15\n"))

people = int(input("How many people to split the bill?\n"))

tip = bill / tip_percent
total = tip + bill
final = total / people
print(f"Each person should pay: ${final}")  #made by baki

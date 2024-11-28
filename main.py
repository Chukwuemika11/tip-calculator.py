print("Welcome to the tip calculator")
total_Bill = float(input("What was the total bill ?\n"))

getBill = total_Bill
print(getBill)

per_tip = int(input("How much tip would you like to give? 10, 20, or 15\n"))

getTip = per_tip
print(getTip)

percentageTip = getTip / 100 * getBill + getBill
print(f" percentage tip is {percentageTip}")

per_split = int(input("How many people should split the bill?\n"))
per_person = per_split

split_tip =  percentageTip / per_person
final_amount = round(split_tip, 2)
print (f" I think each person should pay ${final_amount}")

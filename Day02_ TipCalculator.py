print("Welcome to the Tip Calculator!")
total_bill = float(input("What was the total bill? $"))
tip_percentage= int(input("How much tip would you like to give? 10,12 or 15"))
split_count= int(input( "How many people to split the bills?"))

tip_amount = total_bill * (tip_percentage/100)
total_amount = total_bill + tip_amount
amount_per_person = total_amount/ split_count

print(f"Each person should  pay: $ {amount_per_person}")

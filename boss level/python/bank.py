saved_money = int(input("how much money is in your bank account: "))
added_money = int(input("how much money do you whant to add: "))
money_now = saved_money + added_money
money_i_whant_to_take = int(input("how much money do yo whant to take: "))
if money_i_whant_to_take > money_now:
  print("sorry you dont have enough money")
else:
  print("your ballance is " + str(money_now - money_i_whant_to_take) + "$")

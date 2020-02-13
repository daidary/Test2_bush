print("Hello Daidary_GitHub" + '\n' + "Welcome, Timur ")
error_choice = "Error input, Enter y or n again! "
a = input("Would you like this test? ")
print("Тут новая строчка второй версии")

while a  not in ("y", "n"):

	if a == "y":
	   print("well, glad you see")
	elif a == "n":
	   print("sorry, will improve your experience in feature")
	else:
	   print("\n" + error_choice + "\n")
	   a = input("Would you like this test?(y\\n): ")

print("Здесь новые изменения второй версии")
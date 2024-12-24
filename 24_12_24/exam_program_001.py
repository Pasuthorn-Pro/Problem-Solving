money = int(input("Enter money you want to deposit: "))
year = int(input("Enter how many years do you want to deposit: "))
method = input("Choose a deposit method (day/month/year): ")

if method == "day":
    deposit_day = money / (year * 365)
    print(f"You have to deposit {deposit_day}")

if method == "month":
    deposit_month = money / (year * 12)
    print(f"You have to deposit {deposit_month}")

if method == "year":
    deposit_year = money / year
    print(f"You have to deposit {deposit_year}")

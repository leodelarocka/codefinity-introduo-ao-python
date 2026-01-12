# List of products on promotion for each weekday
daily_promotions = ["Milk", "Eggs", "Bread", "Apples", "Oranges"]

# List of weekdays corresponding to the promotions
weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

for t in range(len(weekdays)):
    weekday = weekdays[t]
    promotion = daily_promotions[t]
    print(f"{weekday}: Promotion on {promotion}")
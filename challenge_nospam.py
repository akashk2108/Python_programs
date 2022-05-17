menu = [
    ["egg", "bacon"],
    ["egg", "sausage", "bacon"],
    ["egg", "spam"],
    ["egg", "bacon", "spam"],
    ["egg", "bacon", "sausage", "spam"],
    ["spam", "bacon", "sausage", "spam"],
    ["spam", "sausage", "spam", "bacon", "spam", "tomato", "spam"],
    ["spam", "egg", "spam", "spam", "bacon", "spam"],
]
for meal in menu:
    if "spam" in meal:
        for i in range(len(meal)-1,-1,-1):
           if meal[i] is "spam":
               meal.remove(meal[i])
        print(meal)
    else:
        print(meal)
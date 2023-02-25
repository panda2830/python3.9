pasta = "tomato, basil, garlic, salt, pasta, olive oil"
apple_pie = "apple, sugar, salt, cinnamon, flour, egg, butter"
ratatouille = "aubergine, carrot, onion, tomato, garlic, olive oil, pepper, salt"
chocolate_cake = "chocolate, sugar, salt, flour, coffee, butter"
omelette = "egg, milk, bacon, tomato, salt, pepper"
menu = {"pasta time!": pasta, "apple pie time!": apple_pie, "ratatouille time!": ratatouille,
        "chocolate cake time!": chocolate_cake, "omelette time!": omelette}
food = input()
for i, j in menu.items():
    if food in j:
        print(i)

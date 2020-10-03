hats = {
    "snapback": 10, 
    "beanie": 5,
    "baseballcap": 3

}

hats.update({"weird top hat" : 1})

print(hats)

hats["snapback"] += 1

print(hats)

del hats['weird top hat']

print(hats)
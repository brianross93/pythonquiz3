sports = ["basketball", "softball", "football", "baseball", "track"]

with open("sports.txt", "w") as sport_list:
    for sport in sports:
        # for each sport in the list of sports, we write the sport and a new line
        # we then print to console, and it is also in the sports.txt file
        sport_list.write(sport)
        sport_list.write("\n")
        print(sport)

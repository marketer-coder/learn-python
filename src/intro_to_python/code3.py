#You are making a game! The player tries to shoot an object and can hit or miss it.
#the player starts with 100 points, with a hit adding 10 points to the player’s score, and a miss deducting 20 points.

#Your program needs to take 4 action results as input ("hit" or "miss"), calculate and output the player’s remaining points.

#your code goes here
player = 100
h = 10
m = 20
i = 1
while i <= 4 :
    inp1 = input()
    if inp1 == "hit" :
        player = player + 10
        i = i + 1
    if inp1 == "miss" :
        player = player - 20
        i = i + 1

print (player)
me = {
    "height": "170",
    "fav_color": "light green",
    "fav_author": "原ゆたか",
    "Birthplace": "琉球"
}

print(me)

answer = input("Type height, fav_color or fav_author, Birthplace")
if answer in me:
    result = me[answer]
    print(result)

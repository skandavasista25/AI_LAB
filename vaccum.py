rooms = {
    "A": "DIRTY",
    "B": "CLEAN"
}
vacuum = "A"
steps = 4
while steps > 0:
    print("Vacuum is in room", vacuum)
    print("Room condition:", rooms[vacuum])
    if rooms[vacuum] == "DIRTY":
        print("Action: SUCK")
        rooms[vacuum] = "CLEAN"
    else:
        if vacuum == "A":
            vacuum = "B"
        else:
            vacuum = "A"
        print("Action: MOVE")
    steps = steps - 1
print("\nFinal condition:")
print("A =", rooms["A"])
print("B =", rooms["B"])

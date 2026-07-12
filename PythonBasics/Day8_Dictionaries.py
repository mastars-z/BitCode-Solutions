# Enter your code here. Read input from STDIN. Print output to STDOUT
size = int(input())
room_no = input()
room_no = room_no.split(" ")
def captain_room(size,room_no):
    ordered = {}
    for room in room_no:   
        if room not in ordered:
            ordered[room] = 1
        else:
            ordered[room] += 1
    for room in ordered:
        if ordered[room] == 1:
            return room
        
print(captain_room(size,room_no))

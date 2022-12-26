# Enter your code here. Read input from STDIN. Print output to STDOUT

def findCaptainsRoom():
    k = int(input())
    rooms = list(map(int, input().split()))
    distnictRooms = {}
    for room in rooms:
        distnictRooms[room] = distnictRooms.get(room, 0) + 1
    for key,val in distnictRooms.items():
        if val <= len(rooms) % k:
            return key 
        
print(findCaptainsRoom())
    

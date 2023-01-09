duration, minMinuite = map(int, input().split())
theorems = list(map(int, input().split()))
minute = list(map(int, input().split()))
'''
Approach: Sliding Windows
'''
# total wake up time
wakeupTime = 0
for i in range(duration):
    if minute[i] == 1:
        wakeupTime += theorems[i]

# current straight wake up time
currWakeup = 0
for i in range(minMinuite):
    if minute[i] == 0:
        currWakeup += theorems[i]

# maximum wake up time
maxWake = wakeupTime + currWakeup
ptr1, ptr2 = 0, minMinuite

while ptr2 < duration:
    # decrease the current wake up time if the previous point points that Mishka is asleep
    if minute[ptr1] == 0:
        currWakeup -= theorems[ptr1]
    # increase the current wake up time if the current point points that Mishka is asleep
    if minute[ptr2] == 0:
        currWakeup += theorems[ptr2]
    maxWake = max(maxWake, wakeupTime + currWakeup)
    ptr1 += 1
    ptr2 += 1

print(maxWake)

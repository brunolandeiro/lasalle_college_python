# 8) Remove duplicates from a list and create a tuple and find the minimum number and maximum

sampleList = [87, 45, 41, 65, 94, 41, 99, 94]
print(sampleList)
sampleSet = set(sampleList)
print(sampleSet)
sampleTuple = tuple(sampleSet)
print(sampleTuple)
print("Min number:", min(sampleTuple))
print("Max number:", max(sampleTuple))
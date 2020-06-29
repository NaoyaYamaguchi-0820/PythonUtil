import random

string = 'beautiful'

resultString = ''.join(random.sample(string, len(string)))
print(resultString)
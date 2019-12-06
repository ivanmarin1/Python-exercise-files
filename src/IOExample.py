import math
import json

year = 2016
event = "Referendum"
yes_votes = 42_562_654
no_votes = 43_132_495
percentage = yes_votes / (yes_votes + no_votes)

# print(f"Results of the {year} {event}")
# print("{:-4} Yes votes {:2.2%}".format(yes_votes, percentage))

num = 24.65746758

# print(f'The value rounded to 3 decimals: {num:.3f}')
# print('The value rounded to 3 decimals: {}'.format(round(num, 3)))

with open("myfile.txt") as f:
    for lines in f:
        print(f.readline())
        print(lines, end="")

values = ("Awesome file made by me ", 100, " percentage")
s = str(values)

with open("newFile.txt", "w") as fw:
    # fw.write(s)
    json.dump([1, "simple", "list"], fw)

with open("newFile.txt") as fr:
    js = json.load(fr)

print(js)

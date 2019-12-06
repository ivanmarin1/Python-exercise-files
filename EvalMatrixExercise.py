import numpy as np
import pandas as pd

class matrix:
    "A matrix used in classification"
    mat = 0
    def __init__(self):
        mat = np.array(0)
    def setMatrix(a):
        mat = np.array(a)
    def getMatrix(a):
        return(a)

def insertMatrix():
    print("Enter number of classes: ")
    classNum = input()
    classNum = int(classNum)
    myMat = matrix()
    print("Enter data: \n")
    temp = input()
    print(np.array(list(temp)).reshape(classNum, classNum))

insertMatrix()

d={"A":[1, 2, 3, 4],
    "B":[5, 6, 7, 8],
    "C":[3, 4, 5, 6],
    "D":[9, 8, 7, 6]}

indexList = []
for x in d.keys():
    indexList.append(x)

print(indexList)

df2 = pd.DataFrame(data=d, index=indexList)

print(df2.transpose())

# f2 = pd.DataFrame(data=[pd.Timestamp("20130102"), 
#                    pd.Timestamp("20130102"),
#                    pd.Series(1, index=list(range(4)), dtype="float32"),
#                    np.array([3] * 4, dtype="int32"),
#                    pd.Categorical(["test", "train", "test", "train"]),
#                 #    pd.Categorical(["test", "train", "test", "train"]),
#                     ], 
#                    index=["A", "B", "C", "D"], 
#                    columns=["A", "B","C","D","E"])
# print(f2)

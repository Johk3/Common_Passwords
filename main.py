import time
import collections
from collections import OrderedDict

class Node(object):

    def __init__(self):
        self.passwords = []
        self.duplicates = []
        self.duplicate_amount = 0

        self.B_dict_duplicates = {}

    def Solution_A(self, password):
        for i in range(len(password)):
            if password[i] in self.passwords:
                self.duplicate_amount += 1
                self.duplicates.append(password[i])
            else:
                self.passwords.append(password[i])

    def Solution_B(self, password):
        for i in range(len(password)):
            if password[i] in self.passwords:
                self.duplicate_amount += 1
                self.duplicates.append(password[i])
            else:
                self.passwords.append(password[i])

    def Cleaner_A(self):
        print("I found {} duplicates, and I searched {} passwords".format(self.duplicate_amount, len(self.passwords)))
        c = collections.Counter(self.duplicates)
        print("These are the top 20 passwords\n")
        i = 0
        mostcommon = []
        for name, score in c.most_common(20):
            i+=1
            mostcommon.append("{}.Password \"{}\" came up {} times\n".format(i, name.rstrip(), score))
        for i in range(len(mostcommon)):
            print(mostcommon[len(mostcommon) - (i + 1)])

    def Cleaner_B(self):
        for item in self.duplicates:
            if item in self.B_dict_duplicates:
                self.B_dict_duplicates[item] = self.B_dict_duplicates[item] + 1
            else:
                self.B_dict_duplicates[item] = 1

        arr = []
        for item in self.B_dict_duplicates:
            arr.append(self.B_dict_duplicates[item])

        return arr

    def Display_Results_B(self, results):
        i = 0
        arr = []
        for result in results:
            i += 1
            if i > 20:
                break
            for name, number in self.B_dict_duplicates.items():
                if result == number:
                    arr.append("{}.Password \"{}\" came up {} times\n".format(i, name.rstrip(), number))
                    break
        for i in range(len(arr)):
            print(arr[len(arr) - (i + 1)])




def mergeSort(alist):
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1
    return alist



with open("10-million-combos.txt", 'r', encoding="utf-8", errors='ignore') as txt:
    # This code is for the Solution B
    # print("Work started on solution B.\nNothing will show up until finished to keep everything optimized.\n")
    # start_time = time.time()
    # engine = Node()
    # for i in range(10000000):
    #     engine.Solution_B(txt.readline().split('\t'))
    # results_to_merge = engine.Cleaner_B()
    #
    # results = list(OrderedDict.fromkeys(mergeSort(results_to_merge)))
    # correct_results = []
    # for i in range(len(results)):
    #     correct_results.append(results[len(results) - (i + 1)])
    # print("These are the top 20 passwords\n")
    # engine.Display_Results_B(correct_results)
    #
    # print("Done")
    # print("This took ", "---{0:.2f} Seconds---".format(time.time() - start_time))

    # This code is for the Solution A
    start_time = time.time()
    print("Work started on solution A.\nNothing will show up until finished to keep everything optimized.\n")
    engine = Node()
    #you can change this range to be for example 10,000 if 10 million is a bit too much!
    for i in range(10000000):
        # .split splits the passwords into two categories: first and last
        engine.Solution_A(txt.readline().split('\t'))
    print("Done")
    print("This took ", "---{0:.2f} Seconds---".format(time.time() - start_time))
    engine.Cleaner_A()



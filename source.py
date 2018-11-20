with open("input.txt") as f:
    w = [int(x) for x in next(f).split()]  # read first line
    if w[0] <= 5:
        for a in range(w[0]):
            array = []
            t = [int(x) for x in next(f).split()]  # read first line
            if t == []:
                t = [int(x) for x in next(f).split()]  # read first line
            if t[0] <= 10000:
                recursion = [1]
                counter = 0
                for b in range(t[0]):
                    array.append([str(x) for x in next(f).split()])
                array.sort()
                for ind in range (1, len(array)):
                    recursion.append(1)
                    if array[ind-1] == array[ind]:
                        recursion[ind] += 1
                        array[ind - 1] = "n"
                        recursion[ind - 1] = "n"
                        counter += 1
                for q in range(counter):
                    array.remove("n")
                    recursion.remove("n")
                for ind in range(len(array)):
                    print ' '.join(array[ind]), recursion[ind]
                if a < w[0]-1:
                    print ""
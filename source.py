with open("input.txt") as f: #get the file
    w = [int(x) for x in next(f).split()]  # read first line to get the number of tests
    if w[0] <= 5: #check if the number of tests are within limits
        for a in range(w[0]): #run the code as many times as the test number
            array = []
            t = [int(x) for x in next(f).split()]  # read the number of accounts
            if t == []: #corner case for when an empty line seperates the chunk of accounts
                t = [int(x) for x in next(f).split()]  # read number of accounts
            if t[0] <= 10000: #check if the number of accounts are within limits
                recursion = [1] #initialize the recursion array for keeping track of duplicates
                counter = 0 #initialize the counter of duplicate numbers
                for b in range(t[0]): #read the account numbers
                    array.append([str(x) for x in next(f).split()])
                array.sort() #sort the account numbers
                for ind in range (1, len(array)): #loop for finding the duplicates
                    recursion.append(1)
                    if array[ind-1] == array[ind]: #case when a duplicate is found
                        recursion[ind] += 1 #increase the corresponding duplication number
                        array[ind - 1] = "n" #mark the duplicate entry
                        recursion[ind - 1] = "n"
                        counter += 1 #increase the number of duplications
                for q in range(counter): #remove the marked duplicate entries
                    array.remove("n")
                    recursion.remove("n")
                for ind in range(len(array)):# print the resulting sorted list with the number of duplicated accounts
                    print ' '.join(array[ind]), recursion[ind]
                if a < w[0]-1: #if there are more accounts print an empty line between them
                    print ""
            else:
                print "invalid file format" #for when the number of accounts have exceeded the given limits
    else:
        print "invalid file format" #for when the number of tests have exceeded the given limits
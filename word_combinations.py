# John Diggins
# Solution to print all combinations of
# [['quick', 'lazy'], ['brown', 'black', 'grey'], ['fox', 'dog']]

def array_counter(counting_arr, limit_arr):
    pos = len(counting_arr) - 1

    if(counting_arr == limit_arr):
        return [-1]

    counting_arr[pos] += 1
    formattingArray = True
    while(formattingArray):
        if(counting_arr[pos] > limit_arr[pos]):
            counting_arr[pos] = 0
            counting_arr[pos - 1] += 1
            pos -= 1
        else:
            formattingArray = False

    return counting_arr
    
def printVector(counting_arr, vector):
    count = 0
    for v in vector:
        print(v[counting_arr[count]], end=' ')
        count += 1
    print()

def limitArrayBuilder(vec):
    my_list = []
    for n in vec:
        my_list.append(len(n) - 1)
    return my_list
def countingArrayBuilder(size):
    my_list = []
    for n in range(size):
        my_list.append(0)
    return my_list

def make_combinations (vec):
    counting_arr = countingArrayBuilder(len(vec))
    limit_arr = limitArrayBuilder(vec)

    while(counting_arr != [-1]):
        printVector(counting_arr, vec)
        counting_arr = array_counter(counting_arr, limit_arr)

word_vector = [['quick', 'lazy'], ['brown', 'black', 'grey'], ['fox', 'dog']]

make_combinations(word_vector)






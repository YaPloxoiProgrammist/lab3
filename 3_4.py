a = [1,2]
b = a
#a += [3,4]
    #здесь значение переменной записывается в одну и ту же ячейку,
    #поэтому значение b тоже меняется

a = a + [4,5,6]
    #здесь значение переменной записывается в новую ячейку, но т.к переменная b
    #уже взяла другое значение а, то она не меняется
print(b)

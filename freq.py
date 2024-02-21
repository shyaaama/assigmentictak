def freq(list):
    return max(set(list),key=list.count)
list=[2,1,2,2,1,3]
print(freq(list))


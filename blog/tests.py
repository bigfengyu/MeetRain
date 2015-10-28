from django.test import TestCase

# Create your tests here.

def partition_col(thelist,n):
    res = [[] for i in range(n)]
    l = len(thelist)
    for i in range(l):
        k = i%n
        res[i%n].append(thelist[i])
    return res


arr = [i for i in range(10)]

print(partition_col(arr,2))
"""2)Для заданного одномерного массива целых чисел найти максимальную по длине монотонную
(т.е. либо неубывающую, либо не возрастающую) подпоследовательность заданной последовательности
нечетных целых чисел."""

a=[]
a=input().split()
max_len=0
le=2
for i in range(0,1):
    b=[]
for i in range(2, len(a)):
    if le>max_len:
        max_len=le
    if a[i]%2==0:
        le+=1
    else:
        if a[i-2]<=a[i-1]<=a[i] or a[i-2]>=a[i-1]>=a[i]:
            le+=1
        elif a[i-1]<=a[i] or a[i-1]>=a[i]:
            le+=1

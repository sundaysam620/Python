##def sumNumbers(n):
##    i=1
##    ListOfNumbers = []
##    while i<n:
##        if (i%3)==0 or (i%5)==0:
##            ListOfNumbers.append(i)
##        else:
##            pass
##        i+=1
##    return sum(ListOfNumbers)
##x = sumNumbers(1000)
##print (x)

##def fibonacci(n):
##    c = 2
##    c = 1
##    SequenceList = [1,2] 
##    while c < n:
##        c = SequenceList[-1] + SequenceList[-2]
##        SequenceList.append(c) 
##    return SequenceList[:-1] 
## 
##def SumEvenValue(n):
##    Total = 0
##    sequence = fibonacci(n)
##    for i in sequence:
##        if i%2 == 0:
##            Total += i
## 
##    return Total
##x = SumEvenValue(4000000)
##print(x)

limit = 4000000
sum=0
a=1
b=1
c=a+b
while c<limit:
    sum=sum+c
    a=b+c
    b=c+a
    c=a+b
output sum

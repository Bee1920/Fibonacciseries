 list = []
 n = int(input("Enter the number of elements:"))
 for i in range(0, n):
  element = int(input())
  list.append(element)
 print("Positive numbers in list:")
 for j in range(n):
  if(list[j] >= 0):
   print(list[j], end = ' ')

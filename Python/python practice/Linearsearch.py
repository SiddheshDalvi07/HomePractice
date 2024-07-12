#linear search
arr=[1,2,3,4,5,6,7]
x=3
def search(arr, x):
 for i in range(len(arr)):
  if arr[i] == x:
   return i
 return -1

print(search(arr,x))
    
    
   
    
    
    
    
    
    
    

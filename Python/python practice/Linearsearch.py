#linear search
arr=[1,2,3,4,5,6,7]
x=8
def search(arr, x):
 for i in range(len(arr)):
  if arr[i] == x:
   return i
 return -1

print(f'element {x} is present at index {search(arr,x)}')
    
    
   
    
    
    
    
    
    
    

 
N = int(input("Please enter a number:" ));
def Prime(n):
  if(n==1 or n==0):
    return False
  for i in range(2,n):
    if(n%i==0):
      return False
  return True
for i in range(1,N+1):
  if(Prime(i)):
    print(i,end=" ")

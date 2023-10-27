sum=0.0
distance=1
count=0

while(sum<=2.5):
     if(count==500):
         print(sum)
         break
     else:
             sum=sum+distance
             distance=(distance/2)
             count=count+1
             
# Frog is not managed to cross 2.5 meters because the distance are getting small.
# We checked for 200 times jump and for 500 times jump, still it is showing the total distance which he covered is around 2.0 for both cases.        
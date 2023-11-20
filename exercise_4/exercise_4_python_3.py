hr_=int(input("Enter the hour : "))
min_=int(input("Enter the minute : "))
sec_=int(input("Enter the second : "))

# now we are incresing second by the one
 

if(hr_!= 24 and min_==59 and sec_==59):
    hr_=hr_+1
    min_=0
    sec_=0
    print(f"New time: {hr_:02d}:{min_:02d}:{sec_:02d}")

elif(min_!= 59 and sec_!= 59):
    sec_=sec_+1
    print(f"New time: {hr_:02d}:{min_:02d}:{sec_:02d}")

elif(min_!= 59 and sec_==59):    
    min_=min_+1
    sec_=0
    print(f"New time: {hr_:02d}:{min_:02d}:{sec_:02d}")

elif(min_ == 59 and sec_!= 59):    
   sec_=sec_+1
   print(f"New time: {hr_:02d}:{min_:02d}:{sec_:02d}")

elif(min_==59 and sec_==59):
    hr_=0
    min_=0
    sec_=0
    print(f"New time: {hr_:02d}:{min_:02d}:{sec_:02d}")











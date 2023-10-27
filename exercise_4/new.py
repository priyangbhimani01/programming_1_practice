hr_=int(input("Enter the hour : "))
min_=int(input("Enter the minute : "))
sec_=int(input("Enter the second : "))

# now we are incresing second by the one

if(min_==59 and sec_==59):
    hr_=hr_+1
    min_=0
    sec_=0
    print(hr_)
    print(min_)
    print(sec_)

elif(min_ is not 59 and sec_ is not 59):
    sec_=sec_+1
    print(hr_)
    print(min_)
    print(sec_)





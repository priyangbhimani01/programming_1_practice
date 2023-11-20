
def palindrom(word):
    start=0
    end=len(word)-1

    while(start<end):
        if(word[start]==word[end]):
            start=start+1
            end=end-1
            
        else:
            return False
        
    return True


word=input("Enter the word: ")
print(palindrom(word))        
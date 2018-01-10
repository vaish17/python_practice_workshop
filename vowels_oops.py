class vowels:
    s = "vaishnavi"
    g = "aeiou"
    size = len(s)
    count = 0
    for i in s:
        if i in g:
            count +=1
    nov = size - count    
    print("number of vowels",count)
    print("number of consonants",nov)

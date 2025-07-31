def calculate_love_score(name1, name2):
    name_one = name1.upper()
    name_two = name2.upper()
    total_for_true = ""
    total_for_love = ""

    for i in name_one:
        for j in "TRUE":
            if i == j:
                total_for_true += i
        for k in "LOVE":
            if i == k:
                total_for_love += i 
          
    
    for h in name_two:
        for m in "TRUE":
            if h == m:
                total_for_true += h
        for n in "LOVE":
            if h == n:
                total_for_love += n
    total = (str(len(total_for_true)) + str(len(total_for_love)))
    print(total)
   
                

calculate_love_score("Thandoluhle","Lisa")
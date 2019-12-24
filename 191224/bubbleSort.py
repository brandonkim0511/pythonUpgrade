def bubblesort(list):
    for iter_num in range(len(list)-1,0,-1):
        for idx in range(iter_num):
            if list[idx]>list[idx+1]:
                temp = list[idx]
                list[idx] = list[idx+1]
                list[idx+1] = temp
                print(list)
    # return(list)

list = [19,2,31,45,6,11,121,27]
bubblesort(list)
print(list)

#Challenge : Sort this List in alphabetical order using Bubble Sort.
["Nayeon",  "JeongYeon", "Sana", "MoMo", "Mina", "Jihyo", "Dahyun", "Tzuyu", "Chaeyoung" ]

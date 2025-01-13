def dict_sorter(dict,lwidth,rwidth):
    print("picnic items".center(lwidth+rwidth,"_"))
    for key,value in dict.items():
        print(key.ljust(lwidth,"."),value.rjust(rwidth," "))


items = {"apple":"5","potato":"6","tomato":"12"}
dict_sorter(items,12,15)

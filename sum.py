# sum of odd numbers

a = int(input("Son kiriting: "))
list1 = []
i = 1
jami = 0
while i <= a:
    try:
        son = float(input(f"{i} - son: "))
        list1.append(son)
        i += 1
        if son % 2 == 1:
        	jami += son
        else:
        	pass

    except:
        print("Faqat Son kiriting!!!")
print("Toq sonlarning yig'indisi: ",jami)

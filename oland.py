print("Oland election")
import random
provinces = ["Amelitical North Oland", "Monkonia", "Tonsky", "North Amelico", "South Amelico", \
"Auwora", "Diveus", "South Oland", "Nordurk", "Oretian", "Dorrun", "Gorrilia Oland", \
"Perusian", "Gazante", "Oogan", "Uramoria", "Mountain", "Aquotitl", "Penonpore", "Airovsky", \
"Ceolynia", "North Utnania", "New Sackny", "South Utnania", "Inner Oretian Islands"]
greentotal = 0
redtotal = 0
thirdtotal = 0
for i in range(len(provinces)):
    x = 0
    selected = random.choice(provinces)
    print(selected)
    if selected == "Amelitical North Oland":
        PGreen = 98
        PRed = 1
        PThird = 1
        value = 8
    elif selected == "Monkonia":
        PGreen = 60
        PRed = 38
        PThird = 2
        value = 29
    elif selected == "Tonsky":
        PGreen = 46
        PRed = 52
        PThird = 2
        value = 19
    elif selected == "North Amelico":
        PGreen = 98
        PRed = 1
        PThird = 1
        value = 6
    elif selected == "South Amelico":
        PGreen = 97
        PRed = 1
        PThird = 2
        value = 6
    elif selected == "Auwora":
        PGreen = 92
        PRed = 3
        PThird = 5
        value = 3
    elif selected == "Diveus":
        PGreen = 3
        PRed = 95
        PThird = 2
        value = 7
    elif selected == "South Oland":
        PGreen = 52
        PRed = 45
        PThird = 3 
        value = 35
    elif selected == "Nordurk":
        PGreen = 98
        PRed = 1
        PThird = 1 
        value = 11
    elif selected == "Oretian":
        PGreen = 97
        PRed = 2
        PThird = 1 
        value = 71
    elif selected == "Dorrun":
        PGreen = 96
        PRed = 2
        PThird = 2
        value = 5
    elif selected == "Gorrilia Oland":
        PGreen = 30
        PRed = 65
        PThird = 5
        value = 2
    elif selected == "Perusian":
        PGreen = 5
        PRed = 94
        PThird = 1
        value = 16
    elif selected == "Gazante":
        PGreen = 96
        PRed = 3
        PThird = 1
        value = 22
    elif selected == "Oogan":
        PGreen = 3
        PRed = 96
        PThird = 1
        value = 13
    elif selected == "Uramoria":
        PGreen = 1
        PRed = 98
        PThird = 1
        value = 9
    elif selected == "Mountain":
        PGreen = 60
        PRed = 35
        PThird = 5
        value = 7
    elif selected == "Aquotitl":
        PGreen = 2
        PRed = 90
        PThird = 8
        value = 3
    elif selected == "Penonpore":
        PGreen = 45
        PRed = 52
        PThird = 3
        value = 17
    elif selected == "Airovsky":
        PGreen = 43
        PRed = 55
        PThird = 2
        value = 9
    elif selected == "Ceolynia":
        PGreen = 40
        PRed = 59
        PThird = 1
        value = 16
    elif selected == "North Utnania":
        PGreen = 1
        PRed = 98
        PThird = 1
        value = 46
    elif selected == "South Utnania":
        PGreen = 1
        PRed = 98
        PThird = 1
        value = 40
    elif selected == "New Sackny":
        PGreen = 97
        PRed = 2
        PThird = 1
        value = 10
    elif selected == "Inner Oretian Islands":
        PGreen = 98
        PRed = 1
        PThird = 1
        value = 2
    problist = list()
    for i in range(PGreen):
        problist.append("ATP wins")
    for i in range(PRed):
        problist.append("LOP wins")
    for i in range(PThird):
        problist.append("NDP wins")
    result = random.choice(problist)
    if result == "ATP wins":
        greentotal = greentotal + value
    elif result == "LOP wins":
        redtotal = redtotal + value
    elif result == "NDP wins":
        thirdtotal = thirdtotal + value
    print(result)
    print("ATP ", greentotal, "   LOP ", redtotal, "   NDP ", thirdtotal)
    while selected in provinces:
        if provinces[x] == selected:
            del provinces[x]
        x = x + 1       
    nexto = str(input("continue?   "))
    if nexto == "no":
        break
print("ATP ", greentotal, "   LOP ", redtotal, "   NDP ", thirdtotal)
if greentotal > 202:
    print("ATP wins the election")
elif redtotal > 202:
    print("LOP wins the election")
elif thirdtotal > 202:
    print("NDP wins the election")
else:
    print("second round needed")
        
     




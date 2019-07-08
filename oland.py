#!/usr/nbin/python3
import random
print("Oland election")
thirdlist = list()

provinces = [
  { 'name':"Amelitical North Oland",  'PGreen': 98,  'PRed': 1, 'PThird': 1,  'value': 8},
  { 'name':"Monkonia",                           'PGreen': 60,  'PRed': 38, 'PThird': 2, 'value': 29},
  { 'name':"Tonsky",                                 'PGreen': 42,  'PRed' : 52, 'PThird': 6,  'value': 19},
  { 'name':"North Amelico",                  'PGreen':98,  'PRed': 1, 'PThird': 1, 'value': 6},
  { 'name':"South Amelico",                  'PGreen':97, 'PRed': 1, 'PThird': 2, 'value': 6},
  { 'name':"Auwora",                               'PGreen': 92, 'PRed': 3, 'PThird': 5, 'value': 3},
  { 'name':"Diveus",                                 'PGreen': 3, 'PRed': 95, 'PThird': 2, 'value': 7},
  { 'name':"South Oland",                      'PGreen': 46, 'PRed': 52, 'PThird': 2 , 'value': 35},
  { 'name':"Nordurk",                              'PGreen': 96, 'PRed': 3, 'PThird': 1 , 'value': 11},
  { 'name':"Oretian",                               'PGreen': 95, 'PRed': 4, 'PThird': 1 , 'value': 71},
  { 'name':"Dorrun",                                'PGreen': 97, 'PRed': 1, 'PThird': 2, 'value': 5},
  { 'name':"Gorrilia Oland",                   'PGreen': 30, 'PRed': 65, 'PThird': 5, 'value': 2},
{ 'name':"Perusian",                               'PGreen': 5, 'PRed': 94, 'PThird': 1, 'value': 16},
{ 'name':"Gazante",                               'PGreen': 95, 'PRed': 3, 'PThird': 2, 'value': 22},
{ 'name':"Oogan",                                  'PGreen': 2, 'PRed': 97, 'PThird': 1, 'value': 13},
{ 'name':"Uramoria",                             'PGreen': 5, 'PRed': 94, 'PThird': 1, 'value': 9},
{ 'name':"Mountain",                            'PGreen': 60, 'PRed': 35, 'PThird': 5, 'value': 7},
{ 'name':"Aquotitl",                               'PGreen': 2, 'PRed': 60, 'PThird': 38, 'value': 4},
{ 'name':"Penonpore",                         'PGreen': 43, 'PRed': 49, 'PThird': 8, 'value': 17},
{ 'name':"Airovsky",                              'PGreen': 34, 'PRed': 59, 'PThird': 5, 'value': 9},
{ 'name':"Ceolynia",                              'PGreen': 40, 'PRed': 59, 'PThird': 1, 'value': 16},
{ 'name':"North Utnania",                  'PGreen': 5, 'PRed': 94, 'PThird': 1, 'value': 46},
{ 'name':"New Sackny",                       'PGreen': 96, 'PRed': 3, 'PThird': 1, 'value': 10},
{ 'name':"South Utnania",                   'PGreen': 1, 'PRed': 98, 'PThird': 1, 'value': 40},
{ 'name':"Inner Oretian Islands",        'PGreen': 98, 'PRed': 1, 'PThird': 1, 'value': 2}
]
greentotal = 0
redtotal = 0
thirdtotal = 0
for i in range(len(provinces)):
    x = 0
    selected = random.choice(provinces)
    print(selected['name'])
    problist = list()
    problist.extend("A" * selected['PGreen'])
    problist.extend("L" * selected['PRed'])
    problist.extend("N" * selected['PThird'])
    result = random.choice(problist)
    if result == "A":
        greentotal = greentotal + selected['value']
        print("ATP Wins!")
    elif result == "L":
        redtotal = redtotal + selected['value']
        print("LOP Wins!")
    elif result == "N":
        nlist = list()
        thirdtotal = thirdtotal +selected['value']
        print("NDP Wins!")
        nlist.append(selected['PGreen'])
        nlist.append(selected['PRed'])
        nlist.append(selected['value'])
        nlist.append(selected['name'])
        thirdlist.append(nlist)
    print("ATP ", greentotal, "   LOP ", redtotal, "   NDP ", thirdtotal)
    while selected in provinces:
        if provinces[x] == selected:
            del provinces[x]
        x = x + 1
    nexto = str(input("continue?   "))
    if nexto == "no":
        break
print("ATP ", greentotal, "   LOP ", redtotal, "   NDP ", thirdtotal)
if greentotal > 206:
    print("ATP wins the election")
elif redtotal > 206:
    print("LOP wins the election")
elif thirdtotal > 206:
    print("NDP wins the election")
else:
    print("second round needed")
    thirdtotal = 0
    for i in range(len(thirdlist)):
        print((thirdlist[i])[3])
        problist = list()
        problist.extend("A" * int((thirdlist[i])[0]))
        problist.extend("A" * int((thirdlist[i])[1]))
        result = random.choice(problist)
        if result == "A":
            greentotal = greentotal + (thirdlist[i])[2]
            print("ATP Wins!")
        elif result == "L":
            redtotal = redtotal + (thirdlist[i])[2]
            print("LOP Wins!")
        print("ATP ", greentotal, "   LOP ", redtotal, "   NDP ", thirdtotal)
        nexto = str(input("continue?   "))
        if nexto == "no":
            break
    print("ATP ", greentotal, "   LOP ", redtotal, "   NDP ", thirdtotal)
    if greentotal >206:
        print("ATP wins the election")
    elif redtotal > 206:
        print("LOP wins the election")

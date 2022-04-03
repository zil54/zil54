list_hobbies = ['hockey', 'basketball', 'volleyball', 'chess', 'draughts']
list_foods = ['bread', 'buterbrod', 'smoothie', 'cookie']
list_favs = list_hobbies+list_foods
print(list_favs)
building_1_ninjas=25
building_2_ninjas=25
building_3_ninjas=25
tunnel_1_ninjas=40
tunnel_2_ninjas=40


all_buildings_ninjas = [25, 25, 25]
all_tunnels_sams = [40, 40]
sub_total = 0
sub_total2 = 0
for each_item_ninja in all_buildings_ninjas:
    sub_total = sub_total + each_item_ninja
for each_item_sam in all_tunnels_sams:
    sub_total2 = sub_total2 + each_item_sam
print (sub_total + sub_total2)



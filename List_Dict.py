phones_price = {
    'CibeR': {
        'Redmi 12': 11943,
        'a5': 3000,
        'cX10': 9525,
        's20': 20000,
        'A43': 11500,
        's3': 2575,
        's15maxsuper': 60500,
        's12pro': 21000
    },
    'MobI': {
        'Redmi 12': 11943,
        'a5': 3050,
        'cX10': 9925,
        's20': 21999,
        'A43': 11500,
        's3': 2570,
        's15maxsuper': 60500,
        's12pro': 20000
    },
    'LuxtecH': {
        'Redmi 12': 13499,
        'a5': 3840,
        'cX10': 9575,
        's20': 25000,
        'A43': 11900,
        's3': 2575,
        's15maxsuper': 60500,
        's12pro': 23000
    }
}
print(phones_price)
a = [phones_price[mag]['s12pro'] for mag in phones_price]
print(a)
vlans = [[10, 21, 35], [101, 115, 150], [111, 40, 50]]
result = [vlan for vlan_list in vlans for vlan in vlan_list]
print(result)
s = [j for i in vlans for j in i]
print(s)
d = {num: num**2 for num in range(1, 11)}
print(d)
lower_key_phones = {mag: {key.lower(): value for key, value in model.items()} for mag, model in phones_price.items()}
print(lower_key_phones)
n = {x: x + x for x in range(5)}
print(n)
n2 = {x.upper(): x * 3 for x in 'beaerb'}
print(n2)
l_k_p = {i: {k.lower(): v for k, v in j.items()} for i, j in phones_price.items()}
print(l_k_p)
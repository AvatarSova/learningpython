citys = {'city': 'Москва', 'temprerature':20}

print(citys.get('city'))
citys['temprerature'] -= 5
print(citys)

print('country' in citys)
print(citys.get('country', 'Russia'))

citys['date'] = '27.05.2017'
print(len(citys))
print(citys)

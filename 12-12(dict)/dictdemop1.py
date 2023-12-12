actor = {
    'name': 'kevin hart',
    'id': 4142142,
    'movies': ['fatherhood', 'whats now']
}

# print(actor)
# print(type(actor))
# print(actor['name'])
# # print(actor['salary'])
# print(actor.get('salary'))

# print(actor)
# actor['name'] = 'kevin <3'  # override a value
# actor['salary'] = 18000  # add a new pair
# print(actor)

# print(actor)
# del actor['id'] # delete the key and the value
# print(actor)
#
# name = actor.pop('name')
# print(actor)
# print(name)

# print(actor)
# actor.clear()  # delete all the pairs
# print(actor)

# x = actor.popitem()
# print(x)

# for k in actor: # iterate over the keys
#     print(f'the value of the key {k} is {actor[k]}')

# print(actor)  # dict
# print(actor.values())  # tuple values
# print(actor.keys())  # keys tuple
# print(actor.items())  # tuple list tuples key value

for k, v in actor.items():  # iterate over all the key and the values of json
    print(k, v)

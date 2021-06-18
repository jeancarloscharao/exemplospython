
pessoa = {'nome': 'Jean Carlos', 'idade': 39, 'cidade' : 'Porto Alegre', 'cursos': []}

print(pessoa)

print(pessoa['nome'])

print(pessoa.get('nome'))

print(pessoa.keys())

print(pessoa.values())

print(pessoa.items())

print(pessoa)

pessoa['cursos'].append('Angular')

print(pessoa)

pessoa.pop('idade')

print(pessoa)

pessoa.update({'idade': 40})

print(pessoa)

del pessoa['cursos']

print(pessoa)







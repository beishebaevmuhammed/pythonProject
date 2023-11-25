data = ("O!", "Megacom", "0705", "Beeline", "0550", "0770", "Katel", "0510", "Fonex", "0543")

designations = []
codes = []

for i in data:
    if i.isnumeric():
        codes.append(i)
    else:
        designations.append(i)

operators = {}

i = 0
while i < len(designations):
    operators[designations[i]] = {codes[i]}
    i += 1

del operators[designations[3]]
del operators[designations[4]]
operators[designations[0]].update({'0700', '0500'})
operators[designations[1]].update({'0999', '0555'})
operators[designations[2]].update({'0222', '0777'})

for key, value in operators.items():
    print(f'{key} - {value}')
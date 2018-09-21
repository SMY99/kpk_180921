from gadget import Smartphone, Consolys, Compudahters

print('*' *45)
smartphone = Smartphone.import_from_file('smartphones.src')
[print(el) for el in smartphone]

print('*' *45)
consolys = Consolys.import_from_file('consolys.src')
[print(el) for el in consolys]

print('*' *45)
compudahters = Compudahters.import_from_file('compudahters.src')
[print(el) for el in compudahters]
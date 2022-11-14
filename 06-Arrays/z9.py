names = ['Genowefa','Onufry','Celestyna','Alojzy','Pankracy']

minname = names[0]
maxname = names[0]

for name in names:
    if len(name) < len(minname):
        minname = name
    elif len(name) > len(maxname):
        maxname = name

print(minname, maxname)
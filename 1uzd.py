from dati import dati



with open("nosaukumi.txt", "w") as file:
    for names in dati:
        file.write(names["name"]+"\n")
    pass

def year_sort(elem):
    return(elem["year_published"])

dati.sort(key=year_sort,reverse=True)
oldest_book = dati[0]
print(oldest_book["name"])

for data in dati:
    print(data["pages"])
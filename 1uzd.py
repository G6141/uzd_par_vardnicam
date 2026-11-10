from dati import dati

with open("nosaukumi.txt", "w") as file:
    for names in dati:
        file.write(names["name"]+"\n")
    pass


# ------ sort functions ------
def year_sort(elem):
    return(elem["year_published"])

def author_sort(elem):
    return(elem["author"])

def name_length_sort(elem):
    return(len(elem["name"]))

def key_sort(elem):
    return(elem.items())





def longest_name(x):
    y = x
    y.sort(key=name_length_sort,reverse=True)
    return(y[0])


dati.sort(key=year_sort)
oldest_book = dati[0]
print("oldestbook:",oldest_book["name"])


total_price = 0
for data in dati:
    print(data["pages"])
    total_price += int(data["price"])

average_price = total_price/len(dati)

print(average_price)

longest_name_book = longest_name(dati) 
print(longest_name_book["author"]+",",longest_name_book["year_published"])
authors = {}
dati_copy = dati
for data in dati_copy:
    if data["author"] == "":
        data["author"] = "Nav norādīts"
    
    if data["author"] not in authors:
        authors[data["author"]] = 1

    else:
        authors[data["author"]] += 1

authors = {k: v for k, v in sorted(authors.items(), key=lambda item: item[0])}
print(authors)
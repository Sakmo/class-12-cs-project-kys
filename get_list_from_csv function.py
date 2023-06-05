

def get_list_from_csv(adm):
    adm = adm[4:]
    import csv
    rows = []
    with open('class 12 project\dataset1.csv','r') as f:
        fc = csv.reader(f)
        for row in fc:
            rows.append(row)
            if row[0]==adm:
                return row
        return []
print(get_list_from_csv('G46-3832'))    
def data_fixer():
    import csv
    import data_indicies
    switch="OFF"
    month_index=data_indicies.month_index
    day_index=data_indicies.day_index
    with open('data_Lev.csv', 'r') as data:
        reader = csv.reader(data, delimiter=';', quotechar='"')
        full_document = []
        for row in reader:
            full_document.append(row)
        data.close()
    for i in full_document:    
        if len(i[month_index])<2:
            switch="ON"
            i[month_index]="0"+i[month_index]
    for i in full_document:
        if len(i[day_index])<2:
            switch="ON"
            i[day_index]="0"+i[day_index]
    if switch=="ON":
        with open('data_Lev.csv', 'w') as data:
            data.write("")
        with open('data_Lev.csv', 'a') as data:
            for i in full_document:
                for j in i: 
                    data.write(j+";")
                data.write("\n")
            data.close()
data_fixer()

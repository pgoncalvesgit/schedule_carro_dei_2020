import csv

def le_form(num_tasks, num_shifts):
    
    file = open('form.csv', 'r')
    csv_dic = csv.DictReader(file)
    
    new_rows = list()
    new_row = list()
    
    aux_text = ""
    
    fieldnames = csv_dic.fieldnames
    
    for row in csv_dic:
        #name
        new_row.append(row[fieldnames[1]])
        
        #availability
        if(row[fieldnames[2]] == "Sim"):
            new_row.append(1)
        else:
            new_row.append(0)
        
        #order of tasks
        for i in range(num_tasks):
            if(i > 0):
                aux_text += "-"
            aux_text += row[fieldnames[2 + 1 + i]]
        new_row.append(aux_text)
        aux_text = ""
        
        #order of shifts
        for i in range(num_shifts):
            if(i > 0):
                aux_text += "-"
            aux_text += row[fieldnames[2 + num_tasks + 1 + i]]
        new_row.append(aux_text)
        aux_text = ""
        
        #preference
        if(row[fieldnames[2 + num_tasks + num_shifts + 1]] == "Horario"):
            new_row.append(1)
        else:
            new_row.append(0)
            
        #tasks to avoid
        for i in range(num_tasks):
            if(row[fieldnames[2 + num_tasks + num_shifts + 2 + i]] == ""):
                break
            if(i > 0):
                aux_text += "-"
            aux_text += row[fieldnames[2 + num_tasks + num_shifts + 2 + i]]
        new_row.append(aux_text)
        aux_text = ""
                
        
        #shifts to avoid
        for i in range(num_tasks):
            if(row[fieldnames[2 + num_tasks + num_shifts + 1 + num_tasks + 1 + i]] == ""):
                break
            if(i > 0):
                aux_text += "-"
            aux_text += row[fieldnames[2 + num_tasks + num_shifts + 1 + num_tasks + 1 + i]]
        new_row.append(aux_text)
        aux_text = ""
        
        new_rows.append(new_row)
        
    print("teste")
    print(new_rows)
    
        
le_form(3,8)
        
        
        
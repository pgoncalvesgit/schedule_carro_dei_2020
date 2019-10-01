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
        temp = [None] * num_tasks
        
        for i in range(num_tasks):
            temp[num_tasks - int(row[fieldnames[2 + 1 + i]]) - 1] = str(i)
            
        for i in range(len(temp)):
            if(i > 0):
                aux_text += "-"
            aux_text += temp[i]
        new_row.append(aux_text)
        aux_text = ""
        
        #order of shifts
        temp = [None] * num_shifts
        
        for i in range(num_shifts):
            temp[num_shifts - int(row[fieldnames[2 + num_tasks + 1 + i]]) - 1] = str(i)
            
        for i in range(len(temp)):
            if(i > 0):
                aux_text += "-"
            aux_text += temp[i]
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
        
    file.close()
    
    
    
    file = open('../input/people_from_form.csv', 'w')
    
    file.write("name,available,tasks_prefered,shifts_prefered,preference,tasks_to_avoid,shifts_to_avoid\n")
    
    for row in new_rows:
        for i in range(len(row)):
            cell = row[i]
            file.write(str(cell))
            if(i < len(row) - 1):
                file.write(",")
        file.write("\n")
    
    file.close()


    
if __name__ == "__main__":  
    #CHANGE
    print("Number of shifts?")
    num_shifts = int(input())
    print("Number of tasks?")
    num_tasks = int(input())
    le_form(num_tasks, num_shifts)
        
        
        
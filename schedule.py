import random
import csv

#class to hold information about a person
class Person:
    def __init__(self, row):
        #name -> name of the person
        self.name = row["name"]
        
        #available -> boolean which indicates if the person is available
        #In the file:
        #   available == 0 -> not available
        #   available == 1 -> available
        self.available = (row["available"] == str(1))
        
        #initializes the hours to 0
        self.hours = 0
        
        #tasks_prefered -> order of task preference (index)
        self.tasks_prefered = row["tasks_prefered"].split("-")
        for i in range(len(self.tasks_prefered)):
            self.tasks_prefered[i] = int(self.tasks_prefered[i])
        
        #shifts_prefered -> order of shift preference (index)
        self.shifts_prefered = row["shifts_prefered"].split("-")
        for i in range(len(self.shifts_prefered)):
            self.shifts_prefered[i] = int(self.shifts_prefered[i])
        
        #preference -> indicates if the person prefers "shift" over "task"
        #   preference == 0 -> prefers "task" over "shift" (looks at person's tasks_prefered first)
        #   preference == 1 -> prefers "shift" over "task" (looks at person's shifts_prefered first)
        self.preference = int(row["preference"])
        
        #initializes schedule
        self.schedule = [[-1, -1], [-1, -1]]
        
        #tasks_to_avoid -> which tasks to avoid (index)
        self.tasks_to_avoid = row["tasks_to_avoid"].split("-")
        for i in range(len(self.tasks_prefered)):
            self.tasks_prefered[i] = int(self.tasks_prefered[i])
        
        #shifts_to_avoid -> which shift to avoid (index)
        self.shifts_to_avoid = row["shifts_to_avoid"].split("-")
        for i in range(len(self.shifts_prefered)):
            self.shifts_prefered[i] = int(self.shifts_prefered[i])
        
    #checks if the user is working at shift
    def works_at_shift(self, shift):
        return self.schedule[0][0] == shift or self.schedule[1][0] == shift
        
    #checks if the user is working at shift and task
    def works_at_shift_and_task(self, shift, task):
        return (self.schedule[0][0] == shift and self.schedule[0][1] == task) or \
               (self.schedule[1][0] == shift and self.schedule[1][1] == task)
        
    #string for debbugging
    def string_working(self):
        if(self.schedule[0][0] == -1):
            return self.name + " doesn't work"
        elif(self.schedule[1][0] == -1):
            return self.name + " works at " + str(self.schedule[0][0]) + "-" + str(self.schedule[0][1])
        else:
            return self.name + " works at " + str(self.schedule[0][0]) + "-" + str(self.schedule[0][1])\
                   + " and " + str(self.schedule[1][0]) + "-" + str(self.schedule[1][1])
    
    #string for debbugging
    def string_test(self):
        return self.name + " is working: " + str(self.schedule[0][0]) + "-" + str(self.schedule[0][1])\
               + " and " + str(self.schedule[1][0]) + "-" + str(self.schedule[1][1])\
               + " and has " + str(self.hours) + " hours"
    
#aux class
class Hour_Row:
    def __init__(self, row, fieldnames):
        self.row = list()
        for i in fieldnames:
            self.row.append(int(row[i]))

   
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        
#read every person and create a list with everyone
def read_persons():
    file = open('input/people_from_form.csv', 'r')
    csv_dic = csv.DictReader(file)
    
    persons = list()
    
    for row in csv_dic:
        person = Person(row)
        if(person.available):
            persons.append(person)
    
    file.close()
    return persons

#update the list with everyone with the current hours
def read_persons_hours(persons):
    file = open('input/hours.csv', 'r')
    csv_dic = csv.DictReader(file)
    
    fieldnames = csv_dic.fieldnames
    
    for row in csv_dic:
        for i in range(len(persons)):
            if(persons[i].name == row[fieldnames[0]]):
                persons[i].hours = int(row[fieldnames[1]])
                
    file.close()
    
    return fieldnames

#reads the number of people for the tasks
def read_tasks_people():
    file = open('input/number_people_tasks.csv', 'r')
    csv_dic = csv.DictReader(file)
    
    #creates the list with the number or people needed for each hour
    people_needed = list()
    fieldnames = csv_dic.fieldnames
    
    for row in csv_dic:
        new_row = list()
        hour_row = Hour_Row(row, fieldnames)
        for j in range(len(hour_row.row)):
            new_row.append(int(hour_row.row[j]))
        people_needed.append(new_row)
        
    
    #counts the number of people needed for some more data
    num_persons_needed_1_hour = 0
    num_persons_needed_2_hours = 0
    for i in range(round(len(people_needed)/2)):
        for j in range(len(fieldnames)):
            num_persons_needed_2_hours += people_needed[i*2][j]
            num_persons_needed_1_hour += abs(people_needed[i*2][j] - people_needed[i*2 + 1][j])
    file.close()
    
    return people_needed, num_persons_needed_2_hours, num_persons_needed_1_hour, fieldnames

#changes current persons hours based on the hours_multiplier list
def change_persons_hours(persons, num_shifts, fieldnames):
    for i in range(num_shifts):
        for j in range(len(fieldnames)):
            for k in range(len(persons)):
                if(persons[k].works_at_shift_and_task(i,j)):
                    persons[k].hours += 1
                    
#writes the hours to a new file
def write_hours(persons, hours_fieldnames, task_fieldnames, num_shifts):
    file = open('output/new_hours.csv', 'w')
    file.write(hours_fieldnames[0] + "," + hours_fieldnames[1] + "\n")
    
    change_persons_hours(persons, num_shifts, task_fieldnames)
    
    for i in range(len(persons)):
        file.write(persons[i].name + "," + str(persons[i].hours) + "\n")
    
    file.close()

#writes the schedule to a new file
def write_schedule_csv(persons, fieldnames, num_shifts):
    file = open('output/schedule.csv', 'w')
    for i in fieldnames:
        file.write("," + i)
    file.write("\n")
    for i in range(num_shifts):
        #beautify
        if(19 + i <= 24):
            file.write(str(19 + i))
        else:
            file.write(str(19 + i - 24))
        file.write("h - ")
        if(19 + i + 1 <= 24):
            file.write(str(19 + i + 1))
        else:
            file.write(str(19 + i + 1 - 24))
        file.write("h,")
        
        #searches every task and sees if a person with the same combination of shift and task is found
        for j in range(4):
            count = 0
            for k in range(len(persons)):
                if(persons[k].works_at_shift_and_task(i,j)):
                    file.write(persons[k].name)
                    if(count == 0):
                        file.write(" - ")
                        count += 1
                    
            file.write(",")
        file.write("\n")

    file.close()
    
#same as the top one, but for txt
def write_schedule_txt(persons, fieldnames, num_shifts):
    file = open('teste.csv', 'w')
    file.write("\t" + fieldnames[0] + "\t" + fieldnames[1] + "\t" + fieldnames[2] + "\t" + fieldnames[3] + "\n")
    for i in range(num_shifts):
        if(19 + i <= 24):
            file.write(str(19 + i))
        else:
            file.write(str(19 + i - 24))
        file.write("h - ")
        if(19 + i + 1 <= 24):
            str(19 + i + 1)
        else:
            str(19 + i + 1 - 24)
        file.write("h\t")
        for j in range(4):
            count = 0
            for k in range(len(persons)):
                if(persons[k].works_at_shift_and_task(i,j)):
                    file.write(persons[k].name)
                    if(count == 0):
                        file.write(" - ")
                        count += 1
                    
            file.write("\t")
        file.write("\n")

    file.close()












def generate_tasks_prefered(num, max):
    #repeats num of shifts
    for i in range (num):
        array = []
        #places max - 1 different elements in the array
        for j in range(max - 1):
            flag = True
            #appends a new item
            array.append(0)
            while flag:
                #generates a random number
                array[j] = round(random.randint(0,max - 1))
                flag = False
                #if its the same as one of the already added numbers,
                #the flag will be true and it repeats until its different
                for k in range(j):
                    if(array[j] == array[k]):
                        flag = True
                        break
        #places the last element in the array
        for j in range(max):
            flag = True
            #verifies if j is the same as any of the already added elements
            for k in range(max - 1):
                #if its the same, it repeats with a new j
                if(array[k] == j):
                    flag = False
                    break
            #if it is differetet, it appends and breaks
            if(flag):
                array.append(j)
                break
        #generates the string and prints it
        string = ""
        for j in range(max - 1):
            string += str(array[j]) + "-"
        string += str(array[max - 1])
        print(string)


#choose someone based on shift preference
def choose_person_shifts_prefered(person, people_needed, avoid_flag, second_schedule_flag):
    #goes through the person.shifts_prefered order
    for i in person.shifts_prefered:
        #goes through the person.tasks_prefered order
        for j in person.tasks_prefered:
            #if the avoid_flag is True, we respect the task and shift avoid choosen and we ignore
            #those schedules. However if it is False, we ignore the avoids
            if (avoid_flag == True and (j in person.tasks_to_avoid or i in person.shifts_to_avoid)):
                continue
            task = j
            shift = i
            #if the person already works at that shift, it checks if the shift before and after is available,
            #if that is the case, it is added
            if (person.works_at_shift(shift)):
                if(second_schedule_flag):
                    for k in person.tasks_prefered:
                        if(shift - 1 >= 0 and people_needed[shift - 1][k] > 0):
                            people_needed[shift - 1][k] = people_needed[shift - 1][k] - 1
                            person.schedule[1] = [shift - 1,k]
                            return 1
                        elif(shift + 1 < len(person.shifts_prefered) and people_needed[shift + 1][k] > 0):
                            people_needed[shift + 1][k] = people_needed[shift + 1][k] - 1
                            person.schedule[1] = [shift + 1,k]
                            return 1
                continue
            #if a space is available, it gets the person in that schedule
            if(int(people_needed[shift][task]) > 0):
                people_needed[shift][task] = people_needed[shift][task] - 1
                if(person.schedule[0][0] == -1):
                    person.schedule[0] = [shift,task]
                else:
                    person.schedule[1] = [shift,task]
                return 1
    return 0
            
def choose_person_tasks_prefered(person, people_needed, avoid_flag, second_schedule_flag):
    #goes through the person.tasks_prefered order
    for i in person.tasks_prefered:
        #goes through the person.shifts_prefered order
        for j in person.shifts_prefered:
            #if the avoid_flag is True, we respect the task and shift avoid choosen and we ignore
            #those schedules. However if it is False, we ignore the avoids
            if (avoid_flag == True and (i in person.tasks_to_avoid or j in person.shifts_to_avoid)):
                continue
            task = i
            shift = j
            #if the person already works at that shift, it checks if the shift before and after is available,
            #if that is the case, it is added
            if (person.works_at_shift(shift)):
                if(second_schedule_flag):
                    for k in person.tasks_prefered:
                        if(shift - 1 >= 0 and people_needed[shift - 1][k] > 0):
                            people_needed[shift - 1][k] = people_needed[shift - 1][k] - 1
                            person.schedule[1] = [shift - 1,k]
                            return 1
                        elif(shift + 1 < len(person.shifts_prefered) and people_needed[shift + 1][k] > 0):
                            people_needed[shift + 1][k] = people_needed[shift + 1][k] - 1
                            person.schedule[1] = [shift + 1,k]
                            return 1
                continue
            #if a space is available, it gets the person in that schedule
            if(int(people_needed[shift][task]) > 0):
                people_needed[shift][task] = people_needed[shift][task] - 1
                if(person.schedule[0][0] == -1):
                    person.schedule[0] = [shift,task]
                else:
                    person.schedule[1] = [shift,task]
                return 1
    return 0





if __name__ == "__main__":
    
    #CHANGE
    print("Number of shifts")
    num_shifts = int(input())
    print()
    
    #reads the persons and hours, sorts and reads the tasks
    persons = read_persons()
    hours_fieldnames = read_persons_hours(persons)
    #https://wiki.python.org/moin/HowTo/Sorting#Sortingbykeys
    persons = sorted(persons, key=lambda person: person.hours, reverse=True)
    (people_needed, num_persons_needed_2_hours, num_persons_needed_1_hour, tasks_fieldnames) = read_tasks_people()
    
    
    
    
    
    
    
    
    
    #data analysis
    num_overflow = 0
    
    if(len(persons) < num_persons_needed_1_hour + num_persons_needed_2_hours):
        print("CAREFULL!! SOME SCHEDULES ARE EMPTY")
        print("MORE SPACES THAN PEOPLE ARE AVAILABLE")
    else:
        num_overflow = len(persons) - (num_persons_needed_1_hour + num_persons_needed_2_hours)
        print(str(num_overflow) + " will not be working")
        
        if(num_persons_needed_1_hour > 0):
            print(str(num_persons_needed_1_hour) + " will only work 1 hour")
    
    
    
    
    
    
    
    
    
    
    
    
    
    #Adds who will be working 1 hour
    for i in range(num_overflow, num_overflow + num_persons_needed_1_hour):
        if(persons[i].preference == 1):
            if (choose_person_shifts_prefered(persons[i], people_needed, True, False) == 0):
                choose_person_shifts_prefered(persons[i], people_needed, False, False)
        else:
            if (choose_person_tasks_prefered(persons[i], people_needed, True, False) == 0):
                choose_person_tasks_prefered(persons[i], people_needed, False, False)
    
    #Adds who will be working 2 hours
    for i in range(num_overflow + num_persons_needed_1_hour, len(persons)):
        for j in range(2):
            if(persons[i].preference == 1):
                if (choose_person_shifts_prefered(persons[i], people_needed, True, j == 1) == 0):
                    choose_person_shifts_prefered(persons[i], people_needed, False, j == 1)
            else:
                if (choose_person_tasks_prefered(persons[i], people_needed, True, j == 1) == 0):
                    choose_person_tasks_prefered(persons[i], people_needed, False, j == 1)
    
    #prints the string for debugging
    for i in range(len(persons)):
        print(persons[i].string_working())













    
    #write in the files
    write_hours(persons, hours_fieldnames, tasks_fieldnames, num_shifts)
    write_schedule_csv(persons, tasks_fieldnames, num_shifts)

















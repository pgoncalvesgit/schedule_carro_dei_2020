# Schedule Carro Dei 2020 v1.0.0

## Index
- [Introdution](#Introdution)
- [Limitations and Bugs](#Limitations_and_Bugs)
- [Points](#Points)
- [Files](#Files)
- [Functions and Classes](#Functions_and_Classes)

## Introduction

This program lets you sort out the schedule for one night based on the preferences and dislikes of some taks or shifts.

## Limitations and Bugs

- Everyone works a maximum of 2 hours
- The schedule outputted might need some tweaking
- If someone is given, for example, the shift from 23 to 24 and then the shift from 22 to 23 or from 24 to 1 is available even though that person choose to avoid it, it will be given to her anyway.
- If there are less people than the number of people for 2 hours shifts plus the number of people for 1 hour shifts, some shifts will be empty

## Points

A point system needs to be in place.

In this version, points are in multiples of 5.

In order to win points, there are 2 ways. Either the program will give you points based on the shift you were working (19-20 isn't the same as 23-24), or by group acknowledgment (it is decided by supermajority(75%) that someone should be given more points for working more than they needed to).

In order to lose points, there are 3 ways. Either by group acknowledgment (it is decided by supermajority(75%) that someone should be taken points for working less than they needed to), by refusing to work on their given schedule for umknown or invalid reasons, or by "normalization" (if everyone has more than 15 points, for example, we can subtract 15 points to everyone)

## Files

### Program Files

#### Schedule.py

The program itself.

### Input Files

#### Number_people_tasks.csv

Has the number of people needed for each task at a given shift.

#### Tasks_points_multiplier.csv

Has the multiplier of each shift and task. The multiplier will be multiplied by 5 and added to the ammount of points the person doing the shift has.

#### People.csv

Every person with name, availability, tasks prefered, shifts prefered, tasks to avoid and shifts to avoid.

#### Points.csv

Every person's current points.

### Output Files

#### Schedule.csv

Schedule outputted by the program. It will have the name of the person, the shift and task that they will be performing. If 2 people share the same shift and task, they will be separated by a "-".

#### New_points.csv

Points everyone has after the program runs.

## Functions and Classes

### Person

Class that holds the information about a person. (name, availability, points, tasks prefered, shifts prefered, preference, given schedule, tasks to avoid, shifts to avoid.

#### Methods

##### works_at_shift(self, shift)

Checks if the person has the given shift.

Returns True or False.

##### works_at_shift_and_task(self, shift, task)

Checks if the person has the given task at the given shift.

Returns True or False

##### stringWorking(self)

Outputs a string for debugging with a custom message about the person's schedule.

##### stringTest(self):

Outputs a string for debugging with a custom message about the person.

### Hour_Row

Class with information about a row with "finos", "senhas", "shots" and "febras" has column titles (keys).

### read_persons()

Reads the people.csv file and outputs a list with every person available

### read_persons_points(persons)

Receives a list with every person available and reads the points.csv file. Changes every person's points to the points in the file.

### read_tasks_people()

Reads the number_people_tasks.csv file, counts the number of people needed and outputs:
 - A list with lists inside, which basically is a bi-dimmensional array, which holds information about the people needed at a given task and shift;
 - Number of people needed for 2 hour shifts.
 - Number of people needed for 1 hour shifts.

### read_points()

Reads the tasks_points_multiplier.csv file and outputs a list with lists inside, which basically is a bi-dimmensional array, which holds information about the point multiplier number for a given shift and task.

### change_persons_points()

Updates each person's points based on the shifts and tasks that they will do.

### write_points(persons)

Receives a list of people and writes each person's points to the new_points.csv file.

### write_schedule_csv(persons)

Receives a list of people and writes each person's schedule to the schedule.csv file.

### write_schedule_txt(persons)

Receives a list of people and writes each person's schedule to a schedule.txt file for copy and paste.

### generate_tasks_prefered(num, max)

Receives a number of random sequences to be generated (num), and a maximum number. It will generate "num" number of sequences of "max" different numbers, from 0 to "max" - 1. For example, if I choose (1,3), 0-2-1 is a valid output.

It is used just for testing purposes

### choose_person_shifts_prefered(person, people_needed, avoid_flag, second_schedule_flag)

For a certain person with preference set to 1, checks their preferences and the shifts available (people_needed). If the "avoid_flag" is set to True, the program will avoid the tasks and shifts that the person choose to avoid. If the "second_schedule_flag" is set to True, the program will try to make a schedule next to the shift the person already has.

It will be evaluating the tasks prefered for the shifts prefered.

### choose_person_tasks_prefered(person, people_needed, avoid_flag, second_schedule_flag)

Same as choose_person_shifts_prefered but instead of the person have the preference set to 1, it must be set to 0.

It will be evaluating the shifts prefered for the tasks prefered.








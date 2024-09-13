grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
sum_0 = sum(grades[0])
len_0 = len(grades[0])
sum_1 = sum(grades[1])
len_1 = len(grades[1])
sum_2 = sum(grades[2])
len_2 = len(grades[2])
sum_3 = sum(grades[3])
len_3 = len(grades[3])
sum_4 = sum(grades[4])
len_4 = len(grades[4])
average_grades_0 = sum_0/len_0
average_grades_1 = sum_1/len_1
average_grades_2 = sum_2/len_2
average_grades_3 = sum_3/len_3
average_grades_4 = sum_4/len_4
students = sorted(students)
average_grades = {students[0]:average_grades_0 ,  students[1]:average_grades_1 , students[2]:average_grades_2 , students[3]:average_grades_3 , students[4]:average_grades_4}
print(average_grades)



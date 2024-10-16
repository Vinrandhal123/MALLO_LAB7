#input the students identification 

student_name = input(input("enter student student name:"))
section = input(input("enter student student name:"))
prelim_grade = float(input("enter the prelim grade: "))
midterm_grade = float(input("enter the midterm grade:"))
finalterm_grade = float(input("enter the final grade:"))

#calculattion of final grad
if prelim_grade > 100 or midterm_grade > 100 or finalterm_grade > 100:
  print("invalid input, please input a grade from 40 to 100,")
  
elif prelim_grade < 40 or midterm_grade < 40 or finalterm_grade < 40:
   print("invalid input, please input a grade from 40 to 100,")
   
else:
  final_grade = prelim_grade * 0.3333 + midterm_grade * 0.3333 + finalterm_grade * 0.3333
  finalgraderound = round(final_grade)

if finalgraderound >= 99 and finalgraderound <= 100:
  print("has a grade percentage of () grade point of 1.00 snd her or she has an execellent remak")
elif finalgraderound <= 98 and finalgraderound >= 96:
  print("has a grade percentage of () grade point of 1.25 and she or she has an outstanding remak")
elif finalgraderound <= 95 and finalgraderound >= 93:
  print("has a grade percentage of () grade point of 1.50 and she or she has an superior remak")
elif finalgraderound <= 92 and finalgraderound >= 90:
  print("has a grade percentage of () grade point of 1.75 and she or she has a very good remak")
elif finalgraderound <= 89 and finalgraderound >= 87:
   print("has a grade percentage of () grade point of 2.00 and she or she has a good remark")
elif finalgraderound <= 86 and finalgraderound >= 84:
  print("has a grade percentage of () grade point of 2.25 and she or she has a satisfactory remark")
elif finalgraderound <= 83 and finalgraderound >= 81:
  print("has a grade percentage of () grade point of 2.50 and she or she has a fairly stisfactory remark")
elif finalgraderound <= 80 and finalgraderound >= 78:
  print("has a grade percentage of () grade point of 2.75 and she or she has a fari remak")
elif finalgraderound <= 77 and finalgraderound >= 75:
  print("has a grade percentage of () grade point of 3.00 and she or she has a passed remak")
elif finalgraderound <=75:
  print("has a grade percentage of () grade point of 5.00, faild")
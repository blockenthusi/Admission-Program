name = input("what is your name?")
print("welcome"  + name +  "to your admission portal")
grade = int(input("Enter Grade!"))

#this section shows the grading cateogories for possible admisssion
if grade <= 49:
    print ("No Admission")
elif grade >= 50 and grade <= 54 :
    print("you can only be admitted to Agric Department")
elif grade >= 55 and grade <= 60 :
    print("choose Botany or Zoology")
elif grade >= 61 and grade <= 70 :
    print("choose Computer Sci, Pschology, or Statistic")
elif grade >= 71 and grade <= 74 :
    print("choose Pharmacy or Physiology")
elif grade >= 75 and grade <= 79 :
    print("choose Banking and Finance, Insurance, or Accountancy")
else:
    print("choose Medicine or Law")



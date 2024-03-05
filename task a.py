#Problem 1 Exam Grading
try:
    print("Enter the student detail")
    student_name = str(input("Enter the student name: "))
    Roll_no = int(input("Enter the roll no: "))
# Obtained score
    maths_score = float(input("Enter marks in maths: "))
    chemistry_score = float(input("Enter marks in chemistry: "))
    physics_score = float(input("Enter marks in physics: "))
#student score
    overall_score = (physics_score + chemistry_score + maths_score)
    average_score = overall_score/3
    if maths_score >= 90:
     grade = "A"
    elif 80 <= maths_score < 90:
     grade = "B"
    elif 70 <= maths_score <80:
     grade = "C"
    elif 60 <= maths_score <70:
     grade = "D"
    else: grade = "F"
    print("grade in maths:",grade)



    if chemistry_score >= 90:
     
     grade = "A"
    elif 80 <= chemistry_score < 90:
     grade = "B"
    elif 70 <= chemistry_score <80:
     grade = "C"
    elif 60 <= chemistry_score <70:
     grade = "D"
    else: grade = "F"
    print("grade in chemistry: ",grade)

          

    if physics_score >= 90:
     grade = "A"
    elif 80 <= physics_score < 90:
     grade = "B"
    elif 70 <= physics_score <80:
     grade = "C"
    elif 60 <= physics_score <70:
     grade = "D"
    else: grade = "F"
    print("grade in physics: ",grade)
    print("\nHere is the grade card")
    print("student Name: ",student_name)
    print("student Roll no: ",Roll_no)
    print("Grade in maths: ",maths_score)
    print("Grade in chemistry:",chemistry_score)
    print("Grade in physics:",physics_score)
    print("overall grade: ",overall_score)



    if average_score >= 90:
     print("grade = A")
    elif 80 <= average_score < 90:
     grade = "B"
    elif 70 <= average_score <80:
     grade = "C"
    elif 60 <= average_score <70:
     grade = "D"
    else: grade = "F"
    print ("Overall grade: ",grade)
    print("Thank you")
#save details to a text file
    with open("output.txt", "w") as file:
        
        file.write("Student Name: " + student_name + "\n")
        file.write("Student Roll No.: " + str(Roll_no) + "\n")
        file.write("Grade in Maths: " + str(maths_score) + "\n")
        file.write("Grade in chemistry: " + str(chemistry_score) + "\n")
        file.write("Grade in physics: " + str(physics_score) + "\n")
        file.write("Overall Grade: " + grade + "\n")
except ValueError:
 print("Invalid input.")






    


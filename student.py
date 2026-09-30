def student_information():
    print("------student details---------")





    student_name = input("enter student name")
        
    student_regnumber = input("enter student id") 
        
    student_roomnumber = int(input("enter student room"))
        
    student_block = int(input("enter student block "))
    student_complaint = int(input("enter complaint description "))


    student = {
        "NAME OF STUDENT": student_name,
        "REGISTRATION NUMBER" : student_regnumber,
        "STUDENT BLOCK NUMBER" :student_block,
        "STUDENT ROOM NUMBER"  : student_roomnumber,

        "STUDENT COMPLAINT"     : student_complaint
        
    }
    return student

















    


    




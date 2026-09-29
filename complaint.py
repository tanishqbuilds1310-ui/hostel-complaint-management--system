COMPLAINTS = []
complaint_count = 0 
def add_complaint(student):
    global complaint_count
    student_name = input("enter student name")
    
    student_regnumber = input("enter student id") 
    
    student_roomnumber = int(input("enter student room"))
    
    student_block = int(input("enter student block "))
    student_complaint = int(input("enter complaint description "))
    complaint_count  =  complaint_count + 1

    complaint_id  = "C"  + str(complaint_count)
    print("COMPLAINT ID :", complaint_id)
    
    status = "pending"
    print("STATUS:" ,status)


    complaint = {
               "NAME OF STUDENT": student_name,
                      "REGISTRATION NUMBER" : student_regnumber,
                      "STUDENT BLOCK NUMBER" :student_block,
                      "STUDENT ROOM NUMBER"  : student_roomnumber,
                      "COMPLAINT COUNT"      : complaint_count,
                      "COMPLAINT ID"         : complaint_id,
                      "STATUS"               : status
    
    }



    COMPLAINTS.append(complaint)
    print("YOUR COMPLAINT REGISTERD SUCCESFULLY")





def view_complaint_status():
        search_id = input('enter compalaint_id :')
        found =False
        for complaint in COMPLAINTS:
                    
            if search_id == "COMPLAINT ID":
                        found = True
                        
        
            else:
                        found =  False
        
        
        if found == True:
                print(" found")
        
        
        
        else:
            print("no found")


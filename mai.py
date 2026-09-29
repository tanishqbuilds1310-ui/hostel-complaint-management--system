from complaint import add_complaint,view_complaint_status
from student import student_information


print('-------///// HOSTEL COMPLAINT MANAGEMENT SYSTEM /////--------')

while True:
               #MAIN MENU#
    print('1.Add complaint')
    print('2.view complaint status')
    print('3.Exit')


    choice = int(input("enter choice :  "))
    if choice == 1:
       student = student_information(student)
       add_complaint()




           
       


       

    elif choice == 2:
        

        view_complaint_status()



    elif choice == 3:
        print("thanks for visiting ")
        break



    else:
        print("your choice is invalid")




















        


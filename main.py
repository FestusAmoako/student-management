from console_colour import *
from student import Student

# creating database
student_database = []


# Welcome Screen msg
def welcome_screen():
    print(Yellow, '**** Welcome To NIIT Student Management System****')
    user_input = int(input("1. Add student\n"
                           "2. View All Student Details\n"
                           "3. Search For Student Details\n"
                           "4. Delete Student Info\n"
                           "5.Update Student Info\n"
                           "6. About System\n"
                           "7. Exit Application\n\n"
                           "Please Provide Your Request: "))
    user_options(user_input)


# user options

def user_options(user_input):
    if user_input == 1:
        response = 'yes'
        while response == 'yes':
            student_info = add_student_info()
            user_ans = input(BLUE + 'Do you want to save info?(Y/N):').lower()
            if user_ans == 'y':
                student_database.append(student_info)
                print(Green, f'{student_info.get_first_name()}'' '
                             f' {student_info.get_middle_name()}'' '
                             f'  {student_info.get_last_name()}'' '
                             f'     Your Details Have Been saved Successfully')
            elif user_ans == 'n':
                user_ans = input('Do You Really Want To Cancel(Y/N):').lower()
                if user_ans == 'y':
                    welcome_screen()
                else:
                    student_database.append(student_info)
            else:
                welcome_screen()
            response = input('is there another student? (yes/no)').lower()
        welcome_screen()

    elif user_input == 2:
        pass
    elif user_input == 3:
        pass
    elif user_input == 4:
        pass
    elif user_input == 5:
        pass
    elif user_input == 6:
        about_us()
    elif user_input == 7:
        close_program()
    else:
        invalid_request()


#  about us function

def about_us():
    print(BLUE, '*** This system keep track of student details')
    welcome_screen()


# close_ program function

def close_program():
    print(BLUE, 'Thank you for using the NIIT sms, Hope to see you again')
    exit(1)


def invalid_request():
    print(Red, 'Request Invalid, Please Try Again. Thank You')
    welcome_screen()


# add new student
def add_student_info():
    print(Yellow, '**** Fill Details Below To Add Student ****', White)
    sid = input('Provide Student Id: ')
    f_name = input('Provide First Name: ')
    m_name = input('Provide Middle Name:')
    l_name = input('Provide Last Name: ')
    dob = input('Provide Your Dob e.g (dd-mm-yy): ')
    course = input('Provide Your Course: ')
    period = int(input('Provide Your Period: '))

    #  Creating student object
    student_info = Student(sid, f_name, m_name, l_name, dob, course, period)
    return student_info


welcome_screen()

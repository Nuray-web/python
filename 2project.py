print("\n              Welcome to the registration app, dear User!")

persons = []
ccourses1 = []
ccourses = []
instructors = []
sstudents = []
scourse = {}

class subject:
    def __init__(self, sname, scode, sspeciality, cred, ects, instructor = 'Unknown'):
        subject.sname = sname
        subject.scode = scode
        subject.sspeciality = sspeciality
        subject.cred = cred
        subject.ects = ects
        subject.instructor = instructor
        #subject.maxPerson = maxPerson
        #subject.students = []
    def __repr__(self):
        return "    Course name: "+subject.sname+"\n    Course code: "+subject.scode+"\n    Course speciality: "+subject.sspeciality+"\n    Course credits: "+subject.cred+"\n    Course ects: "+subject.ects+"\n    Course's instructor: "+subject.instructor
    #def showStudents(self):
    #    return subject.students
    def __str__(self):
        return subject.sname + subject.scode

class person:
    def __init__(self, name, surname, age, nationality, email):
        person.name = name
        person.surname = surname
        person.age = age
        person.nationality = nationality
        person.email = email
    def __repr__(self):
        return "The person's name: "+person.name+"\n    The person's last name: "+person.surname+"\n    The person's age: "+str(person.age)+"\n    The person's nationality: "+person.nationality

class instructor(person):
    def __init__(self,name,surname,age,nationality,email,status,workplace,speciality,course,wemail):
        person.__init__(self,name,surname,age,nationality,email)
        person.workplace = workplace
        person.speciality = speciality
        person.course = course
        person.wemail = wemail
        person.email = email
        person.status = status
    def __repr__(self):
        return "Name: "+person.name+"\n    Last name: "+person.surname+"\n    Age: "+str(person.age)+"\n    Nationality: "+person.nationality+"\n    Workplace: "+person.workplace+"\n    Email: "+person.email+"\n    Status: "+person.status+"\n    Speciality: "+person.speciality+"\n    Courses: "+person.course+"\n    Workplace mail: "+person.wemail
    
class student(person):
    def __init__(self,name,surname,age,nationality,email,status,univer,speciality,idc,eemail):
        person.__init__(self,name,surname,age,nationality,email)
        person.univer = univer
        person.speciality = speciality
        #person.courses = courses
        person.idc = idc
        person.eemail = eemail
        person.email = email
        person.status = status
    def __repr__(self):
        return "Name: "+person.name+"\n    Last name: "+person.surname+"\n    Age: "+str(person.age)+"\n    Nationality: "+person.nationality+"\n    Email: "+person.email+"\n    Status: "+person.status+"\n    University: "+person.univer+"\n    Speciality: "+person.speciality+"\n    ID: "+person.idc+"\n    Educational mail: "+person.eemail

class manager:

    def addSubject():
        print("\n-----------------------------------------------------------------------------------------------\n")
        sname = input("\nPlease, enter the course's name: ")
        scode = input("Please, enter the course's code: ")
        sspeciality = input("Please, enter the course's speciality: ")
        cred = input("Please, enter the course's credits: ")
        ects = input("Please, enter the course's ects: ")
        Subject = subject(sname, scode, sspeciality, cred, ects).__repr__()
        Subject1 = subject(sname, scode, sspeciality, cred, ects).__str__()
        ccourses1.append(Subject1)
        ccourses.append(Subject)
        print("\n\n---   All courses   ---")
        for i in range(len(ccourses1)):
            print('\n<<< '+str(ccourses1[i])+' >>>')
        return ''  
    
    def printCourses(ccourses1):
        print("\n-----------------------------------------------------------------------------------------------\n")
        if bool(ccourses1) == False:
            return ("\n///   Sorry, there're no courses in registration list!   ///\n")
        else:
            for Subject1 in range(len(ccourses1)):
                print("\n")
                print(ccourses1[Subject1])
            return " "

    def registration():
        print("\n-----------------------------------------------------------------------------------------------\n")
        a =  int(input("\nPlease, enter the number of the persons you want to enroll: "))
        while a>0:
            name = input("\nPlease, enter the person's name: ")
            surname = input("Please, enter the person's last name: ")
            age = input("Please, enter the person's age: ")
            nationality = input("Please, enter the person's nationality: ")
            email = input("Please, enter the person's email: ")
            a -= 1
            Person = person(name, surname, age, nationality, email)
            check = input("Please, enter the status of the person (Instructor or Student): ")
            if check == 'Instructor' or check =='instructor' or check == 'inst':
                workplace = input("Please, enter the person's workplace: ")
                speciality = input("Please, enter the person's speciality: ")
                course = input("Please, enter the person's teaching course: ")
                wemail = name+'.'+surname+'@sdu.edu.kz'
                status = check
                Person = instructor(name,surname,age,nationality,email,status,workplace,speciality,course,wemail).__repr__()
                at = person.name + ' ' + person.surname
                print('\nEntered person:\n<<< '+ str(Person))
                instructors.append(at)
            elif check == 'Student' or check == 'student' or check == 'stud':
                univer = input("Please, enter the person's educational organization: ")
                speciality = input("Please, enter the person's studying speciality: ")
                idc = input("Please, enter the person's ID code: ")
                eemail = idc+'@stu.sdu.edu.kz'
                status = check
                Person = student(name,surname,age,nationality,email,status,univer,speciality,idc,eemail).__repr__()
                at = person.name + ' ' + person.surname
                sstudents.append(at)
                print('\nEntered person:\n<<< '+ str(Person))
            persons.append(Person)
        return '\n'

    def regOn():
        print("\n-----------------------------------------------------------------------------------------------\n")
        nameS = input("\nPlease, enter the name of the student you want to register on course: ")
        n = int(input("Please, enter the amount of courses: ")) 
        courseS = [str(n) for n in input("Please, enter the name of the course: ").split()]
        c = list(set(ccourses1) & set(courseS))
        if nameS in sstudents:
            if courseS == c:
                scourse[nameS] = c
            else:
                print("\n///   Sorry, invalid entry! There's no such course in registration app!   ///")
        else:
            print("\n///   Sorry, invalid entry! There's no such student in registration app!   ///")
        print('\n')
        for pair in scourse.items():
            print(pair, end='\n')
        return ''
    
    def request():
        call = input("Please, enter the name of the student whose courses you want to see: ")
        if call in scourse:
            print("\n///   The courses of given student: " + str(scourse.get(call)) + '   ///')
            return ''
        else:
            return "\n///   The given student hasn't registrated on any course!   ///"

    def showAllUsers():
        print("\n-----------------------------------------------------------------------------------------------\n")
        if bool(persons) == False:
            print("\n///   Sorry, there're no enrolled users!   ///\n")
        else:
            print("\n///   Enrolled users   ///")
            for i in range(len(persons)):
                print('\n<<< '+str(persons[i])+' >>>')
            confirm = input("\nIf you would like to see only students or only instructors list, please, enter one option: ")
            if confirm == 'stud' or confirm == 'student' or confirm == '1' or confirm == 'students' or confirm == 'Students' or confirm =='Student':
                if bool(sstudents) != False:    
                    for i in range(len(sstudents)):
                        print('\n<<< '+str(sstudents[i])+' >>>')
                else:
                    print("///   Sorry, there're no enrolled students!   ///")
            elif confirm == 'inst' or confirm == 'instructors' or confirm =='Instructors' or confirm =='instructor' or confirm =='Instructor' or confirm == '2':
                if bool(instructors) != False:    
                    for i in range(len(instructors)):
                        print('\n<<< '+str(instructors[i])+' >>>')
                else:
                    print("///   Sorry, there're no enrolled instructors!   ///")
            else:
                print("///   Sorry, invalid syntax! Please, check your answer!   ///")
        return ''

    while True:   #основной цикл       
        print("\n-----------------------------------------------------------------------------------------------\n")
        option = int(input("Menu Block:\n    1.Create a course\n    2.Show all courses\n    3.Enrolled users list\n    4.Enroll user\n    5.Register student on a course\n    6.Request student's course information\n    7.Exit\nPlease, enter the number of the option: "))
        while True:
            if option == 1:
                print(addSubject())
                break
            elif option == 2:
                print('\n<<<')
                print(printCourses(ccourses))
                print('>>>')
                break
            elif option == 3:
                print(showAllUsers())
                break
            elif option == 4:
                print(registration())
                break
            elif option == 5:
                print(regOn())
                break
            elif option == 6:
                print(request())
                break
            elif option == 7:
                exit()
            else:
                exit() 
        if option == 7:
            exit()      

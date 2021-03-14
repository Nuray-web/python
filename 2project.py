print("\n              Welcome to the registration app, dear User!")

persons = []
personn = []
desc = {}
ccourses1 = []
ccourses = []
instructors = []
sstudents = []
scourse = {}
tcourse = {}

class subject:
    def __init__(self, sname, scode, sspeciality, cred, ects):
        subject.sname = sname
        subject.scode = scode
        subject.sspeciality = sspeciality
        subject.cred = cred
        subject.ects = ects
    def __repr__(self):
        return "    Course name: "+subject.sname+"\n    Course code: "+subject.scode+"\n    Course speciality: "+subject.sspeciality+"\n    Course credits: "+subject.cred+"\n    Course ects: "+subject.ects
    def __str__(self):
        return subject.sname + subject.scode


class person:
    def __init__(self, name, surname, age, nationality, email):
        person.name = name
        person.surname = surname
        person.age = age
        person.nationality = nationality
        person.email = email
        global esim
        esim = person.name + ' ' + person.surname
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
        return "Name: "+person.name+"\n    Last name: "+person.surname+"\n    Age: "+str(person.age)+"\n    Nationality: "+person.nationality+"\n    Workplace: "+person.workplace+"\n    Email: "+person.email+"\n    Status: "+person.status+"\n    Speciality: "+person.speciality+"\n    Workplace mail: "+person.wemail
    def __str__(self):
        if esim in tcourse:
            return '\n    Teaching courses: ' + tcourse[esim]
        else:
            return '\n    Teaching courses: ' + person.course
    
class student(person):
    def __init__(self,name,surname,age,nationality,email,status,univer,speciality,idc,eemail):
        person.__init__(self,name,surname,age,nationality,email)
        person.univer = univer
        person.speciality = speciality
        person.idc = idc
        person.eemail = eemail
        person.email = email
        person.status = status
    def __repr__(self):
        return "Name: "+person.name+"\n    Last name: "+person.surname+"\n    Age: "+str(person.age)+"\n    Nationality: "+person.nationality+"\n    Email: "+person.email+"\n    Status: "+person.status+"\n    University: "+person.univer+"\n    Speciality: "+person.speciality+"\n    ID: "+person.idc+"\n    Educational mail: "+person.eemail

class manager:

    def addSubject():
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
            print('\n    <<< '+str(ccourses1[i])+' >>>')
        return ''  
    
    def printCourses(ccourses1):
        if bool(ccourses1) == False:
            return ("\n---   Sorry, there're no courses in registration list!   ---\n")
        else:
            for Subject1 in range(len(ccourses1)):
                print("\n")
                print(ccourses1[Subject1])
            return " "

    def registration():
        a =  int(input("\nPlease, enter the number of the persons you want to enroll: "))
        while a>0:
            name = input("\nPlease, enter the person's name: ")
            surname = input("Please, enter the person's last name: ")
            age = input("Please, enter the person's age: ")
            nationality = input("Please, enter the person's nationality: ")
            email = input("Please, enter the person's email: ")
            a -= 1
            Person = person(name, surname, age, nationality, email)
            check = input("Please, enter the status of the person (Instructor or Student | 1 or 2): ")
            if check == 'Instructor' or check =='instructor' or check == 'inst' or check == '1':
                workplace = input("Please, enter the person's workplace: ")
                speciality = input("Please, enter the person's speciality: ")
                wemail = name+'.'+surname+'@sdu.edu.kz'
                status = 'Instructor'
                course = 'Unassigned'
                at = person.name + ' ' + person.surname
                instructors.append(at)
                personn.append(at)
                Person = instructor(name,surname,age,nationality,email,status,workplace,speciality,course,wemail).__repr__()
                co = instructor(name, surname, age, nationality, email, status, workplace, speciality, course, wemail).__str__()
                desc[at] = instructor(name,surname,age,nationality,email,status,workplace,speciality,course,wemail).__repr__()
                print('\nEntered person:\n\n<<< '+ str(Person)+'    '+str(co))
            elif check == 'Student' or check == 'student' or check == 'stud' or check == '2':
                univer = input("Please, enter the person's educational organization: ")
                speciality = input("Please, enter the person's studying speciality: ")
                idc = input("Please, enter the person's ID code: ")
                eemail = idc+'@stu.sdu.edu.kz'
                status = 'Student'
                Person = student(name,surname,age,nationality,email,status,univer,speciality,idc,eemail).__repr__()
                at = person.name + ' ' + person.surname
                sstudents.append(at)
                personn.append(at)
                desc[at] = student(name,surname,age,nationality,email,status,univer,speciality,idc,eemail).__repr__()
                print('\nEntered person:\n<<< '+ str(Person))
            persons.append(Person)
        return '\n'

    def regOn():
        if bool(sstudents) == False:
            return("\n---   Sorry, there're no registrated students!   ---\n")
        else:
            if bool(ccourses1) == False:
                return("\n---   Sorry, there're no registrated courses!   ---\n")
            else:
                nameS = input("\nPlease, enter the name of the student you want to register on course: ")
                if nameS in sstudents:
                    n = int(input("Please, enter the amount of courses: "))
                    courseS = [str(n) for n in input("Please, enter the name of the course: ").split( )]
                    c = list(set(ccourses1) & set(courseS))
                    if courseS == c:
                        if nameS not in scourse:
                            scourse[nameS] = c
                        else:
                            scourse[nameS] = scourse[nameS] + c
                    else:
                        print("\n---   Sorry, invalid entry! There's no such course in registration app!   ---")
                else:
                    print("\n---   Sorry, invalid entry! There's no such student in registration app!   ---")
                print('\n')
                for pair in scourse.items():
                    print(pair, end='\n')
                return ''
    
    def request():
        if bool(sstudents) == False:
            return "\n---   Sorry, there're no registrated students!   ---\n"
        else:
            call = input("Please, enter the name of the student whose information you want to see: ")
            if call in desc:
                print("\n<<< " + str(desc[call]) + " >>>")
                if call in scourse:
                    print("\n---   The courses of given student: " + str(scourse.get(call)) + '   ---')
                    return ''
                else:
                    return "\n---   The given student hasn't registrated on any course!   ---" 
            else:
                return "\n---   The given student hasn't registrated!   ---"
    
    def req():
        if bool(instructors) == False:
            return "\n---   Sorry, there're no registrated instructors!   ---\n"
        else:
            call = input("Please, enter the name of the instructor whose courses you want to see: ")
            if call in desc:
                print("\n<<< " + str(desc[call]) + " >>>")
                if call in tcourse:
                    print("\n---   The courses of given instructor: " + str(tcourse.get(call)) + '   ---')
                    return ''
                else:
                    return "\n---   The given instructor hasn't assigned on any course!   ---"
                
            else:
                return "\n---   The given instructor hasn't registrated!   ---"

    def showAllUsers():
        if bool(personn) == False:
            print("\n---   Sorry, there're no enrolled users!   ---\n")
        else:
            print("\n---   Enrolled users   ---\n")
            for i in range(len(personn)):
                print('  <<< '+str(personn[i])+' >>>')
            confirm = input("\nIf you would like to see only students or only instructors list, please, enter one option: ")
            print('\n')
            if confirm == 'stud' or confirm == 'student' or confirm == '1' or confirm == 'students' or confirm == 'Students' or confirm =='Student':
                if bool(sstudents) != False:    
                    for i in range(len(sstudents)):
                        print('<<< '+str(sstudents[i])+' >>>')
                else:
                    print("\n---   Sorry, there're no enrolled students!   ---")
            elif confirm == 'inst' or confirm == 'instructors' or confirm =='Instructors' or confirm =='instructor' or confirm =='Instructor' or confirm == '2':
                if bool(instructors) != False:    
                    for i in range(len(instructors)):
                        print('<<< '+str(instructors[i])+' >>>')
                else:
                    print("\n---   Sorry, there're no enrolled instructors!   ---")
            else:
                print("\n---   Sorry, invalid syntax! Please, check your answer!   ---")
        return ''

    def assign():
        if bool(instructors) == False:
            return "\n---   Sorry, there're no enrolled instructors!   ---\n"
        else:
            name = input("Please, enter the name of the instructor: ")
            if name in instructors:
                n = int(input("Please, enter the amount of courses: ")) 
                coursename = [str(n) for n in input("Please, enter the name of the course: ").split( )]
                c = list(set(ccourses1) & set(coursename))
                if coursename == c:
                    if name not in tcourse:
                        tcourse[name] = c
                    else:
                        tcourse[name] = tcourse[name] + c
                else:
                    print("\n---   Sorry, invalid entry! There's no such course in registration app!   ---")
            else:
                print("\n---   Sorry, invalid entry! There's no such instructor in registration app!   ---")
            print('\n')
            for pair in tcourse.items():
                print(pair, end='\n')
            return ''


    while True:   #основной цикл   
        print("\n-----------------------------------------------------------------------------------------------\n")    
        option = int(input("Menu Block:\n    1.Create a course\n    2.Show all courses\n    3.Enrolled users list\n    4.Enroll user\n    5.Register student on a course\n    6.Request student's information\n    7.Assign instructor\n    8.Request instructor's information\n    9.Exit\nPlease, enter the number of the option: "))
        while True:
            if option == 1:
                print("\n-----------------------------------------------------------------------------------------------\n")
                print(addSubject())
                break
            elif option == 2:
                print("\n-----------------------------------------------------------------------------------------------\n")
                print("---   Courses   ---")
                print(printCourses(ccourses))
                break
            elif option == 3:
                print("\n-----------------------------------------------------------------------------------------------\n")
                print(showAllUsers())
                break
            elif option == 4:
                print("\n-----------------------------------------------------------------------------------------------\n")
                print(registration())
                break
            elif option == 5:
                print("\n-----------------------------------------------------------------------------------------------\n")
                print(regOn())
                break
            elif option == 6:
                print("\n-----------------------------------------------------------------------------------------------\n")
                print(request())
                break
            elif option == 7:
                print("\n-----------------------------------------------------------------------------------------------\n")
                print(assign())
                break
            elif option == 8:
                print("\n-----------------------------------------------------------------------------------------------\n")
                print(req())
                break
            elif option == 9:
                exit()
            else:
                exit() 
        if option == 9:
            exit()      

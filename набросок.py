print("\n              Welcome to the registration app, dear User!")
print("\n---------------------------------------------------------------------------\n")

class person:
    def __init__(self, name, surname, age, nationality, motherland, email):
        person.name = name
        person.surname = surname
        person.age = age
        person.nationality = nationality
        person.motherland = motherland
        person.email = email
    def __repr__(self):
        return "The person's name: "+person.name+"\n    The person's last name: "+person.surname+"\n    The person's age: "+str(person.age)+"\n    The person's nationality: "+person.nationality+"\n    The person's motherland: "+person.motherland

class instructor(person):
    def __init__(self,name,surname,age,nationality,motherland,email,status,workplace,speciality,course,wemail):
        person.__init__(self,name,surname,age,nationality,motherland,email)
        person.workplace = workplace
        person.speciality = speciality
        person.course = course
        person.wemail = wemail
        person.email = email
        person.status = status
    def __repr__(self):
        return "Name: "+person.name+"\n    Last name: "+person.surname+"\n    Age: "+str(person.age)+"\n    Nationality: "+person.nationality+"\n    Motherland: "+person.motherland+"\n    Workplace: "+person.workplace+"\n    Email: "+person.email+"\n    Status: "+person.status+"\n    Speciality: "+person.speciality+"\n    Courses: "+person.course+"\n    Workplace mail: "+person.wemail
    
class student(person):
    def __init__(self,name,surname,age,nationality,motherland,email,status,univer,speciality,courses,idc,eemail,cred,ects):
        person.__init__(self,name,surname,age,nationality,motherland,email)
        person.univer = univer
        person.speciality = speciality
        person.courses = courses
        person.idc = idc
        person.eemail = eemail
        person.email = email
        person.status = status
        person.cred = cred        #19-30
        person.ects = ects        #20-40
        
    def __repr__(self):
        return "Name: "+person.name+"\n    Last name: "+person.surname+"\n    Age: "+str(person.age)+"\n    Nationality: "+person.nationality+"\n    Motherland: "+person.motherland+"\n    Email: "+person.email+"\n    Status: "+person.status+"\n    University: "+person.univer+"\n    Speciality: "+person.speciality+"\n    ID: "+person.idc+"\n    Educational mail: "+person.eemail+"\n    Credits: "+person.cred+"\n    Ects: "+person.ects

    def showCourses(self):
        return person.courses


class subject:
    persons = []
    a =  int(input("Please, enter the number of the persons you want to enroll: "))
    while a>0:
        name = input("\nPlease, enter the person's name: ")
        surname = input("Please, enter the person's last name: ")
        age = input("Please, enter the person's age: ")
        nationality = input("Please, enter the person's nationality: ")
        motherland = input("Please, enter the person's motherland: ")
        email = input("Please, enter the person's email: ")
        a -= 1
        Person = person(name, surname, age, nationality, motherland, email)
        check = input("Please, enter the status of the person (Instructor or Student): ")
        if check == 'Instructor' or check =='instructor' or check == 'inst':
            workplace = input("Please, enter the person's workplace: ")
            speciality = input("Please, enter the person's speciality: ")
            course = input("Please, enter the person's teaching course: ")
            wemail = name+'.'+surname+'@sdu.edu.kz'
            status = check
            Person = instructor(name,surname,age,nationality,motherland,email,status,workplace,speciality,course,wemail).__repr__()
            print('\nEntered person:\n<<< '+ str(Person))
            print('\n----------------------------------------')
        elif check == 'Student' or check == 'student' or check == 'stud':
            univer = input("Please, enter the person's educational organization: ")
            speciality = input("Please, enter the person's studying speciality: ")
            idc = input("Please, enter the person's ID code: ")
            eemail = idc+'@stu.sdu.edu.kz'
            status = check
            courses = []
            ncourses = int(input("Please, enter the amount of taken cources: "))
            for i in range(ncourses):
                courses.append(input("Please, enter the name of the course: "))
            cred = input("Please, enter the person's currently taking credits: ")
            ects = input("Please, enter the person's currently taking ects: ")
            Person = student(name,surname,age,nationality,motherland,email,status,univer,speciality,courses,idc,eemail,cred,ects).__repr__()
            Courses = student(name,surname,age,nationality,motherland,email,status,univer,speciality,courses,idc,eemail,cred,ects).showCourses()
            print('\nEntered person:\n<<< '+ str(Person))
            print("\nCourses: ")
            print(Courses)
            print('\n----------------------------------------')
        persons.append(Person)
    for i in range(len(persons)):
        print('\n<<< '+str(persons[i])+' >>>\n')

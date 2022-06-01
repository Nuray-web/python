#new project
class subject: #основной класс
    def __init__(self, persons, idcode, fio, sp, code, cred, ects): #инициализация
        self.persons = []
        self.idcode = idcode
        self.fio = fio
        self.sp = sp #for speciality
        self.code = code
        self.cred = cred
        self.ects = ects
    def registration(self,person):
        self.persons.append(person)
    def from_input(person):
        return person(input("Please, enter the id: "), input("Please, enter the fio: "), input("Please, enter the sp: "), input("Please, enter the code: "), input("Please, enter the cred: "), input("Please, enter ects: "))
    def __str__(self, idcode, fio, sp, code, cred, ects):
        print(self.idcode, self.fio, self.sp, self.code, self.cred, self.ects)

class person:
    class instructor:
        def __init__(self, idcode, fio, email, course):
            self.idcode = idcode
            self.fio = fio
            self.email = email
            self.course = course
            

reg = subject()
reg.from_input(person())

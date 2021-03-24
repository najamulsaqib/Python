class Student:
    #class variables
    # class variables should be on top pf __init__ method
    institute = "Superior College"
    # you can acces class variables through self. and Class name (Student.) in both these methods
    def __init__(self, name, section, rollno):
        #instance variables
        self.name = name
        self.section = section
        self.rollno = rollno 
    def Show(self):
        print("Hi {}! Your section is {} and Roll no is {} and institue is {}".format(self.name, self.section, self.rollno, Student.institute))

S1 = Student("Najam", "5B", "BSEM-F18-007")
S2 = Student("Saqib", "5B", "Bsewm-F18-001")

S1.Show()
S2.Show()
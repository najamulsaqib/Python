class Student:
    Ins = "Shahbaz Gill"
    # Constructor 
    def __init__(self, name, section, rollno):
        self.name = name
        self.section = section
        self.rollno = rollno 
        
    # Instance Method
    def Show(self):
        print("Hi {}! Your section is {} and Roll no is {}".format(self.name, self.section, self.rollno))
    #Setters & getters (Instance Variable)
    # Setter
    def setName(self, name):
        self.name = name
    #Getter
    def getName(self):
        return self.name

    #Class Methods
    @classmethod
    def Instructor(cls):
        print(Student.Ins)
    
    #Static method
    @staticmethod
    def Rights():
        print("All Rights Reserved by NjM.co")

# Creating Class Objects
S1 = Student("Najam", "5B", "BSEM-F18-007")
S2 = Student("Saqib", "5B", "Bsewm-F18-001")

# Calling Instance methods
S1.Show()
S2.Show()

# Calling Setters & Getters
S1.setName("Bhatti")
print(S1.getName())

# Calling Class Methods
Student.Instructor()

# Calling Static methods
Student.Rights()
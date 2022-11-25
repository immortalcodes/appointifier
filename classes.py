class student_details(object):
    def __init__(self,Name="Shriya",ID="12067890"):
        __name = Name
        __id = ID
    def updateName(self,value,token):
        if token == "Valid":
            self.name = value

    def updateID(self,value,token):
        if token == "Valid":
            self.id = value
    def appointmentTime(self,valueTime,token):
        if token == "Valid":
            self.time = valueTime        

class Professor_details(object):
    def __init__(self,Name="Dr. Raveendra Sharma",ID="12067890"):
        __name = Name
        __id = ID
    def updateName(self,value,token):
        if token == "Valid":
            self.name = value

    def updateID(self,value,token):
        if token == "Valid":
            self.id = value
    def availableTime(self,valueTime,token):
        if token == "Valid":
            self.time = valueTime 
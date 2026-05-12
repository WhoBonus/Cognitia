#Student Class
class student:
    def __init__(self, studentID: int, name: str, marks: float):
        self._studentID = studentID
        self._name = name
        self._marks = marks
    #Getters: Get ID, get Name, get Marks
    def getID(self) -> int:
        return self._studentID
    def getName (self) -> str:
        return self._name
    def getMarks(self) -> float:
        return self._marks 
    
    #Setters above
    def setID(self, studentID: int):
            self._studentID = studentID 
    def setName (self, name: str):
            self._name = name 
    def setMarks (self, marks: float):
            self._marks = marks 

#Main Class
class Main:
    #Get the top student method
    def topStudent(students: list[student]):
        topStudent = students[0]
        for student in students:
            if student.getMarks() > topStudent.getMarks():
                topStudent = student

        print(f"Top Student: {topStudent.getName()} has {topStudent.getMarks()} marks.")
        

    def main():
        #Sample
        students = [
            student(1, "Alice", 80.0),
            student(2, "Bob", 90.0),
            student(3, "Charlie", 100.0)
        ]
        Main.topStudent(students)
        
if __name__ == "__main__":
    Main.main()

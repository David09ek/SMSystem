import mysql.connector
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Davidsql@09",
    database = "student"
)
cursor = mydb.cursor()
class Student:
    def insert_student(self,first_name,last_name,gpa):
            cursor.execute("INSERT INTO student_info (first_name, last_name,gpa) VALUES(%s,%s,%s)", (first_name,last_name,gpa))
            mydb.commit()

    def get_student_by_id(self,student_id):
        cursor.execute("SELECT * FROM  student_info WHERE student_id = %s", (student_id,))
        return cursor.fetchone()

    def update_gpa(self):
        cursor.execute("UPDATE student_info SET gpa = %s WHERE student_id = %s")
        mydb.commit()

    def get_all(self):
        cursor.execute("SELECT * FROM student_info")
        return cursor.fetchall()

    
info = Student()
info.insert_student("David", "Ekeleme", 4.8)
# print(info.get_student_by_id(2))
print(info.get_all())





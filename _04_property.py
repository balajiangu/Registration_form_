import mysql.connector


def create_table():
    a = mysql.connector.connect(
        host = "localhost",
        user = "root",
        database = "Registration",
        password = "Arvb73@#"
    )



    #create cursor
    cursor = a.cursor()



    #write query
    query = "Create table registration_form(Name_of_the_Student varchar(30),DOB date,Email Varchar(30),Father_Name varchar(20),Mother_Name varchar(20),Gender Varchar(10),Nationality Varchar(20),Address Varchar(200),Mobile bigint,12th_School_Name Varchar(50),12th_Total_Mark int,10th_School_Name Varchar(50),10th_Total_Mark int,Course_Choice Varchar(50),Why_You_Want_To_Join_Here Varchar(100))"

    #execute query
    cursor.execute(query)


    #commit
    a.commit()



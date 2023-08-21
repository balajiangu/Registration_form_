import mysql.connector
from _04_property import create_table



#this function is used to create data
def insert_table(get_from_UI):
    a = mysql.connector.connect(
        host = "localhost",
        user = "root",
        database = "Registration",
        password = "Arvb73@#"
    )

    #create cursor
    cursor = a.cursor()

    #values
    values = tuple(get_from_UI.values())

    #write query
    query = "Insert into registration_form values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

    #execute query
    cursor.execute(query,values)

    #commit
    a.commit()

    return "Registered Successfully!"




#this function is used to Retrive data
def view_table():
    a = mysql.connector.connect(
        host = "localhost",
        user = "root",
        database = "Registration",
        password = "Arvb73@#"
    )

    #create cursor
    cursor = a.cursor()

    #write query
    query = "Select * from registration_form"

    #execute query
    cursor.execute(query)
    record = cursor.fetchall()
    for i in record:
        print(i)

    #commit
    a.commit()

    return "-------------Data Get Successfully!------------"



#this function is used to update data

def update_value(new_name,old_name):
    a = mysql.connector.connect(
        host = "localhost",
        user = "root",
        database = "Registration",
        password = "Arvb73@#"
    )



    #create cursor
    cursor = a.cursor()



    #write query
    query = "Update registration_form set Name_of_the_Student = '{}' where  Name_of_the_Student = '{}' ".format(new_name,old_name)

    #execute query
    cursor.execute(query)


    #commit
    a.commit()

    return "------data updated successfully-------"




#this function is used to delete data
def delete_value(stri):
    a = mysql.connector.connect(
        host = "localhost",
        user = "root",
        database = "Registration",
        password = "Arvb73@#"
    )



    #create cursor
    cursor = a.cursor()



    #write query
    query = "Delete from  registration_form where Name_of_the_Student = '{}'".format(stri)

    #execute query
    cursor.execute(query)


    #commit
    a.commit()

    return "------data deleted successfully-------"




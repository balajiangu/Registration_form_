from flask import Flask,request,render_template
from _02_service import service_fun,service_fun_view,service_fun_delete ,service_fun_update

app = Flask(__name__)

#this is the function which is used for testing
@app.route("/")
def test():
    return render_template('register.html')

#this is the function which is used for create the records
@app.route("/hello/student", methods = ["post"])
def create():
    Name_of_the_Student = request.form.get("sname")
    DOB = request.form.get("sdob")
    Email = request.form.get("semail")
    Father_Name = request.form.get("sfname")
    Mother_Name = request.form.get("smname")
    Gender = request.form.get("sgender")
    Nationality = request.form.get("snational")
    Address = request.form.get("saddress")
    Mobile = request.form.get("smobile")
    School_Name_12_th = request.form.get("s12school")
    Total_12_th = request.form.get("s12total")
    School_Name_10_th = request.form.get("s10school")
    Total_10_th= request.form.get("s10total")
    Course_Choice = request.form.get("scc")
    Why_You_Want_To_Join_Here = request.form.get("swh")

    get_from_UI = {
        "name":Name_of_the_Student,
         "date_of_birth":DOB,
         "emailid":Email,
         "fname":Father_Name,
         "mname":Mother_Name,
         "gender":Gender,
         "nation":Nationality,
         "address":Address,
         "mobile":Mobile,
         "school_N_12":School_Name_12_th,
         "school_T_12":Total_12_th,
         "school_N_10":School_Name_10_th,
         "school_T_10":Total_10_th,
         "course":Course_Choice,
         "reason":Why_You_Want_To_Join_Here
         }

    print("The data is : ",get_from_UI)
    x = service_fun(get_from_UI)
    print("Data stored successfully!")
    return x




# this is the function which is used for retriving data
@app.route("/select",methods = ["GET"])
def select():
    get_from_databse = service_fun_view()
    return get_from_databse



#this is the function which is used for update data
#------> i have used Postman
@app.route("/update",methods = ["put"])
def update():
    old_name1 = tuple(request.get_json().values())
    old_name = ""
    for i in old_name1:
        old_name += i
    new_name = input("enter the new name:")
    hello = service_fun_update(new_name,old_name)
    return hello


#this is the function which is used for update data
#------> i have used Postman
@app.route("/delete",methods = ["Delete"])
def delete():
    delete_student_name = tuple(request.get_json().values())
    # print(delete_student_name,type(delete_student_name))
    stri = ""
    for i in delete_student_name:
        stri += i
    hi = service_fun_delete(stri)
    return hi


if __name__ == "__main__":
    app.run(debug=True)
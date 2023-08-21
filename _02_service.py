from  _03_dao import insert_table,view_table,update_value,delete_value

#this function is used to create data
def service_fun(get_from_UI):
    y = insert_table(get_from_UI)
    return y



#this function is used to retrive data
def service_fun_view():
    y = view_table()
    return y


#this function is used to update data
def service_fun_update(new_name,old_name):
    yy = update_value(new_name,old_name)
    return yy



#this function is used to delete data
def service_fun_delete(stri):
    y = delete_value(stri)
    return y


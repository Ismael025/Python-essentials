def inform_employee(empoyees):
    for employee_id, details in employees.items():
        print(f"Hello {details['name']}", f"Your department is, {details['department']}")
        
employees = {
    
    101:{'name':'Ismael', 'department':'Comp Engineering'},
    102:{'name':'gedeon', 'department':'Comp science'},
    103:{'name':'Fils', 'department':' IT'},
    104:{'name':'Patrick', 'department':'civil Engineering'},
    105:{'name':'Daniel', 'department':'Film making'},
    106:{'name':'Jado', 'department':'software Engineering'}
}

inform_employee(employees)
    
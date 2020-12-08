import Controllers.employee_controller as ec
import Controllers.stores_controller as sc
from MongoDB.Models.employees import Employee
from UI.product_menu import input_int_validation


def fire_message(employee, reason):
    if reason == 1:
        print(f"{employee.employee_last_name} was successfully fired for his terrible smell")

    elif reason == 2:
        print(f"{employee.employee_last_name} was let go because he just couldn't keep his mouth shut")
    # ----MySQL----
    # elif reason == 3:
    #     valuables = ec.theft(employee)
    #     print(
    #         f"Ouch, looks like you fired {employee.employee_name} {employee.employee_lastname} and he wasn't happy"
    #         f" with the reason you gave gim. \nHe ran off in your customer {valuables[2]}s"
    #         f" {valuables[1].customer_car_brand} with {valuables[0][0]} {valuables[0][1]}s from your office in "
    #         f"{employee.store.store_name}"
    #     )

    elif reason == 3:
        amount, item, customer = ec.theft(employee)
        print(
            f"Ouch, looks like you fired {employee.employee_first_name} {employee.employee_last_name} and he wasn't happy"
            f" with the reason you gave gim. \nHe ran off in your customer {customer.customer_first_name}s"
            f" {customer.cars[0]['customer_car_brand']} with {amount} {item.description}s from your office in "
            f"{employee.store.store_name}"
        )


def fire_employee(employee):
    while True:
        print(f"Give {employee.employee_last_name} reason for being fired".center(30, " "))
        print("=" * 30)
        print("1. The smell is unbearable")
        print("2. That one time on the company christmas party")
        print("3. Your not a fan if Star Wars")
        print("0. Exit")

        selection = input_int_validation("Thread carefully, your carisma lvl is low!")

        if selection == 1:
            fire_message(employee, selection)
            ec.fire_employee(employee)
            break

        elif selection == 2:
            fire_message(employee, selection)
            ec.fire_employee(employee)
            break

        elif selection == 3:
            fire_message(employee, selection)
            ec.fire_employee(employee)
            break

        elif selection == 0:
            print("Unable")


def employee_edit_menu(employee):
    while True:
        print("Edit employee menu".center(30, " "))
        print("=" * 30)
        print(f"1. Show orders handled by {employee.employee_last_name}")
        print(f"2. Fire {employee.employee_last_name}")
        print("0. Exit")

        selection = input_int_validation("Menu selection")

        if selection == 1:
            # ----MySQL----
            # print(
            #     ("\n".join(f"Order {count} at {order.order_date}".center(30, " ") +
            #                f"\n{details.spare_part.description} \t quantity: {details.quantity}"
            #                for count, order in enumerate(employee.orders, 1) for details in order.order_lines))
            # )
            print("\n".join(f"Order {count} at {order.order_date}".center(30, " ") +
                            f"\n{details['spare_part'].description} \t quantity: {details['quantity']}"
                            for count, order in enumerate(employee.orders, 1) for details in order.order_detail))

        elif selection == 2:
            fire_employee(employee)
            break

        elif selection == 0:
            break


def find_employee_by_store():
    store = search_store()
    print("Employees working in this store: ")
    print("\n".join(f"{i}. {employee.employee_first_name} {employee.employee_last_name}"
                    for i, employee in enumerate(store.employees, 1)))

    selection = input_int_validation("\nChoose an employee")

    return store.employees[selection - 1]


def select_employee_menu():
    while True:
        print("Select employee menu".center(30, " "))
        print("=" * 30)
        print("Search employee by:")
        print("1. First name")
        print("2. Store")
        print("0. Exit")

        # ----MySQL----
        # selection = input_int_validation("Enter employee ID")

        selection = input_int_validation("Menu selection")

        if selection == 0:
            break
        # ----MySQL----
        # employee = ec.get_employee_by_id(selection)

        if selection == 1:
            selection = input("Enter employee first name: ")
            employee = ec.get_employee_by_first_name(selection)

            if employee is not None:
                employee_edit_menu(employee)
            else:
                print(f"There's no one named {selection} working in our stores")
                continue

        if selection == 2:
            employee = find_employee_by_store()
            employee_edit_menu(employee)

        else:
            print(f"\nMenu selection {selection} is not a valid option!\n")


def search_store(name=None):
    if name is not None:
        print(f"Where should {name} work?".center(30, " "))
        print("=" * 30)

    else:
        print(f"Choose a store".center(30, " "))
        print("=" * 30)

    stores = sc.get_all_stores()

    print("\n".join(f"{i}. {store.store_address} in {store.store_name}" for i, store in enumerate(stores, 1)))

    selection = input_int_validation("Enter number: ")

    return stores[selection - 1]


def verify_employee(employee):
    print("OBS!".center(30, "-"))
    print(
        f"First name: {employee.employee_first_name}\n"
        f"Last name: {employee.employee_last_name}\n"
        f"Phone: {employee.employee_phone_nr}\n"
        f"Email: {employee.employee_email}\n"
        f"Store: {employee.store.store_name}\n"
    )

    selection = input_int_validation("Is the information correct?\n(1). Yes\n(2). No\n")

    return selection == 1


def add_employee_menu():
    print("Add employee menu".center(30, " "))
    print("=" * 30)

    employee_dict = {f"employee_{i.replace(' ', '_').lower()}": input(f"{i}: ") for i in
                     ["First name", "Last name", "Phone nr", "Email"]}

    store = search_store(employee_dict["employee_first_name"])

    employee_dict.update({"store_id": store._id})
    employee = Employee(employee_dict)

    if verify_employee(employee):
        employee = ec.save_employee(employee_dict)
        print(f"{employee.employee_first_name} {employee.employee_last_name} is saved and set to work in our store in {store.store_name}")

    else:
        print("Save cancelled!".center(30, "-"))


def employee_menu():
    while True:
        print("Employee Menu".center(30, " "))
        print("=" * 30)
        print("1. Show employees")
        print("2. Select employee")
        print("3. Add employee")
        print("0. Exit")

        selection = input_int_validation("Menu selection")

        if selection == 1:
            employees = ec.get_all_employees()
            print(
                "\n".join(f"{i}. {employee.employee_first_name} {employee.employee_last_name} works at our office in "
                          f"{employee.store.store_name}" for i, employee in enumerate(employees, 1))
            )

        elif selection == 2:
            select_employee_menu()

        elif selection == 3:
            add_employee_menu()

        elif selection == 0:
            break

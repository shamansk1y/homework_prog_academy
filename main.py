import module_student_stud
import module_group_stud

if __name__ == '__main__':
    group_1 = module_group_stud.Group("08-12-2022")
    group_1.stud_add(module_student_stud.Student('Doe', 'John', 101, "Python"))
    group_1.stud_add(module_student_stud.Student('Smith', 'Jane', 102, "Python"))
    group_1.stud_add(module_student_stud.Student('Petrenko', 'Petro', 103, "Python"))
    group_1.stud_add(module_student_stud.Student('Ivanov', 'Ivan', 104, "Python"))
    group_1.stud_add(module_student_stud.Student('Popova', 'Maria', 105, "Python"))
    group_1.stud_add(module_student_stud.Student('Armemovsky', 'Artem', 106, "Python"))
    group_1.stud_add(module_student_stud.Student('Karapetyn', 'Ashot', 107, "Python"))
    group_1.stud_add(module_student_stud.Student('Nevinoven', 'Rafik', 108, "Python"))
    group_1.stud_add(module_student_stud.Student('Makedonskiy', 'Aleksandr', 109, "Python"))
    group_1.stud_add(module_student_stud.Student('Nosurname', 'Oleksandr', 110, "Python"))
    print(group_1.search_stud('Nosurname'))
    group_1.stud_del('Nosurname')
    group_1.stud_add(module_student_stud.Student('Shevchenko', 'Sergiy', 777, "Python"))
    # group_1.stud_add(module_student_stud.Student('Test', 'Test', 555, "Test"))
    print(group_1)
univer = {
    'first_curse': {
        'bob': 19,
        'dan': 22,
        'lilu': 20
    },
    'second_curse': {
        'leo': 25,
        'barbara': 19,
        'ann': 20
    },
    'third_curse': {
        'kate': 21,
        'nick': 20,
        'stan': 18
    }
}
Up_Uni = {courses: {students.upper(): age for students, age in students.items()} for courses, students in univer.items()}
print(Up_Uni)

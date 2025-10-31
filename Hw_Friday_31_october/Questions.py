
def check_duplicates(lst):
    seen = set()  # مقادیری که قبلاً دیده شده‌اند
    duplicates = set()  # مقادیر تکراری

    for item in lst:
        if item in seen:
            duplicates.add(item)
        else:
            seen.add(item)

    if duplicates:
        print("مقادیر تکراری:", duplicates)
        return False  # لیست یکتا نیست
    else:
        print("همه مقادیر یکتا هستند")
        return True  # لیست یکتا است


# مثال استفاده
my_list = [1, 2, 3, 2, 4, 5, 1]
check_duplicates(my_list)
# خروجی:
# مقادیر تکراری: {1, 2}

########################################################
########################################################

def validate_password(password: str) -> bool:
    if len(password) < 8:
        return False

    has_upper = False
    has_lower = False

    for ch in password:
    if ch.islower():
    has_lower = True
    elif ch.isupper():
    has_upper = True
    elif ch.isspace():
    return False

return has_upper and has_lower


print(validate_password("dsdAAAfds"))

########################################################
########################################################




from re import match


def validate_password(password: str) -> bool:
return bool(match( r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)\S{8,}$', password))






########################################################
# Question : 13
########################################################

dic = {
    "Ebrahim": {
        "name": "Ebrahim",
        "age": 32,
        "city": "Tehtran",
        "email": "Ebrahim@mail.com",
    },
    "Ali": {
        "name": "Ali",
        "age": 30,
        "city": "Shiraz",
        "email": "Ali@mail.com",
    }
}

name = input("enter your name: ")
# name = "Ebrahim"
if name in dic:
    pprint(dic[name])
else:
    pprint("name is not exist.")
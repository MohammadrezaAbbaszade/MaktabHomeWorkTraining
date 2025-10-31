
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

    ########################################################
    # Question : 16
    ########################################################

 from pprint import pprint

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

    --------------------------------


    def calculate(user_number):

        if user_number < 0: return "Not valid"

        result = sum(number for number in range(user_number + 1) if number % 2 == 0)
        # for number in range(user_number + 1):
        #     if number % 2 == 0:
        #         result += number

        return result


    user_input = int(input("Please enter a number: "))
    print(calculate(user_input))

########################################################
# Question : 19
########################################################






########################################################
# Question : 23
########################################################

user_input = int(input("Please enter a number: "))
print(calculate(user_input))

n = int(input("Enter a number : "))
for i in range(n, 0, -1):
    for j in range(i, 0, -1):
        print(j , end = " ")
    print()

 ########################################################
    # Question : 25
########################################################

    with open('notes.txt', 'a') as f:
        user_input = input('enter:(for exit 0) ')

        while user_input != '0':
            f.write(user_input + '\n')
            user_input = input('enter:(for exit 0)')



########################################################
 # Question : 26
########################################################

try:
    with open("note.txt") as file:
        lines = file.readlines()

        num_lines = len(lines)
        num_chars = sum(len(line) for line in lines)
        num_words = sum(len(line.split(" ")) for line in lines)

        print("lines:", num_lines)
        print("words:", num_words)
        print("characters:", num_chars)

except FileNotFoundError:
    print("File not found")

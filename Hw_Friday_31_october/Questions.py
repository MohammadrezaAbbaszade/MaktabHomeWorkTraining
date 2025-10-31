
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

########################################################
 # Question
########################################################


def clean_file_spaces(input_file="notes.txt", output_file="notes_clean.txt"):
    try:
        with open(input_file, "r", encoding="utf-8") as fin:
            lines = fin.readlines()

        cleaned_lines = []
        for line in lines:

            words = line.strip().split()
            if words:  # skip empty lines
                cleaned_lines.append(" ".join(words))

        with open(output_file, "w", encoding="utf-8") as fout:
            fout.write("\n".join(cleaned_lines))

        print(f"Cleaned text written to '{output_file}'")

    except FileNotFoundError:
        print(f"File '{input_file}' not found!")


# Run
clean_file_spaces()

########################################################
 # Question
########################################################

import json

# from pprint import pprint

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

with open("notes1.txt", "w", encoding="utf-8") as file:
    json.dump(dic, file, indent=4)

with open("notes1.txt", "r") as file:
    loaded = json.load(file)
    # pprint(loaded)

for k, v in loaded.items():
    print(k, ":", v)


########################################################
 # Question 28
########################################################

with open("notes1.txt", "r+", encoding="utf-8") as file:
    json.dump(dic, file, indent=4)
    file.seek(0)
    loaded = json.load(file)
    pprint(loaded)

for k, v in loaded.items():
    print(k, ":", v)


########################################################
 # Question 30
########################################################


with open("users.json", "r") as file:
    loaded = json.load(file)

for k, v in loaded.items():
    age = v.get("age")
    if age > 20:
        print("name: ", k)
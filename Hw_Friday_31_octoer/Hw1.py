
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

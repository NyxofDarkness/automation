import re

# find and collect all email addresses and phone numbers.
def clean_it_up(phone_re):
    clean = phone_re.replace("(", "")
    clean = clean.replace(")", "-")
    clean = clean.replace(".", "-")
    if len(clean) == 8:
        clean = "206-" + clean

    return clean

if __name__ == "__main__":
    with open('../assets/potential-contacts.txt') as f:
        txt = f.read()

    phone_re = []

    phone_pattern = re.compile(r'\d{3}[-.]\d{2,3}[-.]\d{4}(x\d{3,5})')

    phone_re.extend(re.findall(phone_pattern, txt))

    clean = [clean_it_up(number) for number in phone_re]

    nums = list(set(clean))
    nums.sort()

    phone_return = "\n".join(nums)

    with open("phone_re.txt", "w+") as f:
        f.write(phone_return)
# Phone numbers may be in various formats.
# (xxx) yyy-zzzz, yyy-zzzz, xxx-yyy-zzzz, etc.
# phone numbers with missing area code should presume 206
# phone numbers should be stored in xxx-yyy-zzzz format.
# data_file = open('potential-contatcs.txt', '+w')

# for text in data_file:
#     seperate.append(text)

# for seperates in seperate:
#     if phone_re.search(seperate):
#         phone = phone_re.search(seperate)
#         group_phone_numbers = phone.group()
#         phone_contacts.append(group_phone_numbers)

# data_file.close()
# Once emails and phone numbers are found they should be stored in two separate documents.
# The information should be sorted in ascending order.
# Duplicate entries are not allowed.
import re

data = open("input/p4", "rb").read().decode()

all_fields = {
    "byr": "Birth Year",
    "iyr": "Issue Year",
    "eyr": "Expiration Year",
    "hgt": "Height",
    "hcl": "Hair Color",
    "ecl": "Eye Color",
    "pid": "Passport ID",
    "cid": "Country ID",
}

wanted_fields = {k:all_fields[k] for k in all_fields.keys() - {'cid'}}

documents = data.split("\n\n")

count = 0

height_re = re.compile(r"([0-9]+)(cm|in)")
def validate_height(height):
    match = height_re.match(height)
    if not match:
        return False
    height, unit = match.groups()
    height = int(height)
    if unit == "cm":
        return 150 <= height <= 193
    elif unit == "in":
        return 59 <= height <= 76
    else:
        return False

hair_re = re.compile(r"#[0-9a-f]{6}")

eye_colours = {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}

validations = {
    "byr": lambda year: 1920 <= int(year) <= 2002,
    "iyr": lambda year: 2010 <= int(year) <= 2020,
    "eyr": lambda year: 2020 <= int(year) <= 2030,
    "hgt": validate_height,
    "hcl": hair_re.match,
    "ecl": lambda colour: colour in eye_colours,
    "pid": lambda id: id.isnumeric() and len(id) == 9,
    "cid": lambda any: False,
}

count_2 = 0

for doc in documents:
    fields = (f.split(":") for f in doc.split())
    fields = {k:v for k,v in fields}
    missing = wanted_fields.keys() - fields.keys()

    if len(missing) == 0:
        count += 1
    else:
        continue

    correct = 0
    for k, v in fields.items():
        if validations[k](v):
            correct += 1

    if correct == 7:
        count_2 += 1

print(count)

print(count_2)

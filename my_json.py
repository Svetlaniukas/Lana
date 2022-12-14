import json

str_json = """
{
"response": {
     "staff_shift": [{
         "Monday"   : "10.am-4.pm",
         "Tuesday"  : "9.am-3.pm",
         "Wednesday": "10.am-5.pm",
         "Friday"   : "8am-4pm",
         "Saturday" : "10.am-5.pm",
         "Sunday"   : "8am- 4pm"
}]
}
}"""
print(type(str_json))

data = json.loads(str_json)

print(type(data))
print(data['response'])
for staff_shift in data['response']:
    print(staff_shift)



with open('my.json', 'w') as file:
    json.dump(data, file, indent=3)

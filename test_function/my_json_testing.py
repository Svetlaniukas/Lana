import json

str_json = """
{
  "weekday": {
    "Monday": "10.am-4.pm",
    "Tuesday": "9.am-3.pm",
    "Wednesday": "10.am-5.pm",
    "Thursday": "10am-4pm",
    "Friday": "8am-4pm"
},
  "weekend": {
    "Saturday": "10.am-5.pm",
    "Sunday": "8am- 4pm"
  }
}
"""
print(type(str_json))

data = json.loads(str_json)

print(type(data))

value_week = data['weekday']['Monday']
print(value_week)
value_week1 = data['weekend']['Sunday']
print(value_week1)

with open('../staff.json', 'r') as file:
    json.dump(data, file, indent=3)


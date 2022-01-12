import json, sys, csv, time
import mysql.connector, os
import urllib.request, json
import requests
time.sleep(20)

employees = mysql.connector.connect(
    host="localhost", user="root", password="secret", database="employee-db"
)

with urllib.request.urlopen("http://127.12.0.1/v1/users") as url:
    users = json.loads(url.read().decode())

with open('data.json', 'w') as outfile:
    json.dump(users, outfile)

cursor = employees.cursor()

query = (
    "SELECT e.name FROM departments d, salaries s, employees e "
    "WHERE d.empl_id=e.id AND e.id=s.empl_id AND d.department LIKE 'Production' AND s.salary > 100 AND d.to_date IS NULL AND s.to_date IS NULL"
)

cursor.execute(query)

lines = cursor.fetchall()
fp = open("output", "w")
text = csv.writer(fp)
text.writerows(lines)
fp.close()


f = open('data.json')
data = json.load(f)

json_length = len(data)
#print(json_length)

# payload = {'username': 'aventura'}
# r = requests.get('http://localhost/v1/accesslevels', params=payload)
with open('output') as topo_file:
    for line in topo_file:

        for i in range(json_length):

            payload = {'username': data[i]['username']}
            r = requests.get('http://localhost/v1/accesslevels', params=payload)

            if (line.strip() == data[i]['name']) and ('WRITE' in r.text):
                (data[i]['username'])


query2 = (
    "SELECT e.name, e.birth_date FROM departments d, salaries s, employees e "
    "WHERE d.empl_id=e.id AND e.id=s.empl_id AND d.department LIKE 'Production' AND s.salary > 100 AND d.to_date IS NULL AND s.to_date IS NULL"
)

cur = employees.cursor()
cur.execute(query2)

result = cur.fetchall()

header = ['name', 'birthday', 'username']

with open('output.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(result)

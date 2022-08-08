import requests
import jsonpath
import json



# Verifying the Post Functionality
url = "https://reqres.in/api/users"
file = open("payload.textfile", 'r')
# Reading data from file
json_input = file.read()

# converting to Json format
request_json = json.loads(json_input)

# Creating a New User by using Post Request

response = requests.post(url, request_json)
assert response.status_code == 201
# print (response.content)

# Retriving the ID of the new user
id= jsonpath.jsonpath(response.json(), 'id')
# print(id[0])

Final_ID = id[0]
print(Final_ID)

url = "https://reqres.in/api/users/" + Final_ID

# Verifying the GET API

url = "https://reqres.in/api/users/2"

response = requests.get(url)

# applying assertions
assert response.status_code == 200
# getting the ID
json_response = json.loads(response.text)
name = jsonpath.jsonpath(json_response, 'id')
print(id[0])

# Verifying the update API

url= "https://reqres.in/api/users/2"
file = open("updatedpayload.textfile", 'r')
# Reading data from file
json_input = file.read()

# converting to Json format
request_json = json.loads(json_input)

# Verifying the Update Request

response = requests.put(url, request_json)
assert response.status_code == 200
print(response.content)

# Verifying that Name is updated
json_response = json.loads(response.text)
name = jsonpath.jsonpath(json_response, 'name')
print(name[0])
assert name[0] == "Test_Jawwad Updated"

# Verifying that Job is updated
json_response = json.loads(response.text)
job = jsonpath.jsonpath(json_response, 'job')
print(job[0])
assert job[0] == "QA Automation Updated"

# Verifying the Delete Method

url = "https://reqres.in/api/users/2"

#  using Delete Request

response = requests.delete(url)
assert response.status_code == 204


#Verfying the API on different End Points

#Verifying the GET method

url = "https://reqres.in/api/users?page=2"

response = requests.get(url)

# applying assertions
assert response.status_code == 200
# getting the  Page ID

json_response = json.loads(response.text)
pages = jsonpath.jsonpath(json_response, 'total_pages')
print(pages[0])
assert pages[0] == 2





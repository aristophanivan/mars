from requests import get, post, delete

print(get('http://localhost:5000/api/jobs').json())

print(get('http://localhost:5000/api/jobs/1').json())

print(get('http://localhost:5000/api/jobs/999').json())

print(get('http://localhost:5000/api/jobs/q').json())
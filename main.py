import todoist
from todoist.api import TodoistAPI
import requests
import json

# Todoist API Initialization
api = TodoistAPI('d3cabe14c0027d1e2c228c7277ecad3a888bd783')
api.sync()


# Function to create a Calendly event
def create_calendly_event(event_type, task):
  headers = {
    'Accept':
    'application/json',
    'Content-Type':
    'application/json',
    'X-Token':
    'eyJraWQiOiIxY2UxZTEzNjE3ZGNmNzY2YjNjZWJjY2Y4ZGM1YmFmYThhNjVlNjg0MDIzZjdjMzJiZTgzNDliMjM4MDEzNWI0IiwidHlwIjoiUEFUIiwiYWxnIjoiRVMyNTYifQ.eyJpc3MiOiJodHRwczovL2F1dGguY2FsZW5kbHkuY29tIiwiaWF0IjoxNjc1NDMxMDc5LCJqdGkiOiJhZmVlZmRkNS0xZDQxLTQ3ZjUtOTM1My04YjNhMDIzYWRjODEiLCJ1c2VyX3V1aWQiOiI0MDY1Y2Y1Yy00ZWJlLTQ4NzgtYjE4Yi1iMGY4YTc3NzQxOTgifQ.fet8LBcWfoJ9z65iGJZIM-IEiijb0QnoJJX9fPc0XSAmaM2XZ_C8O3g7GHoi_L23RI8ywW6hXY6c2x0yKDwN2w',
  }
  payload = {
    'event_type':
    event_type,
    'start_time':
    task['due']['date'],
    'invitee': {
      'email': task['email'],
    },
    'questions': [
      {
        'question': 'Task Description',
        'answer': task['content'],
      },
    ],
  }
  response = requests.post('https://calendly.com/api/v1/events',
                           headers=headers,
                           data=json.dumps(payload))
  if response.status_code != 201:
    print(f'Error creating Calendly event: {response.text}')


# Get all tasks from Todoist
tasks = api.items.all()
for task in tasks:
  if task['due']:
    create_calendly_event("calendly.com/thenewmb23/academics", task)

print("Hello World")

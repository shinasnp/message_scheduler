# message_scheduler
schedule message on a given date time
## Installation
Install Rabbitmq
```
sudo apt-get install rabbitmq-server
```
Install Virtaul enviornment

```
sudo apt-get install python-virtualenv
```
### Steps:
```
virtualenv -p python3 env
source env/bin/activate
cd message_scheduler
pip3 install -r requirement.txt
```
### Start celery  Worker
```
celery -A scheduler worker --loglevel info
```
### Start Api
```
python manage.py runserver
```
## Test
```
python manage.py test
```
### To schedule a message at a given time(UTC time)
```
curl -X POST \
  http://127.0.0.1:8000/home/ \
  -H 'content-type: multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW' \
  -F 'datetime=16/01/2019 17:51' \
  -F 'message=Sample Message'
```

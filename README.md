# message_scheduler
Schedule message on a given date time
## Installation

Create a project directory

```
mkdir scheduler
cd scheduler
```

Install Virtual enviornment

```
sudo apt-get install python-virtualenv
```
Clone the project

```
git clone https://github.com/shinasnp/message_scheduler.git

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
export CLOUDAMQP_URL=amqp://username:password@hostname/vhost
celery -A scheduler worker --loglevel info --without-gossip --without-mingle --without-heartbeat
```
### Start Api
```
export CLOUDAMQP_URL=amqp://username:password@hostname/vhost
python manage.py runserver
```
## Test
```
python manage.py test
```
### To schedule a message at a given time
```
curl -X POST \
  http://127.0.0.1:8000/message/ \
  -H 'Content-Type: application/json' \
  -d '{"message":"Sample Message",
	"datetime":"18/01/2019 14:31"
}'
```

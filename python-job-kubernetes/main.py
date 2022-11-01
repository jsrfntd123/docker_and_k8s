import time
import sys
import json
import traceback
from urllib import request

def job_logic():
     time.sleep(10)

def authenticate():
     data = {"username": "jsrfntd@gmail.com", "password": "Sebitas123%"}
     encoded_data = json.dumps(data).encode()
     req = request.Request('https://dm-us.informaticacloud.com/ma/api/v2/user/login', data=encoded_data)
     req.add_header('Content-Type', 'application/json')
     req.add_header('Content', 'application/json')
     response = request.urlopen(req)
     text = response.read()
     json_response=json.loads(text.decode('utf-8'))
     return json_response['icSessionId']


def run_iics_task(icSessionId):
     data = {"@type":"job", "taskName":"SR_NormalizerAggregator_Task","taskType":"MTT"}
     encoded_data = json.dumps(data).encode()
     req = request.Request('https://usw5.dm-us.informaticacloud.com/saas/api/v2/job', data=encoded_data)
     req.add_header('Content-Type', 'application/json')
     req.add_header('Content', 'application/json')
     icSessionId = authenticate()
     req.add_header('icSessionId', icSessionId)
     response = request.urlopen(req)
     text = response.read()
     print(json.loads(text.decode('utf-8')))


def validate_sesion_id(icSessionId):
     data = {"@type": "validatedToken", "userName": "jsrfntd@gmail.com", "icToken": icSessionId}
     encoded_data = json.dumps(data).encode()
     req = request.Request('https://na1.dm-us.informaticacloud.com/saas/api/v2/user/validSessionId', data=encoded_data)
     req.add_header('Content-Type', 'application/json')
     req.add_header('Content', 'application/json')
     response = request.urlopen(req)
     text = response.read()
     json_response = json.loads(text.decode('utf-8'))
     print(json_response)

if __name__ == "__main__":
     try:
          icSessionId = authenticate()
          run_iics_task(icSessionId)
          validate_sesion_id(icSessionId)
          sys.exit(0)
     except Exception:
          traceback.print_exception(*sys.exc_info())
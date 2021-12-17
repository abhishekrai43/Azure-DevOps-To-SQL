from azure.devops.connection import Connection
from azure.devops.v5_1.work_item_tracking.models import Wiql
from msrest.authentication import BasicAuthentication
import requests
import base64
import json
pat = 'xpkksamq5gj6tottpkz32nqhpeq5i6zf252juair5x2mrtey3nbq'
authorization = str(base64.b64encode(bytes(':'+pat, 'ascii')), 'ascii')

headers = {
    'Accept': 'application/json',
    'Authorization': 'Basic '+authorization
}
organization = 'https://dev.azure.com/pursuitsoftwaredev'

#response = requests.get('https://dev.azure.com/pursuitsoftwaredev/ToscaCI_Scrum_Template/_apis/wit/workItems/172/updates?api-version=6.0', headers=headers).json()
#response = requests.get('https://dev.azure.com/pursuitsoftwaredev/_apis/projects/ebefbdb5-4cf1-41df-8e62-05afe9545483/teams?api-version=6.01', headers=headers).json()
#response = requests.get('https://dev.azure.com/pursuitsoftwaredev//{team}/_apis/work/backlogs?api-version=6.0-preview.1', headers=headers).json()
#response = requests.get('https://dev.azure.com/pursuitsoftwaredev/ToscaCI_Scrum_Template/_apis/wit/workitems/172/revisions?api-version=6.0',headers=headers).json()
children = requests.get('https://dev.azure.com/pursuitsoftwaredev/ToscaCI_Scrum_Template/_apis/wit/workitems/179/?$expand=relations&api-version=6.0', headers=headers).json()
#revision = requests.get('https://dev.azure.com/pursuitsoftwaredev/ebefbdb5-4cf1-41df-8e62-05afe9545483/_apis/wit/workItems/178', headers=headers).json()
#with open('rev_data.json', 'w') as f:
#    json.dump(response, f)
print(json.dumps(children, indent=4))
'''
revs = int(response['count'])
print(revs)
#print(revs)
if revs > 1:
    for i in range(revs):
        try:
            ans = response['value'][i]
            rev_name = ans['revisedBy']['name']
            rev_date = ans['revisedDate']
            #print(json.dumps(ans, indent=4))
            for k, v in response['value'][i]['fields'].items():
                #print(k)
                val = v['newValue']
                if val == 'Approved':
                    operation = 'Updated'
                if 'System.AssignedTo' in k:
                    operation = 'Assigned'
                if isinstance(val, dict):
                    print(v['newValue']['displayName'])
            print(val, operation)
        except:
            pass

#projects = requests.get(url="https://dev.azure.com/pursuitsoftwaredev/_apis/projects?api-version=5.1", headers=headers).json()
#print(json.dumps(response, indent=3))
#print("Title :", response['value'][0]['fields']['System.State']['newValue'])
#print("Revised By :", response['value'][0]['revisedBy']['displayName'])
#print("Revised By Contact :", response['value'][0]['revisedBy']['name'])
#print("Type :", response['value'][0]['fields']['System.WorkItemType']['newValue'])
#print("Severity :",response['value'][0]['fields']['Microsoft.VSTS.Common.Severity']['newValue'])
#print("Created Date :",response['value'][0]['fields']['System.CreatedDate']['newValue'])
#print("Comments :",response['value'][0]['fields']['System.CommentCount']['newValue'])
#print("Priority :",response['value'][0]['fields']['Microsoft.VSTS.Common.Priority']['newValue'])
'''''
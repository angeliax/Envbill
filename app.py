#!/usr/bin/env python
import requests
import json
API_KEY = '6VikmbdRNasaOyGtOzMUMy4bc4MaCYYBJPWQ4oAu'
#URL = 'https://api.propublica.org/congress/v1/bills/subjects/search.json'
URL = 'https://api.propublica.org/congress/v1/bills/subjects/'
URL2 = 'https://api.propublica.org/congress/v1/'
URL3 = 'https://api.propublica.org/congress/v1/members/'

house_num = 115
senate_num = 115

house_members = list()
senate_members = list()
congress_members = list()

bill_ids_found = set()
bill_subjects = [
    'environmental-protection',
    'environmental-assessment-monitoring-research',
]
#search_terms = [
#  'climate',
#  'green',
#  'greenhouse',
#  'environ',
#  'environment',
#]

for bill_subject in bill_subjects:
    r = requests.get(URL + bill_subject + '.json', headers={"X-API-Key": API_KEY})
    response_data = r.json()
    results = response_data['results']
    for result in results:
        if result['last_vote'] != 'null':
            bill_ids_found.add(result['bill_id'])
    #print(results[3])
    #print(type(results))
    #bill_ids_found.add(results['bill_id'])

print(bill_ids_found)
print(len(bill_ids_found))

# Get House Member IDs
# get the lists of member_ids
r = requests.get(URL2 + str(house_num) + '/house/members.json', headers={"X-API-Key": API_KEY})
response_data = r.json()
house_members = response_data['results'][0]['members']

# Get Senate Member IDs
# get the lists of member_ids
r = requests.get(URL2 + str(senate_num) + '/senate/members.json', headers={"X-API-Key": API_KEY})
response_data = r.json()
senate_members = response_data['results'][0]['members']

congress_members = house_members + senate_members


for congress_member in congress_members:
    member_id = congress_member['id']
    r = requests.get(URL3 + member_id + 'votes.json', headers={"X-API-Key": API_KEY})
    response_data = r.json()
    votes = response_data['results']
    #votes = response_data['results'][0]['votes']
    #for vote in votes:
     #   print(vote['bill'][0])


#congress_members = results['members']
#print(congress_members)
#print(house_members)
#for member_id in member_ids:
   # r = requests.get(URL2 + member_id + 'votes.json', headers={"X-API-Key": API_KEY})
import requests
from datetime import datetime
from airtable import airtable

# URLS
url = 'https://slack.com/api/conversations.history?token=xoxp-941344735348-941344736356-940042219891-cfa94baf3450c186f332978441ec21ab&channel=CU38UKYRL&users.profile.set=Kareem'

# Slack Variables
p = requests.post(url)
r = requests.get(url)
data = r.json()
name = data.get('messages')
slack_data = list(name[0].values())

# Airtable Variables
api_key = 'keyt4MS2VeMADeIkJ'
base_id = 'appN3x0rrRgpYrNee'
tabel_name = 'Table 3'
at = airtable.Airtable(base_id, tabel_name, api_key=api_key)

# Slack Data
slack_text = slack_data[2]
slack_client_ms_id = slack_data[0]
slack_type = slack_data[1]
slack_user = slack_data[3]
slack_timestamp = slack_data[4]

# Time Converter
timef = float(slack_timestamp)
timei = int(timef)
datei = datetime.fromtimestamp((timei))
slack_date = str(datei)

# User Assigenment
if slack_user == 'UTPA4MNAG':
    slack_user = 'Kareem'
if slack_user == 'UU184NDEZ':
    slack_user = 'Hero'

# Airtable Getting Data
airtable_data = at.get_all(sort='-Date')

# Starting Airtable's Sheet

if airtable_data == []:
    record = {'Text': slack_text, 'Date': slack_date, 'User': slack_user}
    at.insert(record)
else:
    pass
try:
    airtable_dict = dict(airtable_data[0])
    airtable_records = (airtable_dict.get('fields'))

    # Extracting Airtable Loop
    airtable_list_records = list(airtable_records.values())
    airtable_text = airtable_list_records[0]

    # IF Statement For Duplicates
    if slack_text != airtable_text:
        record = {'Text': slack_text, 'Date': slack_date, 'User': slack_user}
        at.insert(record)
        print('Record Created')
    else:
        print('Record Already Exists')
except:
    print('Record Created')

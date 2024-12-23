import os
import json
import datetime

from urllib.request import urlopen

url = 'https://hub.docker.com/v2/namespaces/jenkins/repositories/jenkins/tags?page=1&page_size=100'

with urlopen(url) as response:
    try:
        jsonbody = json.load(response)
    except json.JSONDecodeError:
        print('Failed to get JSON from Docker Hub')
        exit(1)

tags = jsonbody['results']

# Filter by last_updated that is with the past week
one_day_ago = datetime.datetime.now() - datetime.timedelta(days=1)
one_day_ago = one_day_ago.replace(tzinfo=datetime.timezone.utc).isoformat()

filtered = [tag for tag in tags if tag['last_updated'] > one_day_ago]
filtered = [
    tag for tag in filtered if len([
        True for image in tag['images'] if
        image['architecture'] == 'amd64' and image['os'] == 'linux'
    ]) > 0
]

rhel = []
alpine = []
debian = []

for tag in filtered:
    if 'rhel' in tag['name']:
        rhel.append(tag)
    elif 'alpine' in tag['name']:
        alpine.append(tag)
    else:
        debian.append(tag)

print('Filtered tags:')
print(f'RHEL: {len(rhel)}')
print(f'Alpine: {len(alpine)}')
print(f'Debian: {len(debian)}')

rhel = [f'rhel.Dockerfile,{tag["name"]}' for tag in rhel]
alpine = [f'alpine.Dockerfile,{tag["name"]}' for tag in alpine]
debian = [f'debian.Dockerfile,{tag["name"]}' for tag in debian]

all_tags = rhel + alpine + debian

all_tags_str = json.dumps({'tags': all_tags}, separators=(',', ':'))

with open(os.environ["GITHUB_OUTPUT"], "a") as f:
    f.write(f'matrix={all_tags_str}\n')

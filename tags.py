import os
import json
import datetime

from urllib.request import urlopen

url = 'https://hub.docker.com/v2/namespaces/jenkins/repositories/jenkins/tags?page=1&page_size=100'

with urlopen(url) as response:
    try:
        jsonbody = json.load(response)
    except json.JSONDecodeError:
        exit(1)

tags = jsonbody['results']

# Filter by last_updated that is with the past week
one_week_ago = datetime.datetime.now() - datetime.timedelta(days=7)
one_week_ago = one_week_ago.replace(tzinfo=datetime.timezone.utc).isoformat()

filtered = [tag for tag in tags if tag['last_updated'] > one_week_ago]
filtered = [
    tag for tag in filtered if len([
        True for image in tag['images'] if
        image['architecture'] == 'amd64' and image['os'] == 'linux'
    ]) > 0
]

print(f'{len(filtered)} tags found')
for tag in filtered:
    print(tag['name'])
    # print(tag['last_updated'])

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

print(f'RHEL: {len(rhel)}')
print(f'Alpine: {len(alpine)}')
print(f'Debian: {len(debian)}')

for tag in alpine:
    print(tag['name'])

rhel = [f'rhel,{tag["name"]}' for tag in rhel]
alpine = [f'alpine,{tag["name"]}' for tag in alpine]
debian = [f'debian,{tag["name"]}' for tag in debian]

all_tags = rhel + alpine + debian

all_tags_str = json.dumps({'tags': all_tags}, separators=(',', ':'))

print(all_tags_str)

# with open(os.environ["GITHUB_OUTPUT"], "a") as f:
#     f.write(f'matrix={all_tags_str}\n')

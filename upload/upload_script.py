import os
from github import Github

os.chdir('tmp/cache')

g = Github(os.environ["GITHUB_ACCESS_TOKEN"])
repo = g.get_repo('NikiLi3/WCA_Stats')

# TODO: create new directory depending on databased dump date
#folder = 'images'

for file_name in os.listdir():
    print(file_name)
    with open(file_name, 'rb') as image:
        f = image.read()
        image_data = bytearray(f)
    repo.create_file('docs/assets' + '/' + file_name, 'upload via API', bytes(image_data))

import os
from github import Github

os.chdir('images')
if os.path.exists("index.md"):
    os.remove("index.md")

g = Github(os.environ["GITHUB_ACCESS_TOKEN"])
repo = g.get_repo('NikiLi3/WCA_Stats')

# TODO: create new directory depending on databased dump date
#folder = 'images'

# for file_name in os.listdir():
#     print(file_name)
#     with open(file_name, 'rb') as image:
#         f = image.read()
#         image_data = bytearray(f)
#     repo.create_file('docs/assets' + '/' + file_name, 'upload via API', bytes(image_data))

with open('stats.txt') as f:
    lines = [line.rstrip() for line in f]

    with open('index.md', 'w') as webpage:
        for line in lines:
            title, image = line.split('---')
            webpage.writelines('## '+title+'\n\n')
            webpage.writelines('![](assets/'+image+')\n\n')

# Replace index.md file

with open("index.md") as f:
    contents = repo.get_contents("docs/index.md")
    lines = f.readlines()
    fileString = ''.join(lines)
    repo.update_file(contents.path, "updated static webpage", fileString, contents.sha)


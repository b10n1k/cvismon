import json
from pprint import pprint
import re
import termplotlib as tpl

image_data = {}
# need permissions

ihash = ''
img_id = []
with open("/var/lib/docker/image/btrfs/repositories.json", "r") as f3:
    data = f3.read()
    js = json.loads(data)
    for reponame in js['Repositories']:
        for image in js['Repositories'][reponame]:
            m = re.match(r"((\w+/)?)*\w+@sha256", image)
            if not m:
                ihash = js['Repositories'][reponame][image].split(':')[1]
                image_data[image] = ihash

# info
for img, ihash in image_data.items():
    with open("/var/lib/docker/image/btrfs/imagedb/content/sha256/%s" % ihash, "r") as f2:
        data = f2.read()
        js = json.loads(data)
        #first should have always size file
        img_id = js['rootfs']['diff_ids'][0].split(':')[1]
        image_data[img] = img_id
#size
dt = []
for img, idhash in image_data.items():
    with open("/var/lib/docker/image/btrfs/layerdb/sha256/%s/size" % idhash, "r") as f1:
        size = f1.read()
        dt.append(size)
        image_data[img] = size


fig = tpl.figure()
vals = [int(x) for x in image_data.values()]
fig.barh(vals, list(image_data.keys()), force_ascii=True)
fig.show()

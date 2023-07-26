import json
import os
basepath="/Volumes/upoates-raw/raw_data/metadata"
files=os.listdir(basepath)
for fname in files:
    f = open(os.path.join(basepath,fname))
    data = json.load(f)

    totsize=0
    totfiles=0
    for d in data["data"]:
        for exp in d:
            raw_files=d[exp]["data"]["raw_files"]
            totfiles+=len(raw_files)

            for rf in raw_files:
                totsize+=int(rf["size"])
    print('date\t\ttime\t\t\tNExp')
    print(data["date"],'\t',data["time"],'\t',len(data["data"]),'\t',totfiles,'\t',totsize/1000000000000.)
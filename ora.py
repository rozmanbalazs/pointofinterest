import json

class nevezet:
    def __init__(self, name, orszag, varos):
        self.name = name
        self.orszag = orszag
        self.varos = varos


##data = {
##    "név":"sheesh",
##    "sus":"xd"
##    }
##
##final = json.dumps(data, indent = 2, ensure_ascii=False)
##with open("info.json", "w") as file:
##    file.write(final)

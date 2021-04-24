from insert import insert_into_es as esInsert
with open("Android.log") as f:
    lines = [line.rstrip() for line in f]


log_mapp = {
        "V": "Verbose",
        "D": "Debug",
        "I": "Info",
        "W": "Warning",
        "E": "Error",
        "A": "Assert",
        "F" : "Others"
}
for line in lines:
        print(line)
        lineContent = (line.split())
        doc = {}
        month, day = lineContent[0].split('-')
        time = lineContent[1]

        doc["cateogory"]  = lineContent[5][:-1]
        doc['timestamp'] = ('2018-{}-{}T{}Z'.format(month, day, time))
        if lineContent[4] in log_mapp:
                doc['tag'] = log_mapp[lineContent[4]]
        else:
                doc['tag'] = 'Others'
        doc['PID1'] = lineContent[2]
        doc['PID2'] = lineContent[3]
        doc['log'] = " ".join(lineContent[6:])
        # print(doc)
        esInsert(doc, "android")
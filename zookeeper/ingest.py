from insert import insert_into_es as esInsert
with open("Zookeeper.log") as f:
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
        print(lineContent)
        doc = {}
        year, month, day = lineContent[0].split('-')
        time = lineContent[1].split(',')[0]

        doc["cateogory"]  = lineContent[3]
        doc["msg"]  = lineContent[4]
        doc["type"]  = lineContent[6]
        
        doc['timestamp'] = ('{}-{}-{}T{}Z'.format(year,month, day, time))
#         if lineContent[4] in log_mapp:
#                 doc['tag'] = log_mapp[lineContent[4]]
#         else:
#                 doc['tag'] = 'Others'
#         doc['PID1'] = lineContent[2]
#         doc['PID2'] = lineContent[3]
#         doc['log'] = " ".join(lineContent[6:])
        # print(doc)
        esInsert(doc, "zookeper")
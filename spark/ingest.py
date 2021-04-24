from insert import insert_into_es as esInsert
with open("Spark_2k.log") as f:
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
        day, month, year = lineContent[0].split('/')
        time = lineContent[1]

        doc["cateogory"]  = lineContent[2]
        tmp = lineContent[3].replace(':','')
        if 'Remoting' in tmp:
            doc["service"], doc["action"] = 'Remoting',''
        else:
            doc["service"], doc["action"] = tmp.split('.')
        
        doc['timestamp'] = ('20{}-{}-{}T{}Z'.format(year, month, day, time))
#         if lineContent[4] in log_mapp:
#                 doc['tag'] = log_mapp[lineContent[4]]
#         else:
#                 doc['tag'] = 'Others'
#         doc['PID1'] = lineContent[2]
#         doc['PID2'] = lineContent[3]
#         doc['log'] = " ".join(lineContent[6:])
        print(doc)
        esInsert(doc, "spark")
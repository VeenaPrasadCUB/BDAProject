import os


from insert import insert_into_es as esInsert

def process_log(fileName):
    with open(fileName) as f:
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
            try :
                lineContent = (line.split())
                print(lineContent)
                doc = {}
                year, month, day = lineContent[0].split('-')
                time = lineContent[1].split(',')[0]

                doc["cateogory"]  = lineContent[2]
                doc["thread"]  = lineContent[3]
                doc['process'] = lineContent[4]
                doc['timestamp'] = ('{}-{}-{}T{}Z'.format(year, month, day, time))
                if lineContent[4] in log_mapp:
                        doc['tag'] = log_mapp[lineContent[4]]
                else:
                        doc['tag'] = 'Others'
                doc['PID1'] = lineContent[2]
                doc['PID2'] = lineContent[3]
                doc['log'] = " ".join(lineContent[6:])
                # print(doc)
                esInsert(doc, "hadoop")
            except Exception as ex:
                print(ex)
for root,dirs,files in os.walk('logs/'):
    for file in files:
       if file.endswith(".log"):
           print(root, dirs,file)
           process_log(os.path.join(root, file))

import csv

file = open('./hrithika_dodia_project_1.txt','r')
content = file.read().split('\n')
file.close()

with open('hrithika_24332866_final_pred.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    # writer.writeheader()
    writer.writerow(["dodiah"])
    for line in content:
        l = line.split(',')
        if len(l) < 2:
            continue
        writer.writerow([l[0], l[1].strip()])


####################################################
# 26. : Reading datasheet
####################################################
import csv

with open('practice_data_set.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            print(
                f'\t{row[0]} Title:{row[1]} Year:{row[2]} IMDB rating:{row[3]} Metascore:{row[4]} Total Votes:{row[5]} ')
            # Literally same as this below
            #print("\t",row[0],"Title:",row[1],"Year:",row[2],"IMDB rating:",row[3],"Metascore:",row[4],"Total Votes:",row[5])
            line_count += 1
    print(f'Processed {line_count} lines.')

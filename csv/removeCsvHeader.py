import os,csv,shutil
dir_path = 'headerRemoved'




os.makedirs(dir_path, exist_ok=True)  #we make a directory for future csv files
csv_files = [f for f in os.listdir(".") if f.endswith(".csv")]
cwd = os.getcwd()
for csv_file in csv_files :
    os.chdir(cwd)
    data = []
    csv_open = open(csv_file,"r")
    csv_reader = csv.reader(csv_open)
    for csv_row in csv_reader:
        data.append(csv_row)
      #csv writer obj
        
        
    csv_open.close()                #we make a list off csv file rows
    os.chdir(os.path.join(cwd,dir_path))

    with open(csv_file,"w",newline="") as new_csv:
        csv_writer = csv.writer(new_csv)
        for index,newCsv_row in enumerate(data):
            if index == 0: #setting first row as an exeption
                continue
            csv_writer.writerow(newCsv_row)
            
            
    
        
    
    
    
    
    
    
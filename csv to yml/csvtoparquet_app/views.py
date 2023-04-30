from django.shortcuts import render
import os
import csv
import yaml

# this code is read the yaml ,text and log file 

def index(request):
    if request.method=='POST':
        file=request.FILES.get('uploadedfile')
        file_path=os.path.join(os.getcwd(),file.name)
        with open(file_path, 'wb') as f:
            for chunk in file.chunks():
                f.write(chunk)

        with open(file_path, 'r') as csv_file:
            csv_data = csv.DictReader(csv_file)
            data_list = list(csv_data)

        with open(f"{os.getcwd()}/yml/Homestead.yaml", 'w') as yaml_file:
             yaml.dump(data_list, yaml_file, default_flow_style=False)

    return render(request,'index.html')





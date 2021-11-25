#importing necessary modules
import numpy as np 
import csv

#defining the function to get source
def getDataSource(data_path):
    marks_percentage = []
    days_present = []
    with open(data_path) as f:
        csv_reader = csv.DictReader(f)
        for row in csv_reader:
            marks_percentage.append(float(row["Marks In Percentage"]))
            days_present.append(float(row["Days Present"]))
        return {"x":marks_percentage, "y":days_present}

#defining the fuction to find correlation
def findCorrelation(datasource):
    correlation = np.corrcoef(datasource["x"], datasource["y"])
    print("Correlation between Percentage of marks and number of days present is \n--->",correlation[0,1])

data_path = 'C:\Users\PRMOD\Desktop\Coding Notes\Student Marks vs Days Present.csv'
data_source = getDataSource(data_path)
findCorrelation(data_source)
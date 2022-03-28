import csv

# 读
# with open('a.csv', 'r',encoding='UTF-8-sig') as csv_file:
#     csv_reader = csv.reader(csv_file)
#     for line in csv_reader:
#         print(line)


# 写
# with open('a.csv', 'r', encoding='UTF-8-sig') as csv_file:
#     csv_reader = csv.reader(csv_file)
#     with open('new_a.csv', 'w') as new_file:
#         csv_writer = csv.writer(new_file, delimiter=',')
#         for line in csv_reader:
#             csv_writer.writerow(line)

# 读取CSV文件作为字典
# with open('a.csv', 'r', encoding='UTF-8-sig') as csv_file:
#     csv_reader = csv.DictReader(csv_file)
#     for line in csv_reader:
#         print(line)

# 作为字典写入CSV文件
mydict = [{'Passenger': '1', 'Id': '0', 'Survived': '3'},  # key-value pairs as dictionary obj
          {'Passenger': '2', 'Id': '1', 'Survived': '1'},
          {'Passenger': '3', 'Id': '1', 'Survived': '3'}]

fields = ['Passenger', 'Id', 'Survived']  # field name
filename = 'new_Titanic.csv'  # name of csv file

with open('new_Titanic.csv', 'w') as new_csv_file:  # open a new file 'new_titanic,csv' under write mode
    writer = csv.DictWriter(new_csv_file, fieldnames=fields)
    writer.writeheader()  # writing the headers(field names)

    writer.writerows(mydict)  # writing data rows

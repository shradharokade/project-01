import csv
def write_into_csv(info_list):
    with open('student_info.csv','a',newline='')as csv_file:
        writer=csv.writer(csv_file)
        if csv_file.tell()== 0:
            writer.writerow(["name","age","contact_Number","Email_ID"])
        
        writer.writerow(info_list)
        
condition= True

while(condition):
     student_info=input("Enter student information in the following format(name age contact_number E-mail_ID): ")
     print("Entered information: "+ student_info)
     
     #split
     student_info_list=student_info.split(' ')
     print("Entered split up information is:"+ str(student_info_list))
     
     write_into_csv(student_info_list)

     condition_check=input("Enter (yes/no) if you want to enter information for another student: ")
     if condition_check == "yes":
       condition=True
     elif condition_check == "no":
       condition=False

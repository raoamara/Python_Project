import json
import sys
import csv


primary_key = "sql_steps"


with open(
    "C:\\Users\\rsram\\OneDrive\\Documents\\BigDataProgramming\\Python_Project\\data\\config.json", "r",
) as f:
    config_file = f.read()

config_data = json.loads(config_file)

# try:
#     print(config_data.keys())
# except Exception as e:
#     print(f"Syntax error")

print(config_data.keys())

print("------------------------------------------------------")

#l = [1, 2, 3, 4]

if primary_key in config_data.keys():
    print(f"{primary_key} is available in read_config.py")
else:
    print(f"{primary_key} is not available in read_config.py. Exiting the process")
    sys.exit(0)

result = True if isinstance(config_data.get(primary_key), list) else False

# checking if validate_process_key exists in each and every element
if result:
    validate_process_keys = ["sql_num", "action", "next_sql"] 


    for key_to_validate in validate_process_keys:
        for step in config_data.get(primary_key):
            """
            {
            "sql_num": "2",
            "action": "write|csv",
            "location": "python_project\\data\\output\\",
            "next_sql": "3"
            }
            """
            if key_to_validate in step.keys():
               print(f"{key_to_validate} is available in the step")                
            else:
                print(
                    f"Error with {key_to_validate} in the step. Pls correct config file"
                )
                sys.exit(0)

print("----------------------------------------------------------")

# validate sql_mun = 1
Object_key = "sql_num"
Key_value = 1

for step in config_data.get(primary_key):
   if int(step[Object_key]) == Key_value:
      print(f"{Object_key} - {Key_value} is available in the step")
   break                  
else:
      print(f"{Key_value} is not available for {Object_key}")

print("------------------------------------------------------------")
                  
    
# validate action
Object_key = "action"

for step in config_data.get(primary_key):
     for Object_key in step.keys():
        if step[Object_key] in ("read|publish", "write|parquet", "read|parquet"):        
           print(f"{step[Object_key]} is the correct value")
           break
     else:
         print(f"{step[Object_key]} for {Key_value} is not correct, please correct")

print("-----------------------------------------------------")

# update "sql_num" & "next_sql" keys values in the Json
Object_key = "sql_num"
Key_values = [1, 2, 3, 4]

for step in config_data.get(primary_key):

   for Object_key in step.keys():

      if   int(step[Object_key]) == Key_values[0]:
           step.update({Object_key: 1})
           step.update({"next_sql": 2})
           print(step)          
      
      if int(step[Object_key]) == Key_values[1]:
           step.update({Object_key: 2})
           step.update({"next_sql": 3})
           step.update({"action": "write|csv"})
           step.update({"location": "C:\\Users\\rsram\\OneDrive\\Documents\\BigDataProgramming\\Python_Project\\tgt\\config.csv" })
           print(step)
      
      if int(step[Object_key]) == Key_values[2]:
           step.update({Object_key: 3})
           step.update({"next_sql": 4})
           print(step)

      if int(step[Object_key]) not in (Key_values[::]):
        print(f"[{Key_values[::]}] are not available for {Object_key} in {step}")
      break 

print("-------------------------------------------------------------------")






                                      
           
    



 
import datetime

counts = {
    "Deposit":0,
    "Future":0,
    "BasisSwap":0,
    "Swap":0
}

after_date= datetime.datetime(2020,7,1)

docs = open( "C:\\Users\\Hariom\\Downloads\\python_exercise_input.txt",'r')

each_lines = [line.strip() for line in docs if line.strip()]

docs.close()

for line in  each_lines:
    instrument,date_string,value_string = line.split(';')
    date = datetime.datetime.strptime(date_string, '%Y-%m-%d %H:%M:%S')

    

    if date > after_date:
        if instrument in counts :
             counts[instrument] += 1

print("Number of Quotes after 01/07/2020:\n")
for instrument, count in counts.items():
    print(f"{instrument}:{count}")
        
# this is python code
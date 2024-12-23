file_name = input("Enter file name: ") + ".txt"

with open(file_name, 'w') as file:
    print(f"Enter the data to store into {file_name}. Type 'stop' to end: ")
    
    while True:
        data = input("Enter data: ")
        if data.lower() == 'stop':
            break
        file.write(data + "\n")
import json

# Reads a CSV file and returns a list with the items
def read_csv():
    file_to_open = input("Please specify the CSV file name you want to open: ")
    # Stores data from CSV file
    data = []
    # If true, means the file was successfully read
    valid_read = False
    while (valid_read is not True):
        # Checks if file is marked as .csv
        if(file_to_open.endswith(".csv")):
            # Reads each line in file
            try:
                with open(file_to_open) as f:
                    for x in f:
                        x = x.replace("\n", "")
                        # Splits line by comma and adds list to data list
                        data.append(x.split(","))
                    if(len(data) > 0):
                        valid_read = True
                    else:
                        print("The file you selected has no content. Please select another fiie.")
            except:
                print("Could not read the file. Please try again.")
        else:
            print("The file you inputted is not a valid CSV file. Please select another file.")
        if(valid_read is not True):
            file_to_open = input()
    print(f"Found {len(data)} records.")
    return data

# Creates headers for the JSON file
def define_headers(values: list):

    # Value that determines whether the file has headers
    has_headers: str = ""

    # Stores headers
    headers = []

    valid_inputs = ["y", "yes", "n", "no"]

    # If one value was found, set value to no
    if(len(values) == 1):
        has_headers = "no"

    # Asks user if file has headers
    else:
        has_headers = input("Does the file have headers (headers are on the first row of the CSV file)? (Y)es or (No): ")
        # Asks for input again if value is not "(y)es" or "(n)o"
        while(not any(item == has_headers.lower() for item in valid_inputs)):
            has_headers = input("Invalid input. Valid inputs are (Y)es or (No): ")

    # Removes first item from list to headers if user selects yes
    if (has_headers.lower() == "yes" or has_headers.lower() == "y"):
        headers = values[0]
        values.pop(0)

    # Gets row with longest number of items
    longest_row = max(values)

    # For each element, ask user to enter an header if blank in file
    for i in range(len(headers)):
        if(not headers[i].strip()):
            headers[i] = input(f"Element at position {i + 1} is blank. Please provide a name: ")

    # While the header size is shorter than the longest row, ask the user to add headers until the
    # header length matches the longest row 
    while(len(longest_row) > len(headers)):
        new_header = input(f"Please enter a name for the property at element {len(headers) + 1}: ")
        headers.append(new_header)
        
    return headers

# Creates dictionaries with values
def create_dicts(headers: list, values: list):
    output = []

    for i in values:
        # Creates new dictionary
        new_dict = {}
        for j in range(len(headers)):
            # Skips adding values is header size is larger than current row
            if j >= len(i): continue
            # Adds value to dictionary if value is not blank
            if(i[j].strip()):
                if(len(i[j].split(";")) > 1):
                    new_dict[headers[j]] = i[j].split(";")
                else: new_dict[headers[j]] = i[j]
        if (len(new_dict) > 0):
            output.append(new_dict)
    print(f"Created list of {len(output)} items.")
    return output

# Writes JSON file to device
def save_json(values: list):
    output_name = input("Enter the name you would like to save this file to: ")
    if(not output_name.strip()):
        output_name = "output.json"
    if(not output_name.endswith(".json")):
        output_name += ".json"

    try:
        with open(output_name, "w") as f:
            f.write(json.dumps(values, indent=4))
        print(f"Successfully written to {output_name}.")
    except:
        print(f"An error has occured writing to {output_name}.")

# Main function
def main():
    # Stores raw CSV values
    csv_values = []
    # Stores headers and property names
    headers = []
    # Stores dictionaries to be converted to JSON and exported
    json_dicts = []

    csv_values = read_csv()
    
    headers = define_headers(csv_values)
    json_dicts = create_dicts(headers=headers, values=csv_values)
    save_json(json_dicts)

main()
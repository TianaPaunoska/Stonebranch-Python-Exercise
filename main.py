# Tiana Paunoska
# This is the main script, where the functions of preselect_customers.py are implemented 
# Additionally, there are functions for extracting the entire data and writing it in new files for the preselected customers

import csv
from preselect_customers import preselectCustomers

# Function for extracting entire data for the preselected customers
def extractData(customer_codes, *files):  # *files for dynamic number of files for extracting
    data = {file: [] for file in files}

    # The following block of code saves the rows from customer.csv for the preselected customers
    customer_codes_set = set(customer_codes)
    customer_info = {}
    with open("customer.csv", mode = 'r', newline = '\n', encoding = 'utf-8') as customer_file:
        csv_reader = csv.reader(customer_file)
        header = next(csv_reader)
        for row in csv_reader:
            code = row[0].strip('“”')
            if code in customer_codes_set:
                customer_info[code] = row

    # The following block of code saves the invoice codes in a set
    invoice_codes_set = set()
    with open("invoice.csv", mode = 'r', newline = '\n', encoding = 'utf-8') as invoice_file:
        csv_reader = csv.reader(invoice_file)
        header = next(csv_reader)
        for row in csv_reader:
            code = row[0].strip('“”')
            if code in customer_info:
                invoice_codes_set.add(row[1].strip('“”'))

    for file in files:
        with open(file, mode = 'r', newline = '\n', encoding = 'utf-8') as current_file:
            csv_reader = csv.reader(current_file)
            header = next(csv_reader)
            if file == "invoice_item.csv": # this check is needed to create a link between all the files
                rows = [row for row in csv_reader if row[0].strip('“”') in invoice_codes_set]
            else:
                rows = [row for row in csv_reader if row[0].strip('“”') in customer_codes_set]
            data[file] = (header, rows)

    return data

# Function for writing the extracted data into the new, smaller files
def writeData(output_file, headers, data):
    with open(output_file, mode = 'w', newline = '\n', encoding = 'utf-8') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(headers)
        csv_writer.writerows(data)

# The main part where all the necessary functions are called and executed
if __name__ == "__main__":
    extractCustomerInfo = preselectCustomers()

    num_customers = int(input("Enter the number of preselected customers.\n"))
    selected_customers = extractCustomerInfo.getPreselectedCustomers(num_customers)
    if selected_customers:
        print("Customers are preselected.\n")
    extractCustomerInfo.preselectedCustomers.update(selected_customers)
    extractCustomerInfo.createFile()
    print(f"The file '{extractCustomerInfo.output_file}' is created successfully.\n")

    extracted_data = extractData(extractCustomerInfo.preselectedCustomers, "customer.csv", "invoice.csv", "invoice_item.csv")
    for file, (header, data) in extracted_data.items():
        output_file_new = f"{file.lower().replace('.csv', '_new.csv')}"
        writeData(output_file_new, header, data)

    print("The data for the preselected customers is saved successfully.\n")


# Tiana Paunoska
# This script has the necessary functions regarding the creation of the customer_sample.csv file

import csv, random

class preselectCustomers:
    def __init__(self, preselectedCustomers = None, input_file = "customer.csv", output_file = "customer_sample.csv"):
        self.input_file = input_file
        self.output_file = output_file
        self.preselectedCustomers = set(preselectedCustomers) if preselectedCustomers else set()

    # This function is used for a random preselection of customers based on a number of customers chosen by the user
    def getPreselectedCustomers(self, num_customers):
        with open(self.input_file, mode = 'r', newline = '\n', encoding = 'utf-8') as csv_file:
            csv_reader = csv.reader(csv_file)
            header = next(csv_reader)
            customers = [row[0].strip('“”').strip('"') for row in csv_reader]
            if num_customers > len(customers):
                print("The inserted number of customers exceeds the real number of customers.\n")
                return None
            selected_customers = sorted(random.sample(customers, num_customers))

            return selected_customers

     # This function is for creating and writing info (the customer code) in the customer_sample.csv file   
    def createFile(self):
        with open(self.output_file, mode = 'w', newline = '\n', encoding = 'utf-8') as csv_file:
            csv_writer = csv.writer(csv_file, quoting = csv.QUOTE_ALL)
            csv_writer.writerow(["CUSTOMER_CODE"])
            for customer_code in sorted(self.preselectedCustomers):
                csv_writer.writerow([customer_code])





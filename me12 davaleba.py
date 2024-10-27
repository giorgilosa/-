#######################
#task 1
######################

import csv


def filter_survivors(input_file, output_file, filter_column=None, filter_value=None):


    try:

        with open(input_file, mode='r') as infile:
            reader = csv.reader(infile)
            header = next(reader)
            survivors = []


            for row in reader:
                if row[1] == '1':

                    if filter_column is not None and filter_value is not None:
                        if row[filter_column] == filter_value:
                            survivors.append(row)
                    else:
                        survivors.append(row)


        with open(output_file, mode='w', newline='') as outfile:
            writer = csv.writer(outfile)
            writer.writerow(header)
            writer.writerows(survivors)

        print(f"Filtered survivor data has been saved to {output_file}")

    except FileNotFoundError:
        print(f"The file {input_file} was not found. Please check the file location.")
    except Exception as e:
        print(f"An error occurred: {e}")




filter_survivors('titanic.csv', 'survived.csv')


filter_survivors('titanic.csv', 'survived_pclass_1.csv', filter_column=2, filter_value='1')

#######################
#task 2
#######################

import csv


def sort_and_filter_organizations(input_csv, output_csv, location=None, descending=True):

    try:

        with open(input_csv, mode='r') as infile:
            reader = csv.reader(infile)
            header = next(reader)
            data = list(reader)


        if location:
            data = [row for row in data if row[2] == location]


        data.sort(key=lambda row: int(row[3]), reverse=descending)


        with open(output_csv, mode='w', newline='') as outfile:
            writer = csv.writer(outfile)
            writer.writerow(header)
            writer.writerows(data)

        print(f"Sorted and filtered data has been saved to {output_csv}")

    except FileNotFoundError:
        print(f"The file {input_csv} was not found. Please check the file path.")
    except Exception as e:
        print(f"An error occurred: {e}")



sort_and_filter_organizations('organizations-100.csv', 'sorted_organizations.csv')


sort_and_filter_organizations('organizations-100.csv', 'usa_sorted_organizations.csv', location='USA')


sort_and_filter_organizations('organizations-100.csv', 'ascending_sorted_organizations.csv', descending=False)

#######################
#task 3
#######################

import csv


def extract_ssl_companies(input_csv_path, output_csv_path, industry_filter=None):

    try:

        with open(input_csv_path, mode='r') as infile:
            reader = csv.reader(infile)
            header = next(reader)
            rows = list(reader)


        ssl_companies = [row for row in rows if row[3].startswith("https://")]


        if industry_filter:
            ssl_companies = [row for row in ssl_companies if row[4] == industry_filter]


        extracted_data = [
            [row[0], row[1], row[3], row[4], row[5]]
            for row in ssl_companies
        ]


        with open(output_csv_path, mode='w', newline='') as outfile:
            writer = csv.writer(outfile)
            writer.writerow(["ID", "Company Name", "Website", "Industry", "Number of Employees"])  # Write header
            writer.writerows(extracted_data)  # Write filtered rows

        print(f"SSL-secured companies have been saved to {output_csv_path}")

    except FileNotFoundError:
        print(f"Error: The file '{input_csv_path}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


extract_ssl_companies('organizations-100.csv', 'ssl_companies.csv')


extract_ssl_companies('organizations-100.csv', 'ssl_companies_tech.csv', industry_filter='Tech')

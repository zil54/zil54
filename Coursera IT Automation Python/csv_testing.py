import csv
import itertools
import os

'''
The most common format for importing and exporting data for spreadsheets is a .csv format. 
A Comma Separated Values (.csv) file is a plain text file that uses—you guessed it—commas to separate each piece of data. 
You may already be familiar with .csv files if you have saved a spreadsheet in the .csv format. 
Here is a simple example of a .csv file displaying employee information:

Name, Department, Salary

Aisha Khan, Engineering, 80000

Jules Lee, Marketing, 67000

Queenie Corbit, Human Resources, 90000

Notice that each row represents an employee’s information, and the values are separated by commas. 

In this reading, you will examine different commands to use when working with .csv files in Python and be provided 
with additional links for more information. Module contents

The .csv module is a built-in Python functionality used to read and work with .csv files. 
Let’s look at how the .csv module defines some of these functions:

csv.reader This function returns a reader object that iterates over lines in the .csv file.
csv.writer This function returns a writer object that’s responsible for converting the user’s data
into delimited strings on the given file-like object.

class csv.DictReader This function creates an object that functions as a regular reader but maps the information 
in each row to a dictionary whose keys are given by the optional fieldname parameters.
Dialects and formatting parameters

Dialects are rules that define how a .csv file is structured, and parameters are formed to control
the behavior of the .csv reader and writer and live within dialects. The following  features are supported by dialects:
Dialect.delimiter This attribute is a one-character string used to separate fields and defaults to a comma.
Dialect.quotechar  This attribute is a one-character string used to quote fields containing special characters and defaults to ‘ ‘’ ‘.
Dialect.strict  This attribute’s default is False, but when True, exception csv.Error will be raised if an error is detected.
Reader objects

A reader object contains the following public methods and attributes:
csvreader._next_() This method returns the next row of the reader’s iterable object as a list or a dictionary, parsed properly to the current dialect. 
Typically, you would call this next(reader).

csvreader.dialect This attribute is a read-only description of the dialect in use by the parser.

Writer objects
Writer objects provide you the capability to write data to a .csv file. 
Let’s look at a couple of public methods and attributes for writer objects:

csvwriter.writerows(rows) This method writes all elements in rows to the writer’s 
file object and formats following the current dialect.
csvwriter.dialect This attribute is a read-only description of the dialect being used by the writer.

Key takeaways

If you haven’t worked with .csv files yet, it’s only a matter of time. 
Become familiar with the .csv module’s reader and writer objects to work more efficiently with .csv files. 
The modules, features, and attributes in this reading are only some of the commands that can be used while working with .csv files. 


'''

#print(os.environ.get('PATH'))
#print(os.getcwd())
#os.chdir("..")
#print(os.getcwd())

#print (os.path.abspath(os.getcwd()))

class CSVUtility:

    def __init__(self, sourceDir, sourceFile):
        self.sourceDir = sourceDir
        self.sourceFile = sourceFile

    def csv_print_each_row(self, bool_useDictReader, bool_skipHeader_non_Dict=None):
        file_to_read = os.path.join(self.sourceDir,self.sourceFile)
        with open(file_to_read, 'r') as file:
            if not bool_useDictReader:
                reader = csv.reader(file)
                if bool_skipHeader_non_Dict:
                    next(reader, None)  # skip header
                for row in reader:
                    print(" ".join(row))
            else:
                reader = csv.DictReader(file)  # header is automatically used as keys
                for row in reader:
                    print(row)


    def csv_print_specific_keys_values(self):
        file_to_read  = os.path.join(self.sourceDir,self.sourceFile)
        list_years = []
        list_winners = []
        list_runners_up = []
        with open(file_to_read, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
            # Each row is a dictionary
                for keys, values in row.items():
                    if keys.strip() == 'Winner':
                        list_winners.append(values)
                    elif keys.strip() == 'Runner-Up':
                        list_runners_up.append(values)
                    elif keys.strip() == 'Year':
                        list_years.append(values)
                   # print("key " + keys + "\n")
                   # print("value " + values + "\n" + "-------")
        for each_value1, each_value2, each_value3 in zip(list_years, list_winners, list_runners_up):
            print ("Year: " + each_value1 + " Winner: " + each_value2 + " Runner-Up: " + each_value3)
    def csv_demo_writer(self, list_of_items_to_write):
        file_to_write = os.path.join(self.sourceDir, self.sourceFile)
        with open(file_to_write, "w") as file:
            for item in list_of_items_to_write:
                file.write(item)

    def csv_demo_writer2(self, list_of_dicts_to_write):
        file_to_write = os.path.join(self.sourceDir, self.sourceFile)
        with open(file_to_write, "w", newline='') as file:
            # Assuming all dictionaries have the same keys, use the keys from the first dictionary as the header
            fieldnames = list_of_dicts_to_write[0].keys()
            writer = csv.DictWriter(file, fieldnames=fieldnames)

            writer.writeheader()  # Write the header row
            writer.writerows(list_of_dicts_to_write)  # Write all th



# Read the file contents and format the information about each row






def main():
    CSV_Util = CSVUtility(os.getcwd(),"World_Cup_Winners.csv")
    CSV_Util.csv_print_each_row(False, True)
    CSV_Util.csv_print_specific_keys_values()

#write
    #list_of_items_to_write = ["name,color,type\n","carnation,pink,annual\n","daffodil,yellow,perennial\n","iris,blue,perennial\n","poinsettia,red,perennial\n","sunflower,yellow,annual\n"]
   # CSV_Util1 = CSVUtility(os.getcwd(), "Flowers.csv")
    #CSV_Util1.csv_demo_writer(list_of_items_to_write)

if __name__ == "__main__":
    main()







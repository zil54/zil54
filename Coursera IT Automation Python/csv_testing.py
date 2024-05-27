import csv
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



def csv_demo(file_name):
    test_file = os.path.join(os.getcwd(), file_name)
    with open(test_file, 'r') as file:
        reader = csv.reader(file)
        next(reader, None) #skip header
        for row in reader:
            print(" ".join(row))
    file.close()

def csv_demo_reader_dict(file_name):
    test_file = os.path.join(os.getcwd(), file_name)
    with open(test_file, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            # Each row is a dictionary
            print(row)
    file.close()

def csv_demo_reader_dict2(file_name):
    test_file = os.path.join(os.getcwd(), file_name)
    with open(test_file, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            # Each row is a dictionary
            print(("{} won vs. {}").format(row["Winner"], row["Runner-Up"]))
    file.close()


def create_file(filename):
  with open(filename, "w") as file:
    file.write("name,color,type\n")
    file.write("carnation,pink,annual\n")
    file.write("daffodil,yellow,perennial\n")
    file.write("iris,blue,perennial\n")
    file.write("poinsettia,red,perennial\n")
    file.write("sunflower,yellow,annual\n")

# Read the file contents and format the information about each row
def contents_of_file(filename):
  return_string = ""

  # Call the function to create the file
  create_file(filename)

  # Open the file
  with open(filename, "r") as file:
    # Read the rows of the file into a dictionary
    csv_reader = csv.DictReader(file)
    # Process each row
    for row in csv_reader:
      name, color, plant_type = row["name"], row["color"], row["type"]
      # Format the return string for data rows only
      return_string += "a {} {} is {}\n".format(name, color, plant_type)
  return return_string

#Call the function
print(contents_of_file("flowers.csv"))

# Read the file contents and format the information about each row
def contents_of_file(filename):
  return_string = ""

  # Call the function to create the file
  create_file(filename)

  # Open the file
  with open(filename, "r") as file:
    csv_reader = csv.DictReader(file)
    # Process each row
    for row in csv_reader:
      name, color, plant_type = row["name"], row["color"], row["type"]
      # Format the return string for data rows only

      return_string += "a {} {} is {}\n".format(name, color, plant_type)
  return return_string

#Call the function
print(contents_of_file("flowers.csv"))
def cvs_demo_writer():
    rows = [{'name': 'John', 'age': 30, 'city': 'New York'},
            {'name': 'Anne', 'age': 25, 'city': 'Paris'},]
    # Add more dictionaries as needed]

# Specify the fieldnames (keys of the dictionaries)
    fieldnames = ['name', 'age', 'city']

# Open the CSV file for writing
    with open('people.csv', 'w', newline='') as csvfile:
    # Create a DictWriter object
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    # Write the header (optional)
        writer.writeheader()

    # Write the rows
        writer.writerows(rows)




# Create a file with data in it
def create_file1(filename):
  with open(filename, "w") as file:
    file.write("name,color,type\n")
    file.write("carnation,pink,annual\n")
    file.write("daffodil,yellow,perennial\n")
    file.write("iris,blue,perennial\n")
    file.write("poinsettia,red,perennial\n")
    file.write("sunflower,yellow,annual\n")

# Read the file contents and format the information about each row
def contents_of_file1(filename):
  return_string = ""

  # Call the function to create the file
  create_file(filename)

  # Open the file
  with open(filename, "r") as file:
    # Read the rows of the file into a dictionary
    csv_reader = csv.DictReader(file)
    # Process each item of the dictionary
    for row in csv_reader:
      return_string += "a {} {} is {}\n".format(row["color"], row["name"], row["type"])
  return return_string

#Call the function
print(contents_of_file("flowers.csv"))





def main():
    csv_demo("World_Cup_Winners.csv")
   # csv_demo_reader_dict("World_Cup_Winners.csv")
   # csv_demo_reader_dict2("World_Cup_Winners.csv")
   # print(create_python_script("program.py"))

if __name__ == "__main__":
    main()







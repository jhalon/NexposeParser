import sys
import os
import time
import csv

def banner():
    print "  _   _     __  __                       ____                          "
    print " | \ | | ___\ \/ /_ __   ___  ___  ___  |  _ \ __ _ _ __ ___  ___ _ __ "
    print " |  \| |/ _ \\  / | '_ \ / _ \/ __|/ _ \ | |_) / _` | '__/ __|/ _ \ '__|"
    print " | |\  |  __//  \| |_) | (_) \__ \  __/ |  __/ (_| | |  \__ \  __/ |   "
    print " |_| \_|\___/_/\_\ .__/ \___/|___/\___| |_|   \__,_|_|  |___/\___|_|   "
    print "                 |_|                                                   "
    print "                          Created By: Jack Halon                       "
    print
    print

def usage():
    print "NeXpose Parser - A Quick Python Script to Parse NeXpose Scans"
    print "-------------------------------------------------------------"
    print
    print "Usage Information:"
    print "Step 1: Enter the .cvs file name of the NeXpose Scan"
    print "Step 2: Select one of the following parse options:"
    print "         - 1: Print out all Asset Names that don't have an Asset Owner"
    print "         - 2: Print out all Asset IP's that don't have an Asset Name"
    print "         - 3: Print out all Asset IP's that don't have an Asset Name or Asset Owner"
    print "Step 3: Enter a name for the output file"
    print "Step 4: Wait for the parse to complete"
    print "Step 5: Done!\n"

def main():
    global file_input
    global file_output
    global file_exist
    parse_option = ""
    save_option = ""
    row_count = 0
    seen_line = []

    # Take user input for options
    file_input = raw_input("Please enter the filename for the NeXpose Scan you want to parse: ")
    parse_option = raw_input("Please select a parse option from above: ")
    #save_output = raw_input("Please select a save option from above: ")
    file_output = raw_input("Please enter a name for the output file: ")

    print

    # Check if the Input File Exists
    while not os.path.exists(file_input):
        print "Reading in file, please wait",
        for i in range(6):
            print ".",
            time.sleep(1)
        print "[ERROR] NeXpose Scan File was not found!"
        time.sleep(1)
        file_input = raw_input("\nPlease enter the filename for the NeXpose Scan you want to parse: ")
        print
    else:
        print "Reading in file, please wait",
        for i in range(6):
            print ".",
            time.sleep(1)
        print "OK!"
        time.sleep(1)

    # Enumerate Headers for Specific Column Index
    reader = csv.reader(open(file_input, "rU"), delimiter=',')
    hrow = reader.next()
    anField = hrow.index("Asset Names")
    aoField = hrow.index("Asset Owner")
    aipField = hrow.index("Asset IP Address")

    # Count total amount of rows in CSV File
    with open(file_input) as count_inpt:
        row_reader = csv.reader(count_inpt, delimiter=',')
        row_data = list(row_reader)
        rc = len(row_data)
    # Close Row Count File Reader
    count_inpt.close()

    # Open file to read and parse data
    with open(file_input) as f_input:
        reader = csv.reader(f_input, delimiter=',')
        row_count = len(reader.next())

        print

        print "Parsing a total of %s rows in %s" % (rc, file_input)
        time.sleep(2)
        print

        # Check parse option and print accordingly
        while parse_option is not "1" or not "2" or not "3":
            print "[ERROR] Incorrect Parse Option Set. Must be set to 1, 2 or 3!\n"
            time.sleep(1)
            parse_option = raw_input("Please select a parse option from above: ")
            print
        else:
            if parse_option == "1":
                print "Appending Asset Names without an Asset Owner to %s.csv\n" % (file_output)
                time.sleep(2)
            elif parse_option == "2":
                print "Appending Asset IP's without an Asset Name to %s.csv\n" % (file_output)
                time.sleep(2)
            elif parse_option == "3":
                print "Appending Asset IP's without an Asset Name or Owner to %s.csv\n" % (file_output)
                time.sleep(2)

        # Open up write to append data to CSV File
        file_exist = os.path.exists(file_output + ".csv")
        while file_exist:
            out_exist()
        else:
            writer = csv.writer(open(file_output + ".csv" , "wb"))
            time.sleep(2)

        # Read each line of the file and check Parse Option
        for line in reader:
            if parse_option == "1":
                # Check to see if Owner Name is Empty
                if line[aoField] in (None, ""):
                    # Check to see if Asset Name is in duplicates
                    if line[anField] not in seen_line:
                        # Check to see if Asset Name is Emtpy
                        if line[anField] not in (None, ""):
                            # Write data to CSV File
                            writer.writerow(line)
                            # Add lines to seen_line to prevent duplicates
                            seen_line.append(line[anField])
            elif parse_option == "2":
                # Check to see if Asset Name is Empty
                if line[anField] in (None, ""):# and line[aoField] in (None, ""):
                    # Check to see if Asset IP is in duplicates
                    if line[aipField] not in seen_line:
                        # Check to see if Asset IP is null
                        if line[aipField] not in (None, ""):
                            # Write data to CSV file
                            writer.writerow(line)
                            # Add lines to seen_line to prevent duplicates
                            seen_line.append(line[aipField])
            elif parse_option == "3":
                # Check to see if Asset Name is Empty
                if line[anField] in (None, "") or line[aoField] in (None, ""):
                    # Check to see if Asset IP is in duplicates
                    if line[aipField] not in seen_line:
                        # Check to see if Asset IP is null
                        if line[aipField] not in (None, ""):
                            # Write data to CSV file
                            writer.writerow(line)
                            # Add lines to seen_line to prevent duplicates
                            seen_line.append(line[aipField])

        print 'Output file "%s.csv" was saved successfully!\n' % (file_output)
        time.sleep(1)

        print "[Completed]"
        time.sleep(3)

def out_exist():
    global file_output
    global file_exist
    ow_input = raw_input('[ERROR] The file "%s" already exists! Do you want to overwrite it? (y/n): ' % (file_output))
    print
    if ow_input == "y":
        file_exist = False
    elif ow_input == "n":
        file_output = raw_input("Please enter a name for the output file: ")
        print
        file_exist = os.path.exists(file_output + ".csv")
    else:
        print "Sorry, that was invalid input!\n"
        time.sleep(1)

if __name__ == "__main__":
    banner()
    usage()
    main()

    close_input = ""

    while close_input == "":
        close_input = raw_input("\nWould you like to run this program again? (y/n): ")
        print

        if close_input == "y":
            main()
            close_input = ""
        elif close_input == "n":
            print "[OK] - Thanks for using Nexpose Parse!\n"
            time.sleep(1)
            print "Shutting Down..."
            time.sleep(3)

"""A data tracker application for use with csv files from the Bandwidth+ application for OS X """

import csv

def open_and_read_files():
    try:
        filename = raw_input("Insert file name")
        with open(filename, 'rb') as csvfile:
            filelines = csv.reader(csvfile)
            file_text = []
            for row in filelines:
                new_row = [entry.lower() for entry in row]
                file_text.append(new_row)
        return file_text
    except IOError:
        print "Please enter a valid file name"
        return open_and_read_files()



def make_list_of_network_dates_and_data(file_text):
    network = raw_input("Which network connection would you like to see data use for?")
    list_of_usage = []

    for line in file_text:
        if network in line[1]:
            line_info = [line[0], line[4]]
            list_of_usage.append(line_info)

    if list_of_usage == []:
        print "Please enter a valid network name"
        return make_list_of_network_dates_and_data(file_text)

    return list_of_usage


def print_list_of_usage(list_of_usage):
    sorted_by_date_list = sorted(list_of_usage, reverse=True)
    for line in sorted_by_date_list:
        print line[0], ": ", line[1]


def calculate_total_usage(list_of_usage):
    sorted_by_date_list = sorted(list_of_usage, reverse=True)
    total_usage = 0

    first_date = sorted_by_date_list[-1][0]
    last_date = sorted_by_date_list[0][0]

    for line in sorted_by_date_list:
        total_usage += float(line[1])

    print "Your total usage from %s to %s: %f GBs" % (first_date, last_date, total_usage / 1000)



def main():
    file_text = open_and_read_files()
    list_of_usage = make_list_of_network_dates_and_data(file_text)

    print "\n", "Here is the data usage in MB per day", "\n"
    print_list_of_usage(list_of_usage)
    print
    calculate_total_usage(list_of_usage)


if __name__ == "__main__":
    main()

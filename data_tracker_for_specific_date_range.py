"A data tracker application for use with csv files from the Bandwidth+ application for OS X """

import csv
import bisect


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


def make_list_of_specific_network_data_and_dates_only(file_text):
    network = raw_input("Which network connection would you like to see data use for?")
    unordered_list_of_usage = []

    for line in file_text:
        if network in line[1]:
            line_info = [line[0], line[4]]
            unordered_list_of_usage.append(line_info)

    if unordered_list_of_usage == []:
        print "Please enter a valid network name"
        return make_list_of_specific_network_data_and_dates_only(file_text)

    return unordered_list_of_usage


def get_list_of_usage(unordered_list_of_usage):
    specific_dates = raw_input("Would you like to enter a specific date range? Type 'yes' or 'no'")

    if specific_dates == "no" or specific_dates == "No":
        return all_dates_get_list_of_usage(unordered_list_of_usage)

    elif specific_dates == "yes" or specific_dates == "Yes":
        return specific_dates_get_list_of_usage(unordered_list_of_usage)

    else:
        print "Please enter 'yes' or 'no'"
        return get_list_of_usage(unordered_list_of_usage)


def all_dates_get_list_of_usage(unordered_list_of_usage):
    return sorted(unordered_list_of_usage, reverse=True)


def specific_dates_get_list_of_usage(unordered_list_of_usage):
    sorted_by_date_list = sorted(unordered_list_of_usage)

    start_date = raw_input("Enter start date in yyyy-mm-dd format")
    end_date = raw_input("Enter end date in yyyy-mm-dd format")

    indexes = [line[0] for line in sorted_by_date_list]
    most_recent_date_index = bisect.bisect_right(indexes, end_date)
    furthest_date_index = bisect.bisect_left(indexes, start_date)

    return sorted(sorted_by_date_list[furthest_date_index:most_recent_date_index], reverse=True)


def print_usage_by_day_and_total(sorted_data_list):
    print "\n", "Here is your data use in MB per day: "
    for line in sorted_data_list:
        print line[0], ": ", line[1]

    total_usage = calculate_total_usage(sorted_data_list)
    print "\n", "Your total usage for these days: %f GBs" % (total_usage / 1000)


def calculate_total_usage(sorted_by_date_list):
    total_usage = 0
    for line in sorted_by_date_list:
        total_usage += float(line[1])
    return total_usage


def main():
    file_text = open_and_read_files()
    unordered_list_of_usage = make_list_of_specific_network_data_and_dates_only(file_text)
    list_of_usage_by_date = get_list_of_usage(unordered_list_of_usage)
    print_usage_by_day_and_total(list_of_usage_by_date)


if __name__ == "__main__":
    main()

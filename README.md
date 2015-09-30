# Data-Tracker-application-for-Bandwidth-+
data tracker application for use with csv files from the Bandwidth+ application for OS X 

## data_tracker_csv_reader.py
For use with csv files from OS X Bandwidth+ application.

Bandwidth+ gives a csv file with all of the connections and their bandwith used for *all networks* to which a device has connected. 


data_tracker_csv_reader.py allows to reader to specify a *particular network* and receive a list of the connections to that network, each connection's data use, and the total data usage for that network.


## data_tracker_for_specific_date_range.py

data_tracker_for_specific_date_range.py is an updated version of data_tracker_csv_reader.py that allows a user to enter a specific range of dates for bandwidth use to be calculated.


###usage
Run the script and follow the prompts.

The Bandwidth+ csv file to be read must be in the **same directory** as the script.

`python data_tracker_for_specific_date_range.py`

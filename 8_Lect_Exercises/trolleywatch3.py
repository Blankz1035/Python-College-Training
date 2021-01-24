#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Program to visualise Trolley Watch data 
Example of: matplotlib
(For simplicity, ignoring errors, i.e. no Exception Handling)
"""
import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

def get_data(filename):
    """
    Function to retrieve trolleywatch data from the file

    Parameters
    ----------
    filename : string
        The pathname of the file containing the data.

    Returns
    -------
    dates_data : dict
        A dictionary containing as key-value pairs the dates and the number of patients on that date
    hospitals_data : dict
        A dictionary containing as key-value pairs the hospital and the number of patients in that hospital.
    regions_data : dict
        A dictionary containing as key-value pairs the region and the number of patients in that region.
    trolley_vs_ward_numbers: list
        A list of tuples containing the trolley numbers and ward numbers.
    """
    # create empty dictionaries for the data
    dates_data = {}
    hospitals_data = {}
    regions_data = {}
    
    # create an empty list for the trolley and ward numbers
    trolley_vs_ward_numbers = []
    
    # date format string
    format_str = "%d/%m/%Y"

    # read the data from the file
    with open(filename) as datafile:
        # read the first line containing the headings and discard it
        datafile.readline()
        
        # for each other line in the file
        for line in datafile:
            # split the line into the components
            date_string, hospital, region, trolley, ward, patients = line.strip().split(",")
            
            # convert the date string to a datetime object
            date = datetime.datetime.strptime(date_string, format_str)  

            # convert the patient value to an int, save having to code this repeatedly
            patients = int(patients)                          
            
            # if this is the first occurrence of this date
            if date not in dates_data:
                # insert into dictionary 
                dates_data[date] = patients
            else:
                dates_data[date] += patients

            # if this is the first occurrence of this hospital
            if hospital not in hospitals_data:
                # insert into dictionary 
                hospitals_data[hospital] = patients
            else:
                hospitals_data[hospital] += patients            

            # if this is the first occurrence of this region
            if region not in regions_data:
                # insert into dictionary 
                regions_data[region] = patients
            else:
                regions_data[region] += patients  
                
            # add the trolley and ward numbers to a list of tuples
            trolley_vs_ward_numbers.append((int(trolley),int(ward)))

    # return the data structures for use with with matplotlib
    return dates_data, hospitals_data, regions_data, trolley_vs_ward_numbers
        
    
if __name__ == "__main__":
    
    # get the data from the file
    dates_data, hospitals_data, regions_data, trolley_vs_ward_numbers = get_data("trolleywatch2.csv")
    
    fig, ax = plt.subplots()
    
    ax.xaxis.set_major_locator(mdates.DayLocator()) 
    date_format = mdates.DateFormatter("%A")
    ax.xaxis.set_major_formatter(date_format)
    

    ax.set_xlabel("Day")
    ax.set_ylabel("Patients")
    
    
    ax.plot_date(dates_data.keys(), dates_data.values())
    plt.show()
    
    
   def create_charts(values_to_plot, title, hospitals_data, dates_data):
    fig, ax = plt.subplots(2, 2, figsize=(15, 15))
    ax[0][0].set_title(title)
    ax[0][0].pie(values_to_plot.values(), labels=values_to_plot.keys(), autopct="%.0f%%")
    ax[0][1].set_title(title)
    y_pos = list(range(len(hospitals_data)))
    ax[0][1].set_yticks(y_pos)
    ax[0][1].set_yticklabels(hospitals_data.keys())
    ax[0][1].barh(y_pos, hospitals_data.values())
    ax[1][0].xaxis.set_major_locator(mdates.DayLocator()) 
    date_format = mdates.DateFormatter("%A")
    ax[1][0].xaxis.set_major_formatter(date_format)
    ax[1][0].set_xlabel("Day")
    ax[1][0].set_ylabel("Patients")  
    ax[1][0].plot_date(dates_data.keys(), dates_data.values())
    return plt
    
 
    
    
    
    
    
    
    
    
    
    
 
    
 
    
    
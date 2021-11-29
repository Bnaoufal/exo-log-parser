import datetime
import logging


# Function o Read the log file line by line
def engine_file_reader(filename):
    my_data = []
    format = '%b/%d/%Y %H:%M:%S'
    text_start = 'starting nxengine'
    text_run = 'nxengine is running'
    # create and configure logger
    logging.basicConfig(format='%(message)s', level=logging.INFO)
    log_file = open(filename, "r+")
    for row in log_file:
        if text_start in row:
            dateTimeStr = row.split()[0] + '/' + row.split()[1]+'/2021' + ' ' + row.split()[2]
            dateTimeObj = datetime.datetime.strptime(dateTimeStr, format)
            logging.info('Starting nxengine: %s', dateTimeObj.strftime(format))
            my_data.append(dateTimeObj)
        if text_run in row:
            dateTimeStr = row.split()[0] + "/" + row.split()[1]+"/2021"+" " + row.split()[2]
            dateTimeObj = datetime.datetime.strptime(dateTimeStr, format)
            logging.info('Running nxengine: %s', dateTimeObj.strftime(format))
            my_data.append(dateTimeObj)
    pass
    return my_data


# Function to iterate every two elements of data list
def grouped(iterable, n):
    return zip(*[iter(iterable)]*n)


# Function to calculate cycle duration
def count_diff(my_data):
    i = 0
    for x, y in grouped(my_data, 2):
        i += 1
        logging.info('Start Cycle: %s Duration: %s', str(i),  str(y - x))
        pass


# Main
if __name__ == "__main__":
    count_diff(engine_file_reader('engine.log'))

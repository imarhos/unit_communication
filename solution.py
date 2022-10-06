import sys

#This function opens the input file, reads it, saves the content in a variale called lines and returns it.
def read_input_file(inputfile):
    try:
        file1 = open(inputfile, 'r')
        lines = file1.readlines()
    except:
        print("Input file not found or incorrect format")
        exit()
    #We close the file
    file1.close()
    return lines

#This function puts the data from line in an array of arrays
def put_input_file_data_in_array_of_arrays(lines):
    data = []
    for line in lines:
        line_data = [unit.strip() for unit in line.split(",")]
        data.append(line_data)
    return data



#This function separates units by satellites
def separate_units_by_satellites(sat,elements,lines):
    start_elements_state = elements
    #For every line
    for line in lines:
    	#If a satellite is in line
        if sat in line:
            for l in line:
                if l not in elements:
                	#Save distinct units that belongs at the unit if not saves yet
                    elements.append(l)
                else:
                    pass
    if(len(start_elements_state)==len(elements)):
        return elements
    else:
        for el in start_elements_state.__xor__(elements):
            separate_units_by_satellites(el,elements,lines)

def list_all_units(data):
    # initialize a null list
    unique_list = []
    for data in data:
    # traverse for all elements
        for x in data:
            # check if exists in unique_list or not
            if x not in unique_list:
                unique_list.append(x)
    #return unique_list with no duplicated units
    return unique_list

def list_all_satellites(units):
	#filter only satellites
    sats = []
    for unit in units:
        if (unit[0:3]=="SAT"):
            sats.append(unit)
    if(len(sats)==0):
        print("No satellites found, program will stop")
        exit()
    return sats
#Get maximum numbers ( the maximum number is the number of units of a satellite (the name of the satellites not included))
#Example if SAT1 is : ['Alpha', 'Bravo', 'SAT1', 'Charlie', 'Beta', 'Ales'] the maximum number is lengthof(['Alpha', 'Bravo', 'SAT1', 'Charlie', 'Beta', 'Ales'] ) -1 = 5
def get_maximum_number(sats,inputfile_data):
    maximum_number= 0
    for sat in sats:
        units_by_sat = separate_units_by_satellites(sat,[],inputfile_data)
        if(len(units_by_sat) > maximum_number):
            maximum_number=len(units_by_sat) -1
    return maximum_number

if __name__ == '__main__':

    inputfile = sys.argv[1]

    lines = read_input_file(inputfile)

    print("\nPut all data in array of arrays: \n")
    inputfile_data = put_input_file_data_in_array_of_arrays(lines)
    print(inputfile_data)
    

    print("\nList of units: \n")
    units = list_all_units(inputfile_data)
    print(units)



    print("\nDetecting satellites: \n")
    satellites = list_all_satellites(units)
    print(satellites)

    print("\nSeparating units by satellites: \n")
    for sat in satellites:
        units_by_sat = separate_units_by_satellites(sat,[],inputfile_data)
        print(units_by_sat)


    maximum_number= get_maximum_number(satellites,inputfile_data)
    print("\nThe maximum number of units that can communicate a message with each other is : "+str(maximum_number))


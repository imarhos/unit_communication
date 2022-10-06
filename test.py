import unittest

from solution import put_input_file_data_in_array_of_arrays,list_all_units,read_input_file,list_all_satellites,get_maximum_number


class Test_list_all_units(unittest.TestCase):
    def test_list_all_units(self):
        """
        Test that we can get the list of all units from input file
        """
        inputfile = "input.txt"
        lines = read_input_file(inputfile)
        array_data = put_input_file_data_in_array_of_arrays(lines)
        units = list_all_units(array_data)
        print("Testing listing all units from input file")
        self.assertEqual(units,  ['Alpha', 'Bravo', 'SAT1', 'Charlie', 'Delta', 'Zulu', 'SAT2'])

    def test_list_all_satellites(self):
        """
        Test that we can get the list of all satellites from input file
        """
        inputfile = "input.txt"
        lines = read_input_file(inputfile)
        array_data = put_input_file_data_in_array_of_arrays(lines)
        units = list_all_units(array_data)
        sats = list_all_satellites(units)
        print("Testing listing all satellites from input file")
        self.assertEqual(sats,  ['SAT1', 'SAT2'])


    def test_maximum_number_calculation(self):
        """
        Test that we can calculate the  maximum number of units that can communicate a message with each other 
        """
        inputfile = "input.txt"
        lines = read_input_file(inputfile)
        array_data = put_input_file_data_in_array_of_arrays(lines)
        units = list_all_units(array_data)
        sats = list_all_satellites(units)
        maximum_number = get_maximum_number(sats,array_data)

        print("Testing if the  maximum number of units that can communicate a message with each other is well calculated")
        self.assertEqual(maximum_number, 3)
if __name__ == '__main__':
    unittest.main()

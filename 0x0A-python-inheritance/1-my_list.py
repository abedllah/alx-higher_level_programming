#!/usr/bin/python3
"""class mylist"""

class MyList(list):
    """Class MyList inherits from list"""

    def print_sorted(self):
        """Prints the list, in ascending order"""

        new_list = self[:]
        new_list.sort()
        print("{}".format(new_list))

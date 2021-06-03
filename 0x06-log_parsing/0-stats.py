#!/usr/bin/python3
""" log steeam parsing by line  """

import sys

dict_codes = {'200': 0, '301': 0, '400': 0, '401': 0,
              '403': 0, '404': 0, '405': 0, '500': 0}
total_size = 0
num_lines = 0

try:
    for line in sys.stdin:
        line_list = line.split(" ")

        if len(line_list) > 2:
            size = line_list[-1]
            status_code = line_list[-2]

            if status_code in dict_codes.keys():
                dict_codes[status_code] += 1

            num_lines += 1
            total_size += int(size)

        if num_lines == 10:
            print("File size: {}".format(total_size))

            for key, value in sorted(dict_codes.items()):
                if value > 0:
                    print("{}: {}".format(key, value))
            num_lines = 0

except Exception:
    pass

finally:
    print("File size: {}".format(total_size))

    for key, value in sorted(dict_codes.items()):
        if value > 0:
            print("{}: {}".format(key, value))

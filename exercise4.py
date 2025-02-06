# Import regular expression module
import re

data = '''# Measurements started
Sep 9, 9:05, T=22deg
SEP 9, 10:15, T=25deg
# Taking a coffee break
Sep 9, 11:15, T=-10deg
# Weekend
Sept 12, 09:00AM, T=32deg
Oct12 13:00, T=32degr''' 

# Create regular expression
pattern = re.compile("^([A-Za-z]+) ?([0-9]+).+[0-9]+:[0-9]+.+T=([-0-9]+)deg[r]?")

for data_line in data.split('\n'):
    match = pattern.match(data_line)
    if match:
        if int(match.group(3)) > 0:
            print(match.group(3))


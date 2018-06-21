import re

# take input.txt file as input
input_ip = open('input.txt','r')
all_ips = input_ip.read()
print(all_ips)
input_ip.close()
# make list of ip from file using regex
ip_finder = re.compile(''' 
		((\d{1,3}\.\d{1,3}\.\d{1,3})(.*)).*
''',)  
ips = ip_finder.search(all_ips)
print(ips.group())
# ping each request
# on each request success ( create file if not exist give name as ping_success ) write ip into file 
# on request failure ( create file if not exist give name as ping_failure ) write ip into file



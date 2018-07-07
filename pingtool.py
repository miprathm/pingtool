import re
import os

# take input.txt file as input
input_ip = open('input.txt','r')
all_ips = input_ip.read()
#print(all_ips)
input_ip.close()
#creating output files
if not os.path.exists('output'):
	os.mkdir('output')
else:
	os.unlink('output')
	
ping_success = open(os.path.join('output','success.txt'),'w')	
ping_fail = open(os.path.join('output','fail.txt'),'w')	

# make list of ip from file using regex
ip_finder = re.compile(''' 
		(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s*
''',re.X)  
ips = ip_finder.findall(all_ips)
noOfIps = len(ips)
print("No of ips processing : "+str(noOfIps))
# ping each request
for index in range(len(ips)):
	hostname = ips[index] #example
	print("Processing : "+str(index+1)+" / "+str(noOfIps)+"\n")
	print("###################### Pinging : "+hostname+"######################")
	response = os.system("ping " + hostname)
	#and then check the response...
	#print(" in python ",response)
	"""
	# following script gives false positive to "Destination host unreachable"
	if response == 0:
		ping_success.write(hostname+'\n')
		print(hostname+" is up ")
	else:
		ping_fail.write(hostname+'\n')
		print(hostname+" is down")
	"""
	print("############################################")

# on each request success ( create file if not exist give name as ping_success ) write ip into file 
# on request failure ( create file if not exist give name as ping_failure ) write ip into file
ping_success.close()
ping_fail.close()


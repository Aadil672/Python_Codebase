# Python program to validate an Email 

# import re module 

# re module provides support 
# for regular expressions 
import re 

# Make a regular expression 
# for validating an Email 
#regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
#var emailPattern = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$/;
#regex = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$/; #Invalid syntax
regex = '^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$'
	
# Define a function for 
# for validating an Email 
def check(email): 

	# pass the regualar expression 
	# and the string in search() method 
	if(re.search(regex,email)): 
		print("Valid Email") 
		
	else: 
		print("Invalid Email") 
	

# Driver Code 
if __name__ == '__main__' : 
	
	# Enter the email 
	email = "ankitrai326@gmail.com"
	
	# calling run function 
	check(email) #Valid

	email = "my.ownsite@ourearth.org"
	check(email)  #Valid

	email = "ankitrai326.com"
	check(email) #Invalid
    

	email = "aadil@frontm.com"
	check(email) #Valid
    
	email = "aadil@frontm.in"
	check(email) #Valid
    
	email = "aadil+007@frontm.com"
	check(email) #Invalid
    
	email = "aadil.frontm.com"
	check(email) #Invalid
    
	email = "aadil.bit007@frontm.com"
	check(email) #Valid
#regex = '^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$'
	email = "aadil007._@frontm01.COM24"
	check(email) #Invalid
	email = "aadil007._@frontm01.COM"
	check(email) #Valid

#Program for Extracting the Mail Ids from Text
#ExtractMaildsEx1.py
import re
gd="Rossum maild is rossum_py@psf.com, Travis maild is travis_1@numpy.org , Ritche maild is ritche_c@belllabs.co.in and Jhon maild is jhon_hun@matplotlib.net.in  and Anthony maild is anothony_ora@oracle.com and Kvr maild is kvr1.python@gmail.com  and Jim mail id is Jim_12@NumLib.org.in"
sp=r"\S+@\S+"
mailslist=re.findall(sp,gd)
print("------------------------------")
print("List of Mails")
print("------------------------------")
for mails in mailslist:
	print(mails)
print("------------------------------")
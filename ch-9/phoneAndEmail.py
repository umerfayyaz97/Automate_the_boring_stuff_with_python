import re

phone_re = re.compile(r'''(
    (\d{3}|\(\d{3}\))? # Area code
    (\s|-|\.)? # Separator
    (\d{3}) # First three digits
    (\s|-|\.) # Separator
    (\d{4}) # Last four digits
    (\s*(ext|x|ext\.)\s*(\d{2,5}))? # Extension
    )''', re.VERBOSE)

email_re = re.compile(r'''([a-zA-z0-9.%+-]+ #usermame
                      @  #symbol
                      [a-zA-Z0-9.-]+ #domain name
                      (\.[a-zA-Z]{2,4}) #dot-somethins                
                    )''', re.VERBOSE)



text = '''Skip to main content
Home
Shopping cart
0 Items	Total: $0.00
Search
Enter your keywords 
Catalog
Merchandise
Blog
Early Access
Write for Us
About Us
Contact Us
Labor Day sale — desktop banner
Time left
00
days
 
20
hours
 
37
min
 
54
sec
Topics
Art & Design
General Computing
Hacking & Computer Security
Hardware / DIY
Kids
LEGO®
Linux & BSD
Manga
Programming
Python
R for All
Science & Math
Scratch
System Administration
Early Access
FREE ebook edition with every print book purchased from nostarch.com!
+

EARLY ACCESS lets you read full chapters months before a title's release date!
User login
Log in
Create account
Contact Us
Reach Us by Email - email is the best way to reach us
General inquiries or help with an order: info@nostarch.com
Bulk orders and special sales questions: sales@nostarch.com
Academic requests: academic@nostarch.com (Further information)
Conference and event inquiries: conferences@nostarch.com
Errata - please send any errata reports to: errata@nostarch.com
Media requests: media@nostarch.com
Proposals or editorial inquiries: editors@nostarch.com
Rights inquiries: rights@nostarch.com (Further information)
Interested in working with us? 
View our current job openings
Physical Address
No Starch Press Inc
245 8th Street
San Francisco, CA 94103
USA

Mailing Address
No Starch Press Inc
329 Primrose Road,  #42
Burlingame, CA 94010-4093
USA

Phone: 800.420.7240 or +1 415.863.9900
Fax: +1 415.863.9950

Reach Us on Social Media
Twitter Facebook Instagram Linkedin Pinterest

 
 

Navigation
My account
Want sweet deals?
Sign up for our newsletter.


About Us  |  Jobs!  |  Sales and Distribution  |  Rights  |  Media  |  Academic Requests  |  Conferences  |  FAQ  |  Contact Us  |  Write for Us  |  Privacy
Copyright 2025. No Starch Press, Inc '''


phone_numers = phone_re.findall(text)
emails = email_re.findall(text)

clean_numbers = [match[0] for match in phone_numers ]
# print(clean_numbers)

clean_emails = [match[0] for match in emails]
# print(clean_emails)

combined = clean_numbers + clean_emails
print(combined)
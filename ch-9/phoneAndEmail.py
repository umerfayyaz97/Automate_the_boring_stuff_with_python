import re

phone_re = re .compile(r'''(
    (\d{3}|\(\d{3}\))? # Area code
    (\s|-|\.)? # Separator
    (\d{3}) # First three digits
    (\s|-|\.) # Separator
    (\d{4}) # Last four digits
    (\s*(ext|x|ext\.)\s*(\d{2,5}))? # Extension
    )''', re.VERBOSE)

rmail_re = re.compile(r'''([a-zA-z0-9.%+-]+ #usermame
                      @  #symbol
                      [a-zA-Z0-9.-]+ #domain name
                      (\.[a-zA-Z]{2,4}) #dot-somethins                
                    )''', re.VERBOSE)

 
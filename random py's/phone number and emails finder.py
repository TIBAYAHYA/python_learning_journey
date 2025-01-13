import re,pyperclip
#phone number compiler
PHONE_REGEX = re.compile(r"""(
            ((\d{3})|(\(\d{3}\)))?          #area code which is optional
             (\s|-)                   #seperator
            \d{3}                  #triple digit
            -                  #seperator
            \d{4}                 #last 4 digits
            (\s(ext|x)(\.\s)?\d{2,5})?       # ext.123 | x4567 | ext 45| or nothing
            
            
            
                )
           """,re.VERBOSE)
#email compiler
email_regex = re.compile(r"""
                        [a-zA-Z.+_0-9]+
                        @
                        [a-zA-Z.+_0-9]+
                        
                        
                         """,re.VERBOSE)
text = pyperclip.paste()
extracted_phones = PHONE_REGEX.findall(text)
extracted_emails = email_regex.findall(text)
print(extracted_phones)
print(extracted_emails)
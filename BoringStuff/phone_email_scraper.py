#! python3
import re

phoneNumberRegex = re.compile(r'''
    # 111-111-1111
    # 222-2222
    # (123) 123-1234
    # ext 12345
    # ext. 12345
    # x12345
    (
        ((\d{3}-) | (\(\d{3}\)))?  # area code (optional)
        (\s|-)?                    # seperator
        (\d{3})                    # 3 digits
        (-)                        # seperator
        (\d{4})                    # 4 digits
        (\s)?                      # space between number and extension (optional)
        (
            ((ext(\.)?\s)|x)       # ext, ext. x
            (\d{2,5})              # 2-5 digits
        )?                         # extension (optional)
    )
''', re.VERBOSE)


results = phoneNumberRegex.search('123-456-7890 ext 12345')
print(results.group())

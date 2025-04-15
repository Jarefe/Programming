import re

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
phoneNumRegexAlt = re.compile(r'\d{3}-\d{3}-\d{4}')

testString = "my number is 123-456-7890"
phoneSearch = phoneNumRegexAlt.search(testString)
print('Phone number found: ' + phoneSearch.group())

phoneNumRegexGrouped = re.compile(r'(\d{3})-(\d{3}-\d{4})')
# mo = match objects
mo = phoneNumRegexGrouped.search(testString)
print('Phone number found: ' + mo.group())
print('Regex groups ' + str(mo.groups()))
# print('Area code: ' + mo.group(1))
# print('Rest of number: ' + mo.group(2))
# below lines functionally do the same as commented prints
area_code, main_number = mo.groups()
print('Area code: ' + area_code)
print('Main number: ' + main_number)
print()

# Matching multiple groups with pipe
pipeRegex = re.compile(r'Batman|Robin')
pipe1 = pipeRegex.search('Batman and Robin')
pipe2 = pipeRegex.search('Robin and Batman')
# pipe will find first occurrence of either string; effectively or operator
print(pipe1.group()) # Batman
print(pipe2.group()) # Robin
print()

batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
batMo = batRegex.search('Batcopter, batmobile')
print(batMo.group()) # Batcopter
print(batMo.group(1)) # copter
print()


# Optional matching
batwomanRegex = re.compile(r'Bat(wo)?man') # ()? indicates optional group
batMo1 = batwomanRegex.search('Batman Batwoman')
print(batMo1.group()) # Batman
batWomanMo = batwomanRegex.search('Batwoman batman')
print(batWomanMo.group()) # Batwoman
print()


# Matching 0 or more with *
starRegex = re.compile(r'Bat(wo)*man')
starMo1 = starRegex.search('test Batman')
starMo2 = starRegex.search('test Batwoman')
starMo3 = starRegex.search('Batwowowowowowowowoman')
print(starMo1.group()) # Batman
print(starMo2.group()) # Batwoman
print(starMo3.group()) # Batwowowowowowowowoman
print()


# Matching 1 or more with +
plusRegex = re.compile(r'Bat(wo)+man')
plusMo1 = plusRegex.search('Batman')
plusMo2 = plusRegex.search('Batwowowowoman')
print(plusMo1 is None) # nothing found
print(plusMo2.group()) # Batwowowowoman
print()


# Matching specific reptitions with {}
braceRegex = re.compile(r'(Ha){3}')
braceMo1 = braceRegex.search('HaHaHa')
braceMo2 = braceRegex.search('HaHaHaHaHa')
print(braceMo1.group()) # HaHaHa
print(braceMo2 is None) # nothing found
# (Ha){3,5} can match 3, 4, or 5 instances

# Python regex is greedy by default
# greedy = finds longest string that matches conditions
# non-greedy / lazy = find shortest string that matches

haString = 'HaHaHaHaHa'
greedyHaRegex = re.compile(r'(Ha){3,5}')
lazyHaRegex = re.compile(r'(Ha){3,5}?')

greedyMo = greedyHaRegex.search(haString)
lazyMo = lazyHaRegex.search(haString)

print(greedyMo.group()) # HaHaHaHaHa
print(lazyMo.group()) # HaHaHa
print()
# ? can either mean optional group or non-greedy match


# findall will return a list as long as there are NO GROUPS
phoneRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') # has no groups
print(phoneRegex.findall('Cell: 415-555-9999 Work: 212-555-0000'))
# ['415-555-9999', '212-555-0000']

# if groups are present, then a list of tuples will be returned
groupedPhoneRegex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)') # has groups
print(groupedPhoneRegex.findall('Cell: 415-555-9999 Work: 212-555-0000'))
# [('415', '555', '9999'), ('212', '555', '0000')]
print()


# ^ looks at beginning, $ looks at end
beginsWithHello = re.compile(r'^Hello')
print(beginsWithHello.search('Hello world').group()) # Hello
print(beginsWithHello.search('He says hellow') is None) # None found

endsWithNumber = re.compile(r'\d$')
print(endsWithNumber.search('The number is 34').group()) # 4
print(endsWithNumber.search('34 is the number') is None) # None found

wholeStringIsNumber = re.compile(r'^\d+$')
print(wholeStringIsNumber.search('123456789').group()) # 123456789
print(wholeStringIsNumber.search('123xyz789') is None) # None found
print()


# . matches any char except newline
atRegex = re.compile(r'.at')
print(atRegex.findall('The cat in the hat sat on the flat mat.'))
# ['cat', 'hat', 'sat', 'lat', 'mat']
print()


# Match everything except newline with .*
fullNameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
fullname = fullNameRegex.search('First Name: Al Last Name: Sweigart')
print(fullname.groups()) # ('Al', 'Sweigart')


# Match newline with .
noNewlineRegex = re.compile('.*')
print(noNewlineRegex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.').group())
# 'Serve the public trust.'

newlineRegex = re.compile('.*', re.DOTALL)
print(newlineRegex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.').group())
# Serve the public trust.
# Protect the innocent.
# Uphold the law.
print()


# Case insensitive matching
robocop = re.compile(r'robocop', re.I)
print(robocop.findall('Robocop, roboCOP, RoBoCop, robocop, ROBOCOP'))
# ['Robocop', 'roboCOP', 'RoBoCop', 'robocop', 'ROBOCOP']
print()


# Substituting with regex
redactRegex = re.compile(r'Agent \w+')
print(redactRegex.sub('REDACTED', 'Agent Alice gave the secret documents to Agent Bob.'))
# REDACTED gave the secret documents to REDACTED.

agentNamesRegex = re.compile(r'Agent (\w)\w*')
print(agentNamesRegex.sub(r'\1****', 'Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent.'))
# A**** told C**** that E**** knew B**** was a double agent.
print()



# Managing complex regex
complexPhoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?            # area code
    (\s|-|\.)?                    # separator
    \d{3}                         # first 3 digits
    (\s|-|\.)                     # separator
    \d{4}                         # last 4 digits
    (\s*(ext|x|ext.)\s*\d{2,5})?  # extension
    )''', re.VERBOSE)
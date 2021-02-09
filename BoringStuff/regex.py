import re

phoneNumberRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
results = phoneNumberRegex.findall('Hello there, my phone number is 161-616-6161, my wife\'s number is 171-717-1717')

print(results)

phoneNumberRegexGrouped = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
results = phoneNumberRegexGrouped.search('Hello there, my phone number is 161-616-6161, my wife\'s number is 171-717-1717')
print(results.group(1))
print(results.group(2))

phoneNumberRegexParens = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')

results = phoneNumberRegexParens.search('Hello there, my phone number is (161) 616-6161')
print(results.group(1))
print(results.group(2))

batRegex = re.compile(r'Bat(man|mobile|copter|bat)')

results = batRegex.findall('Batman was driving the Batmobile')
print(results)

batRegex = re.compile(r'Bat(wo)?man')  # ? matches 0 or 1. so Batman or Batwoman work here
results = batRegex.search('Adventures of Batman')
print(results.group())
results = batRegex.search('Adventures of Batwoman')
print(results.group())
results = batRegex.search('Adventures of Batwowoman')
print(results)

phoneNumberRegexOptionalParens = re.compile(r'(\d\d\d-)?(\d\d\d-\d\d\d\d)')
batRegex = re.compile(r'Bat(wo)*man')  # * matches 0 or more. so Batman or Batwoman or Batwowoman work here
results = batRegex.search('Adventures of Batman')
print(results.group())
results = batRegex.search('Adventures of Batwoman')
print(results.group())
results = batRegex.search('Adventures of Batwowoman')
print(results.group())

batRegex = re.compile(r'Bat(wo)+man')  # + matches 1 or more. so Batwoman or Batwowoman work here
results = batRegex.search('Adventures of Batman')
print(results)
results = batRegex.search('Adventures of Batwoman')
print(results.group())
results = batRegex.search('Adventures of Batwowoman')
print(results.group())


phoneNumberRegexSmaller = re.compile(r'(\d){3}-((\d){3}-(\d){4})')
results = phoneNumberRegexGrouped.search('Hello there, my phone number is 161-616-6161, my wife\'s number is 171-717-1717')
print(results.group())

# Greedy vs non greedy
# Greedy matches the longest string possible, nongreedy the shortest
greedyNum = re.compile(r'(\d){3,5}')
results = greedyNum.search('1234567890')
print(results.group())

nonGreedyNum = re.compile(r'(\d){3,5}?')  # ? makes this a non greedy match
results = nonGreedyNum.search('1234567890')

print(results.group())

greedyAny = re.compile(r'<(.*)>')

results = greedyAny.findall('<Hello there> How are you today>')
print(results)

nonGreedyAny = re.compile(r'<(.*?)>')
results = nonGreedyAny.findall('<Hello there> How are you today>')
print(results)

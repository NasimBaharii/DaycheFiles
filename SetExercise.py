

myParagraph = 'The chair sat in the corner where it had are! for are 25 years. The only is. was there was someone am sitting in it. are long had it been since am had done that? Ten years or more he imagined. Yet there was no is? the presence in the chair now. Please LIKE & SHARE to keep our generators available! Click Like He knew what he was supposed to do. That had been apparent from the beginning. That was what made the choice so difficult. What he was supposed to do and what he would do were not the same. This would have been fine if he were willing to face the inevitable consequences, but he was.'
# myParagraph = 'I am is are'

world = ''
worldList = []
for world in myParagraph.split(" "):
    worldList += [world]

print('Total Number of World is: ', len(worldList))
print('=' * 40)
print('Total Number of Union World is: ', len(set(worldList)))
print('=' * 40)

amNumber = worldList.count('am') + worldList.count('am.') + worldList.count('am!') + worldList.count('am?')
isNumber = worldList.count('is') + worldList.count('is!') + worldList.count('is?') + worldList.count('is.')
areNumber = worldList.count('are') + worldList.count('are.') + worldList.count('are!') + worldList.count('are?')
wasNumber = worldList.count('was') + worldList.count('was.') + worldList.count('was!') + worldList.count('was?')
wereNumber = worldList.count('were') + worldList.count('were.') + worldList.count('were!') + worldList.count('were?')

print('Total Number of "to be" is: ', (amNumber + isNumber + areNumber + wasNumber + wereNumber))
print('=' * 40)

print('Number of "am" are:', amNumber)
print('Number of "is" are:', isNumber)
print('Number of "are" are:', areNumber)
print('Number of "was" are:', wasNumber)
print('Number of "were" are:', wereNumber)
print('=' * 40)


# world = ''
# worldList = []
# for char in myParagraph:
#     if char != ' ':
#         world += char
#     else:
#         worldList += [world]
#         world = ''
# worldList += [world]
#
# print(worldList)
# print('Total Number of World is: ', len(worldList))
#
# worldSet = set(worldList)
# # print(worldSet)
# print('Total Number of Union World is: ', len(worldSet))
#
# # amNumber = worldList.count('am') + worldList.count('am.') + worldList.count('am!') + worldList.count('am?')
# # # isNumber = worldList.count('is', 'is!', 'is?', 'is.') # wrong!
# # isNumber = worldList.count('is') + worldList.count('is!') + worldList.count('is?') + worldList.count('is.')
# # areNumber = worldList.count('are') + worldList.count('are.') + worldList.count('are!') + worldList.count('are?')
# # wasNumber = worldList.count('was') + worldList.count('was.') + worldList.count('was!') + worldList.count('was?')
# # wereNumber = worldList.count('were') + worldList.count('were.') + worldList.count('were!') + worldList.count('were?')
#
# amNumber = 0
# isNumber = 0
# areNumber = 0
# wasNumber = 0
# wereNumber = 0
#
# for eachWorld in worldList:
#     print(eachWorld)
#     if eachWorld == 'am':
#         amNumber += 1
#     elif eachWorld == 'is':
#         isNumber += 1
#     elif eachWorld == 'are':
#         areNumber += 1
#     elif eachWorld == 'was':
#         wasNumber += 1
#     elif eachWorld == 'were':
#         wereNumber += 1
#
# print('Total Number of "to be" is: ', (amNumber + isNumber + areNumber + wasNumber + wereNumber))
#
# print('Number of "am" are:', amNumber)
# print('Number of "is" are:', isNumber)
# print('Number of "are" are:', areNumber)
# print('Number of "was" are:', wasNumber)
# print('Number of "were" are:', wereNumber)
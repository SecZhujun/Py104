
# -*- coding:utf-8 -*-

formatter = "%r %r %s %r"

print formatter % (1,2,3,4)
print formatter % ("one", "two", "three", "four")
print formatter % (True,False,True,False)
print formatter % (formatter,formatter,formatter,formatter)
print formatter % (
"I had a thing.",
"that you could type up right.",
"But you didn't sing",
"haha."
)

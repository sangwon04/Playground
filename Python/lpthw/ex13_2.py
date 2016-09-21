from sys import argv

first, first_name, last_name, age = argv

final_age = int(age) + 10

print "Ten years from now, %s %s will be %r years old." % (first_name, last_name, final_age)

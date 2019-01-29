# import pdb
# pdb.set_trace()
count = 1

while count <= 5:
    try:
        number = input("Enter number: ")
        print "Divide 100 by the number {} is : {}".format(number, 100/number)
        break
    except Exception as E:
        count += 1
    # else:       # If try successfully execute then this else block is execute
        # print "here is else"
    # finally:    # Every time finally block will be execute
        # print "here is finally"
else:
    print 'Account blocked'

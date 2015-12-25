def donuts(count):
  if count < 10:
    print 'Number of donuts: ' + str(count)
  else:
    print 'Number of donuts: many'

def main():
    print donuts(4)

if __name__ == '__main__':
  main()

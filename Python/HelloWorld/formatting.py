for i in range(1,13):
    print("No.{0:2} squared is {1:3} and cubed is {2:4}".format(i, i ** 2, i** 3))

print()
print("Pi is approximately {0:12}".format( 22 /7)) #general format 15 decimals.
print("Pi is approximately {0:12f}".format( 22 /7)) #floating point default 6 decimals.
print("Pi is approximately {0:12.50f}".format( 22 /7)) # floating, 50 decimals.
print("Pi is approximately {0:52.50f}".format( 22 /7)) #ignores the width and goes for precision.
print("Pi is approximately {0:62.50f}".format( 22 /7)) #50 decimals
print("Pi is approximately {0:72.50f}".format( 22 /7))  # 50 decimals in 72w

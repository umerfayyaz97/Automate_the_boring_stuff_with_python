# import time, sys
# indent = 0 # How many spaces to indent
# indentIncreasing = True # Whether the indentation is increasing or not
# try:
#     while True: # The main program loop
#         print(' ' * indent, end='')
#         print('********')
#         time.sleep(0.1) # Pause for 1/10th of a second.
#         if indentIncreasing:
# # Increase the number of spaces:
#             indent = indent + 1
#             if indent == 20:
# # Change direction:
#                 indentIncreasing = False
#         else:
# # Decrease the number of spaces:
#             indent = indent - 1
#         if indent == 0:
# # Change direction:
#             indentIncreasing = True
# except KeyboardInterrupt:
#     sys.exit()


# import time, sys
# try:
#     while True: # The main program loop
# # Draw lines with increasing length:
#         for i in range(1, 9):
#             print('-' * (i * i))
#             time.sleep(0.1)
# # Draw lines with decreasing length:
#         for i in range(7, 1, -1):
#             print('-' * (i * i))
#             time.sleep(0.1)
# except KeyboardInterrupt:
#     sys.exit()


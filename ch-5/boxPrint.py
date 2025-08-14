# def box_print(sybmol, width, height):
#     if len(sybmol) != 1:
#         raise Exception("Symbol must be a single character string")
#     if width <=2:
#         raise Exception("Width must be greater than 2")
#     if height <=2 :
#         raise Exception("Height must be greater than 2")
    
#     print(sybmol * width)
#     for i in range (height - 2):
#         print(sybmol + (' ' * (width-2)) + sybmol)
#     print(sybmol * width)
    
    
# try:
#     box_print("*", 4,4)
#     box_print('0', 20,5)
#     box_print('zz',3,3)
# except Exception as err:
#     print('An exception happened: ' + str(err))




# with open('image.png','rb')as f:
#     input=f.read()
#     print(type(input))
# with open('image_copy.png','wb')as f:
#     f.write(input)
#     print('image copied successfully...!')


# '''zipfile'''
# import zipfile
# with zipfile.ZipFile('sample.zip','w')as zipf:
#  zipf.write('file2.csv')
#  zipf.write('file3.csv')
#  print('files added to zip file..!')
#  print('files zipped  successfully...!')

# '''zipfile'''
# import zipfile
# with zipfile.ZipFile('sample.zip','r')as zipf:
#  print('Files in the zip archive:')
#  for files_name in zipf.namelist():
#   print(files_name)
# zipf.extractall()
# print('All files have been extracted successfully...!')
  
# import zipfile
# with zipfile.ZipFile('sample.zip','r')as zipf:
#    names=zipf.namelist()
#    print('file in zip:')
#    for i in names:
#        print(zipf.read(i))




import os
filename = "EP103_SQ001_SH0170_LGT_v004.ma"
dict = {}

filenameNoExt   = os.path.splitext(filename) [0]
filenameSplit   = filenameNoExt.split('_')
episode         = filenameSplit[0][2:]
# episode         = episode[2:]
sequence        = filenameSplit[1]
sequence        = sequence[2:]
shot            = filenameSplit[2]
shot            = shot[2:]
departament     = filenameSplit[3]
version         = filenameSplit[4]
version         = version[1:]


# for (x in filenameSplit):
#     if (len(x) == 5):

dict["Episode"]     = episode
dict["Sequence"]    = sequence
dict["Shot"]        = shot
dict["Department"]  = departament
dict["Version"]     = version

print("filename is ", filename)
print("('filename', 'ext') is ", os.path.splitext(filename))
print("filenameNoExt is ", filenameNoExt)
print("filenameSplit is ", filenameSplit)
print("\n")
# print("{'Episode': ", episode, ",")
# print(" 'Sequence': ", sequence, ",")
# print(" 'Shot': ", shot, ",")
# print(" 'Department': ", departament, ",")
# print(" 'Version': ", version, "}")
print("dict is ", dict)

def FilenameInfo(self, filename):
    pass

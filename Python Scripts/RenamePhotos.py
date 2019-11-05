import os
os.getcwd()
collection = "E:/DocumentsHDD/facenetdatasets/datasets/casia/CASIA-maxpy-clean/Liam_Keane/"
i = 1
for i, filename in enumerate(os.listdir(collection)):
    os.rename("E:/DocumentsHDD/facenetdatasets/datasets/casia/CASIA-maxpy-clean/Liam_Keane/" + filename, "E:/DocumentsHDD/facenetdatasets/datasets/casia/CASIA-maxpy-clean/Liam_Keane/" + "Liam_Keane" + str(i) + ".jpg")
    i+1
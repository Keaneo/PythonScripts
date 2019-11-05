#!/usr/bin/python
import os

for N in (1, 4):
    os.system('python E:/DocumentsHDD/facenet-master/src/align/align_dataset_mtcnn.py E:/DocumentsHDD/facenetdatasets/datasets/casia/CASIA-maxpy-clean/ E:/DocumentsHDD/facenetdatasets/datasets/casia/casia_maxpy_mtcnnpy_182 --image_size 182 --margin 44 --random_order --gpu_memory_fraction 0.5 & done')

#def main(args):
#
 #   for N in (1, 4):        
  #      python src/align/align_dataset_mtcnn.py
   #     E:/DocumentsHDD/facenetdatasets/datasets/casia/CASIA-maxpy-clean/ \
    #    E:/DocumentsHDD/facenetdatasets/datasets/casia/casia_maxpy_mtcnnpy_182 \
     #   --image_size 182 \
      #  --margin 44 \
       # --random_order \
        #--gpu_memory_fraction 0.25 \
         #& done
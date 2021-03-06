from random import randint
from os import listdir, chdir, getcwd
from shutil import move

base_path = '/home/Dataset'

train_imgs = base_path + '/TrainingSet/Imgs'
train_gt = base_path + '/TrainingSet/GT'

test_imgs = base_path + '/TestingSet/Imgs'
test_gt = base_path + '/TestingSet/GT'

#Ramdomly select images from training set

testset_size = len(listdir(train_imgs)) // 2

for i in listdir(train_imgs):
    if randint(0, 1) and testset_size > 0:
        move(train_imgs + '/' + i, test_imgs)
        testset_size -= 1
        move(train_gt + '/' + i, test_gt)
    

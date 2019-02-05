from __future__ import division
from PIL import Image,ImageMath
import shutil,os
hero_size = 200

os.chdir(os.path.dirname(__file__))
folder1=  os.getcwd() + '//images\PNG Sequences_golem3\Idle'
to1 =  os.getcwd() + '//images\PNG Sequences_golem3\Idle_'
folder2 = os.getcwd() + '//images\PNG Sequences_golem3\Running'
to2 =  os.getcwd() + '//images\PNG Sequences_golem3\Running_'
folder3 = os.getcwd() + '//images\PNG Sequences_golem3\Slashing'
to3 = os.getcwd() + '//images\PNG Sequences_golem3\Slashing_'

folder_array = [folder1,folder2,folder3]
to_array = [to1,to2,to3]

#delete
for i in range(len(to_array)):
    to = to_array[i]
    for the_file in os.listdir(to):
        file_path = os.path.join(to, the_file)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
            #elif os.path.isdir(file_path): shutil.rmtree(file_path)
        except Exception as e:
            print(e)
#copy
for i in range(len(folder_array)):
    src = folder_array[i]
    dest = to_array[i]
    src_files = os.listdir(src)
    for file_name in src_files:
        full_file_name = os.path.join(src, file_name)
        if (os.path.isfile(full_file_name)):
            shutil.copy(full_file_name, dest)
# optimize
for i in range(len(to_array)):
    cur_dir = to_array[i]
    src_files = os.listdir(cur_dir)
    for file_name in src_files:
        full_file_name = os.path.join(cur_dir, file_name)
        im = Image.open(full_file_name)
        im = im.resize((hero_size,hero_size))
        im = im.convert('P')
        im.save(full_file_name)





'''
for i in range(n):
    index =''
    if i <= 9:
        index += '0'
    index += str(i)
    original_path = 'images/PNG Sequences_golem3/Idle_/0_Golem_Idle_0' + index + '.png'
    original = Image.open(original_path)
    #result = original.convert('P', palette=Image.ADAPTIVE, colors=8)
    #result.show()
    width, height = original.size
    #print('The original image size is {wide} wide x {height} '
          #'high'.format(wide=width, height=height))

    resized_image = original.resize((128,128))
    width, height = resized_image.size
    #print('The resized image size is {wide} wide x {height} '
          #'high'.format(wide=width, height=height))
    #resized_image.show()
    resized_image = resized_image.convert('P')
    resized_image.save(original_path)
'''


from __future__ import division
from PIL import Image,ImageMath
import shutil,os
hero_size = 200

os.chdir(os.path.dirname(__file__))
folder1=  os.getcwd() + '//images\PNG Sequences_golem1\Idle'
to1 =  os.getcwd() + '//images\PNG Sequences_golem1\Idle_Red'
folder2 = os.getcwd() + '//images\PNG Sequences_golem1\Running'
to2 =  os.getcwd() + '//images\PNG Sequences_golem1\Running_Red'
folder3 = os.getcwd() + '//images\PNG Sequences_golem1\Slashing'
to3 = os.getcwd() + '//images\PNG Sequences_golem1\Slashing_Red'

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
# optimize and make red
for i in range(len(to_array)):
    cur_dir = to_array[i]
    src_files = os.listdir(cur_dir)
    for file_name in src_files:
        full_file_name = os.path.join(cur_dir, file_name)
        im = Image.open(full_file_name)
        im = im.convert('RGBA')
        width, height = im.size
        for x in range(width):
            for y in range(height):
                current_color = im.getpixel((x, y))
                R, G, B, A = current_color
                if A == 0:
                    continue
                new_color = (255, G, B)
                im.putpixel((x, y), new_color)
        im = im.resize((hero_size,hero_size))
        im = im.convert('P')
        im.save(full_file_name)








from __future__ import division
from PIL import Image,ImageMath

'images/PNG Sequences_golem3/Idle_/0_Golem_Running_000.png'
folder =''
n = 18
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


# 2023 - dmlxe

from PIL import Image, ImageDraw
import sys

def sortPixels(img_in, direction, order, delta):
    # Get weight and height of the source Image
    axis_X, axis_Y = img_in.size
    # Delta variables
    delta = int(delta)
    control_X = axis_X / delta
    control_Y = axis_Y / delta
    # Create the output Image
    img_out = Image.new('RGB', (axis_X,axis_Y))
    draw_img_out = ImageDraw.Draw(img_out)
    # Controls the direction where the algorithm is going to sort
    if direction == 'v':
        axis = axis_X
        control = control_Y 
    elif direction == 'h':
        axis = axis_Y
        control = control_X
    else:  
        print ('No valid direction given')
        return False
    for i in range(delta):
        row = []
        for x in range(axis):
            # Get the pixel rows from the source Image
            for y in range(int(i*control), int((i+1)*control)):
                if direction == 'v':
                    pixel = img_in.getpixel((x,y))
                elif direction == 'h':
                    pixel = img_in.getpixel((y,x))
                row.append(pixel)
            # Sort the array
            row.sort(reverse=order)
            # Put the sorted pixels on the output Image
            for y in range(int(i*control), int((i+1)*control)):
                if direction == 'v':
                    draw_img_out.point((x,y), row.pop())
                elif direction == 'h':
                    draw_img_out.point((y,x), row.pop())
    return img_out

if __name__ == "__main__":
    script, orientation, order, delta, filename_out, filename_in = sys.argv
    # Get the source image
    img_in = Image.open(filename_in)
    # Determines the sorting order
    if order == '-a':
        order = False
    elif order == '-d':
        order = True
    # Determines the sorting direction, execute the sorting algorithm and saves the output Image
    if orientation == '-h':
        sortPixels(img_in, 'h', order, delta).save(filename_out + ".png")
    elif orientation == '-v':
        sortPixels(img_in, 'v', order, delta).save(filename_out + ".png")
    elif orientation == '-hv':
        sortPixels(sortPixels(img_in, 'h', order, delta), 'v', order, delta).save(filename_out + ".png")
    elif orientation == '-vh':
        sortPixels(sortPixels(img_in, 'v', order, delta), 'h', order, delta).save(filename_out + ".png")
    else:
        print ("Invalid input")
        exit()
    print ("Done!")
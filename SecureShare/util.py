from PIL import Image
from numpy import asarray
 
def rgba_to_hex(r, g, b, a):
    return '#{:02x}{:02x}{:02x}{:02x}'.format(r, g, b, a)

def rgb_to_hex(r, g, b):
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)

def genHex(filename):
    img = Image.open(filename)
    numpydata = asarray(img)

    rows = img.height
    columns = img.width
    matrix = [[0 for x in range(columns)] for y in range(rows)] 

    for i in range(0,rows):
        for j in range(0,columns):
            if img.mode == "RGBA":
                matrix[i][j] = (rgba_to_hex(numpydata[i][j][0],numpydata[i][j][1],numpydata[i][j][2], numpydata[i][j][3]))
            else:
                matrix[i][j] = (rgb_to_hex(numpydata[i][j][0],numpydata[i][j][1],numpydata[i][j][2]))
    return matrix, img.mode

def genImg(reconstructFile, matrix, mode):
    height = len(matrix)
    width = len(matrix[0])
    img = Image.new(mode, (width, height))

    # Loop over each pixel in the array and set the color in the image
    # import pdb; pdb.set_trace()
    for y in range(height):
        for x in range(width):
            # print("here before")
            color = matrix[y][x]
            img.putpixel((x, y), tuple(int(color[i:i+2], 16) for i in (1, 3, 5)))

    # Save the image to a file
    img.save(reconstructFile)

def padded_hex(i, l):
    given_int = i
    given_len = l

    hex_result = hex(given_int)[2:] # remove '0x' from beginning of str
    num_hex_chars = len(hex_result)
    extra_zeros = '0' * (given_len - num_hex_chars) # may not get used..

    return ('0x' + hex_result if num_hex_chars == given_len else
            '?' * given_len if num_hex_chars > given_len else
            '0x' + extra_zeros + hex_result if num_hex_chars < given_len else
            None)

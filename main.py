#https://arxiv.org/pdf/1408.3245.pdf
from PIL import Image
import numpy as np
from scipy.interpolate import lagrange as lag
import os
import util.util as util

def polynomial(img, n, k):
    '''
        Generate lagrange polynomial of degree k-1
        f(x) = c1(x^k) + c2(x^k-1) .... + secret (mod prime)
        prime > secret
    '''
    coef = np.random.randint(low = 0, high = 251, size = (img.shape[0], k - 1)) #Coefficients should not exceed value of prime number chosen
    gen_imgs = []
    for i in range(1, n + 1):
        base = np.array([i ** j for j in range(1, k)])
        base = np.matmul(coef, base)
        imgValue_ = (img + base) % 251
        gen_imgs.append(imgValue_)
    return np.array(gen_imgs)

def reconstruct(imgs, index, k):
    '''
        Reconstruct image using share index values for k shares
    '''
    print("Shares: ", index)
    assert imgs.shape[0] >= k
    x = np.array(index)
    dim = imgs.shape[1]
    img = []
    for i in range(dim):
        if i % 10000 == 0:
            print("Reconstructing pixel ", i, " of ", dim, " pixels")
        y = imgs[:, i]
        poly = lag(x, y)
        pixel = poly(0) % 251
        img.append(pixel)
    return np.array(img)

    
if __name__ == "__main__":
    #Secret split
    path = input("\nEnter the image path you wish to split into shares: ")
    pathPrefix = path.split('.')[0]
    os.makedirs(pathPrefix, exist_ok=True)

    
    n, k = map(int,input("\nEnter the space separated values of n and k: ").split())
    img_flattened, shape = util.read_image(path)
    gen_imgs = polynomial(img_flattened, n = n, k = k)
    to_save = gen_imgs.reshape(n, *shape)
    for i, img in enumerate(to_save):
        Image.fromarray(img.astype(np.uint8)).save(pathPrefix + "/share" + "_{}.jpeg".format(i + 1))
    print("\n -----Shamir secret sharing is complete-----")
    
    #Secret reconstruction
    shareIndex = list(map(int, input("\nEnter the index of shares to reconstruct: ").split()))
    origin_img = reconstruct(gen_imgs, shareIndex, k = k)
    origin_img = origin_img.reshape(*shape)
    Image.fromarray(origin_img.astype(np.uint8)).save(pathPrefix + "/reconstructed_image.jpeg")
    print("Shamir secret reconstruction is complete")



    
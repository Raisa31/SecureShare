import argparse
import os
from StegaStamp.encode_image import encode_image
from StegaStamp.decode_image import decode_secret
from shamir_algo import generate_and_reconstruct_image
import warnings
warnings.filterwarnings("ignore")

current_dir = os.getcwd()
parser = argparse.ArgumentParser()
parser.add_argument("-i", "--image", help = "Enter absolute path of the image to be used", type = str)
parser.add_argument("-n", "--n_shares", help = "Enter number of shares to be generated", type = int)
parser.add_argument("-t", "--threshold", help = "Enter number of shares as threshold for reconstructing secret", type = int)
parser.add_argument("-s", "--secret", help = "Enter the secret", type = str)
parser.add_argument('--model', type=str, default = f"{os.getcwd()}/StegaStamp/saved_models/stegastamp_pretrained/")
parser.add_argument('--images_dir', type=str, default=None)
parser.add_argument('--save_dir', type=str, default=f"{current_dir}/")
parser.add_argument('--secret_size', type=int, default=100)
args = parser.parse_args()

encode_image(args)
for file_name in os.listdir(current_dir):
  if file_name.find("hidden")!=-1:
    os.replace(file_name, f"{current_dir}/encoded_image.png")
  if file_name.find("residual")!=-1:
    os.remove(file_name)

generate_and_reconstruct_image(args)
args.image = "img_reconst.png"


decode_secret(args)

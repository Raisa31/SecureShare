# SecureShare: Secret obfuscation and distribution for data security

SecureShare is designed to enhance data privacy and security. This project utilizes [StegaStamp](https://github.com/tancik/StegaStamp) to encode secret text within an image and Shamir's Secret Sharing algorithm  is used to distribute hidden information across multiple shares. By embedding the secret within an image file, we provide an additional layer of secrecy to prevent unauthorized access. 

This repository contains:

1. Documentation on the project implementation and methods used
2. Python Script to execute SecureShare for data encoding

## Install

This project uses [python3](https://www.python.org/) and [conda](https://docs.conda.io/en/latest/) . These are the steps to install and run this project on your local machine

```
conda create -n secureshare python=3.6
pip install -r requirements.txt
```

Download saved models with the following steps:
```
cd StegaStamp
wget http://people.eecs.berkeley.edu/~tancik/stegastamp/saved_models.tar.xz
tar -xJf saved_models.tar.xz
rm saved_models.tar.xz
```
## Usage
After installation of the required libraries, execute the project using the following command in the base directory
```
python main.py -i {image_path} -n {no_of_shares_to_generate} -t {no_of_threshold_shares} -s {secret}
```

## Authors

[@RaisaArief](https://github.com/Raisa31)
[@SohamJagtap](https://github.com/SohamJagtap)

## License
[MIT](LICENSE) © Raisa Arief, Soham Jagtap
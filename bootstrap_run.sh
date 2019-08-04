#!/bin/bash
# Install Python 2 kernel
sudo yum update -y
curl -O https://repo.continuum.io/archive/Anaconda3-5.0.1-Linux-x86_64.sh
bash Anaconda3-5.0.1-Linux-x86_64.sh -b 
conda create -n py27 python=2.7 anaconda
source /opt/conda/envs/py27/bin/activate
apt-get update
apt-get install -y gcc
cd ..
cd /opt/conda/envs/py27/bin
python -m pip install --upgrade ipykernel
python -m ipykernel install 
#sudo yum install python-setuptools
#sudo yum install python-pip
#sudo yum install python34-setuptools
#sudo yum install easy_install pip
#sudo yum install python34-pip
#sudo yum install python-pip
#sudo yum apt-get update
#sudo pip install -U ujson pandas scikit-learn scipy numpy nltk imbalanced-learn networkx sklearn itertools 
# Install libraries for Python2


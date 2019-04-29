#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 14:24:32 2019

@author: yijingyang
"""

from bs4 import BeautifulSoup
import numpy as np
import requests
import cv2
import urllib
import matplotlib.pyplot as plt
import random
import os
import socket
#from urllib.request import urlopen

def url_to_image(url):
# download the image, convert it to a NumPy array, and then read
# it into OpenCV format
#    opener = urllib.request.build_opener()
#    opener.addheaders = [('User-agent','Mozilla/49.0.2')]
    try:
#        op1ener.open(url)
        resp = urllib.request.urlopen(url,timeout=1)        
    except urllib.error.HTTPError:
        print('find one HTTPError')
        return 0
    except urllib.errorURLError:
        print('find one URLError')
        return 0
    except socket.timeout:
        print('time out')
        return 0
            
    image = np.asarray(bytearray(resp.read()), dtype="uint8")
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)
    image = cv2.resize(image,(224,224))
    # return the image
    return image

def main():       
    startp = 0
    # number of images per class
    n_of_training_images=10  
    # read in the wordnet id list
    infile = open("./wnids1000.txt","r")
    lines = infile.readlines()
    wnids = []
    for line in lines:
        wnids.append(line.strip('\n').split(' ')[0])
    wnids = wnids[startp:]
    # download images
    for i in range(len(wnids)):
        print("preparing class #%d"%(i+startp))
        # create sub folders
        root = "./images/"+str(i+startp)
        folder = os.path.exists(root)
        if not folder:
            os.makedirs(root)
        # start downloading (BeautifulSoup is an HTML parsing library)
        url = "http://www.image-net.org/api/text/imagenet.synset.geturls?wnid=" + wnids[i]
        page = requests.get(url)#ship synset
        soup = BeautifulSoup(page.content, 'html.parser')#puts the content of the website into the soup variable, each url on a different line
        str_soup=str(soup) #convert soup to string so it can be split
        type(str_soup)
        split_urls=str_soup.split('\r\n')#split so each url is a different possition on a list
        # shuffle
        random.shuffle(split_urls)
        print(len(split_urls))#print the length of the list so you know how many urls you have
        # store images
        nn = 0
        kk = 0
        while(nn<n_of_training_images and kk<len(split_urls)):
            if not split_urls[kk] == None:
                try:
                    I = url_to_image(split_urls[kk])
                    if I.any():
                        if (len(I.shape))==3: #check if the image has width, length and channels
#                            plt.imshow(I)
#                            plt.show()
                            if np.mean(I)<250: # remove failed images (almost all white)
                                save_path = root+'/img'+str(nn)+'.jpg'#create a name of each image                
                                cv2.imwrite(save_path,I)
                                nn=nn+1
                except:
                    None
            kk=kk+1
            if kk==len(split_urls):
                print("not enough valid images!")

if __name__ == '__main__':
    main()

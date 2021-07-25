#!/usr/bin/env python3

import sys

import cv2 as cv

from read_image import read_image
from display_image import display_image

def find_and_decode_qrcode(image_matrix):
  print("[INFO] Find and decode QRCode")
  return cv.QRCodeDetector().detectAndDecode(image_matrix)

if __name__ == "__main__":
  if len(sys.argv) != 2:
    print("Usage : {} <IMAGE_FILE>".format(sys.argv[0]))
    sys.exit(1)

  image_file_path = sys.argv[1]
  print("[INFO] Using '{}' image file as datasource".format(image_file_path))

  image_matrix = read_image(image_file_path)

  data, bbox, rectifiedImage = find_and_decode_qrcode(image_matrix)

  display_image(rectifiedImage)

  if len(data) > 0:
    print("[INFO] Found data :")
    print(data)
  else:
    print("[WARNING] No data found")
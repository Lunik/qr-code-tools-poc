#!/usr/bin/env python3

import sys

import cv2 as cv

from read_image import read_image

def display_image(image_matrix):
  print("[INFO] Displaying image from matrix".format(image_matrix))
  cv.imshow("Display window", image_matrix)
  k = cv.waitKey(0)

if __name__ == "__main__":
  if len(sys.argv) != 2:
    print("Usage : {} <IMAGE_FILE>".format(sys.argv[0]))
    sys.exit(1)

  image_file_path = sys.argv[1]
  print("[INFO] Using '{}' image file as datasource".format(image_file_path))

  image_matrix = read_image(image_file_path)

  display_image(image_matrix)
#!/usr/bin/env python3

import sys

import cv2 as cv

def read_image(image_file_path):
  print("[INFO] Reading file '{}'".format(image_file_path))
  return cv.imread(image_file_path)

if __name__ == "__main__":
  if len(sys.argv) != 2:
    print("Usage : {} <IMAGE_FILE>".format(sys.argv[0]))
    sys.exit(1)

  image_file_path = sys.argv[1]
  print("[INFO] Using '{}' image file as datasource".format(image_file_path))

  image_matrix = read_image(image_file_path)

  image_width = len(image_matrix)
  image_height = len(image_matrix[0])

  print("[INFO] Image is '{}' pixels width and '{}' pixels height".format(image_width, image_height))

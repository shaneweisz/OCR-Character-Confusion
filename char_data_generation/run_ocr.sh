# Runs tesseract ocr on a given image file
# $1 --> path to the image file to run ocr on
# $2 --> name of the output file to send recognized text to after ocr
# Example Usage: ./run_ocr.sh image_test.png recognized_chars

tesseract $1 $2 -l 'eng' --psm 6 --oem 1 --tessdata-dir ./tesseract_files\

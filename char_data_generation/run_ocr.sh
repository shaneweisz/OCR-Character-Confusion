# $1 --> path to the .tif file to run ocr on
# $2 --> name of the output file to send recognized text to after ocr

tesseract $1 $2 -l 'eng' --psm 6 --tessdata-dir ../tesseract_files \

# Converts a text file to images in various selected fonts
# to be used to run Tesseract's OCR on

PANGOCAIRO_BACKEND=fc \
text2image --text ./char_data_generation/random_chars.txt\
   --outputbase './char_data_generation/font_images/image'\
   --fonts_dir ./char_data_generation/selected_fonts\
   --find_fonts true\
   --degrade_image false\
   --rotate_image false\
   --bidirectional_rotation false

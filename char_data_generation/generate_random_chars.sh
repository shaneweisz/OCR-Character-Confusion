#!/bin/bash
# Generate test images for tesseract using text2image.

PANGOCAIRO_BACKEND=fc \
text2image \
   --text random_chars.txt\
   --fonts_dir /Library/Fonts\
   --font 'Verdana' \
   --ptsize 12\
   --outputbase 'test_data'\
   --resolution 300\
   --exposure 5\
   --rotate_image true\
   --degrade_image true\
   --bidirectional_rotation true \
/


# Exposure: 0 - 10 scale (10 = black)

#------------------------
# Font Stuff
#------------------------
#--render_per_font false\
#--find_fonts true\
#--min_coverage  0\
#--list_available_fonts\
#------------------------

#  --xsize  Width of output image  (type:int default:3600)
#  --ysize  Height of output image  (type:int default:4800)
#  --max_pages  Maximum number of pages to output (0=unlimited)  (type:int default:0)
#  --only_extract_font_properties  Assumes that the input file contains a list of ngrams. Renders each ngram, extracts spacing properties and records them in output_base/[font_name].fontinfo file.  (type:bool default:false)
#  --unicharset_file  File with characters in the unicharset. If --render_ngrams is true and --unicharset_file is specified, ngrams with characters that are not in unicharset will be omitted  (type:string default:)
#  --fontconfig_tmpdir  Overrides fontconfig default temporary dir  (type:string default:/tmp)

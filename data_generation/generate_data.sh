#!/bin/bash
# Generate test images for tesseract using text2image.

PANGOCAIRO_BACKEND=fc \
text2image \
   --text  eng.training_text\
   --fonts_dir /Library/Fonts\
   --font 'Verdana' \
   --outputbase 'test_data'\
   --resolution  300\
   --rotate_image  true\
   --degrade_image true\
   --exposure 1000000\




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
#  --glyph_resized_size  Each glyph is square with this side length in pixels  (type:int default:0)
#  --glyph_num_border_pixels_to_pad  Final_size=glyph_resized_size+2*glyph_num_border_pixels_to_pad  (type:int default:0)
#  --tlog_level  Minimum logging level for tlog() output  (type:int default:0)
#  --char_spacing  Inter-character space in ems  (type:double default:0)
#  --underline_start_prob  Fraction of words to underline (value in [0,1])  (type:double default:0)
#  --underline_continuation_prob  Fraction of words to underline (value in [0,1])  (type:double default:0)
#  --bidirectional_rotation  Rotate the generated characters both ways.  (type:bool default:false)
#  --only_extract_font_properties  Assumes that the input file contains a list of ngrams. Renders each ngram, extracts spacing properties and records them in output_base/[font_name].fontinfo file.  (type:bool default:false)
#  --output_individual_glyph_images  If true also outputs individual character images  (type:bool default:false)
#  --unicharset_file  File with characters in the unicharset. If --render_ngrams is true and --unicharset_file is specified, ngrams with characters that are not in unicharset will be omitted  (type:string default:)
#  --fontconfig_tmpdir  Overrides fontconfig default temporary dir  (type:string default:/tmp)

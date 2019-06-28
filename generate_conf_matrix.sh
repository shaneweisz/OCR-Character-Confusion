# Run from char-seq-confusion folder

# Repeat this process n times to test the fonts with different text
n=3
for (( i = 1; i <= $n; i++ ))
do
    python3 char_data_generation/generate_random_chars.py # generate 5 000 random characters to a text file
    ./char_data_generation/generate_images.sh # convert the text file to tif files using text2image

    # Loop through the tif files, add noise and then save to a png
    for font_image in char_data_generation/font_images/*
    do
        python3 char_data_generation/add_image_noise.py $font_image
    done

    # Loop through the noisey png files, run ocr and then compare and update confusion matrix
    for font_image in char_data_generation/noisey_font_images/*
    do
        ./char_data_generation/run_ocr.sh $font_image char_data_generation/recognized_chars # run ocr
        pypy3 confusion_matrix/file_comparison.py # align truth and read
        python3 confusion_matrix/generate_confusion_matrix.py # calculate and update confusion matrix
    done

done

open confusion_matrix.xlsx -a "Microsoft Excel"

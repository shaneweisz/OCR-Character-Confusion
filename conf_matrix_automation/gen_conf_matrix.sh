# Run from conf_matrix_automation folder
python3 ../char_data_generation/random_chars.py
../char_data_generation/generate_data.sh

for font_image in ../char_data_generation/font_images/*
do
    python3 ../char_data_generation/add_image_noise.py $font_image
    ../char_data_generation/run_ocr.sh $font_image ../char_data_generation/recognized_chars
    pypy3 ../confusion_matrix/file_comparison.py
    python3 ../confusion_matrix/confusion_matrix.py
done

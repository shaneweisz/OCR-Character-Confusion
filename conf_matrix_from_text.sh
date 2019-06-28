# these commands place the supplied truth and read text files into the directories needed by our scripts
make clean # remove the current pickle

cp $t char_data_generation/random_chars.txt
cp $r char_data_generation/recognized_chars.txt

pypy3 confusion_matrix/file_comparison.py # align truth and read
python3 confusion_matrix/generate_confusion_matrix.py # calculate and update confusion matrix

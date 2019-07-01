# char-seq-confusion
Isazi Character Sequence Confusion 2019

-------------------------
## How to use if testing a different implementation of an OCR engine:

1) You must supply a text file (e.g. truth.txt) with the true text,
and a text file with the text recognized by the OCR engine
(e.g read.txt).

2) Place these text files in the char-seq-confusion folder (the same
directory as the Makefile) or specify the path to them in (3) below.

3) Run from the same directory as the Makefile:
    > make conf_matrix t=truth.txt r=read.txt

4) The calculated confusion matrix should be saved and open automatically.

--------------------------
## How to use the Weighted Levenshtein (using weights from our confusion matrix):

Run `python3 weighted_lev.py <word1> <word2>` from the root directory.


--------------------------
## How to generate new sample data and confusion matrix:
<em>(Note: this will overwrite the current confusion matrix)</em>

1) Remove the current pickle:
    > make clean

2) Generate new data and calculate the confusion matrix:
    > make


--------------------------
## Explanation of folders:

<ul>

<li> char_data_generation:  Creates text files with random characters that are converted to images
                            in various fonts, which then have noise added to them.
                            These images then have OCR performed on them.
                            The output is a random_chars.txt (the true characters)
                                     and recognized_chars.txt (the OCR'ed read characters). </li>

<li> confusion_matrix:  Creates a confusion matrix based on the data generated above.
                        Requires: random_chars.txt and recognized_chars.txt
                        Outputs: A confusion matrix excel spreadsheet. </li>

</ul>

---------------------------
## Relevant Literature:

https://jlcl.org/content/2-allissues/1-heft1-2018/jlcl_2018-1_3.pdf
("supervised post-correction on character level will be more
beneficial than on word level due to data sparsity issues.")

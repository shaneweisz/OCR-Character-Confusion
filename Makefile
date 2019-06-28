default:
	./generate_conf_matrix.sh

# We recommend placing e.g. truth.txt and read.txt in the same directory as the Makefile
# Otherwise, supply the path to the files instead.
conf_matrix: # EXAMPLE USAGE make conf_matrix t=truth.txt r=read.txt
	./conf_matrix_from_text.sh $t $r

clean:
	rm confusion_matrix/confusion_matrix.pkl

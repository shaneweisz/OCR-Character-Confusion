default:
	./generate_conf_matrix.sh

conf_matrix: # EXAMPLE USAGE make confusion_matrix t=truth.txt r=read.txt
	./conf_matrix_from_text.sh $t $r

clean:
	rm confusion_matrix/confusion_matrix.pkl

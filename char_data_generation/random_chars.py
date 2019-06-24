from random import randint

def rand_chars(n,m):
    rv = ""
    for i in range(1, n + 1):
        rv += chr(randint(33,126)) + " "
        if i%m == 0:
            rv +="\n"
    return rv

def write_to_file(text, file_name="random_chars.txt"):
    f = open(file_name,'w')
    f.write(text)
    f.flush()
    f.close()


def main():
    write_to_file(rand_chars(10000,50))


if __name__ == "__main__":
    main()

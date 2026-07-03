def split_and_join(line):
    # write your code here
    split_word = line.split(" ")
    join_word = "-".join(split_word)
    return join_word
if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)

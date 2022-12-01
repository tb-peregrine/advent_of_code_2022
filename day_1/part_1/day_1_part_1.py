import sys

def read_input(input_file):
    with open(input_file) as f:
        return f.readlines()


def total_cals_array(lines):
    sums = []
    tmp_sum = 0
    for l in lines:
        if l != '\n':
            tmp_sum = tmp_sum + int(l.split('\n')[0])
        else:
            sums.append(tmp_sum)
            tmp_sum = 0
    return sums


def main(input_file):
    lines = read_input(input_file)
    sums = total_cals_array(lines)
    print(max(sums))

if __name__ == '__main__':
    try:
        input_file = sys.argv[1]
        main(input_file)
    except Exception as e:
        print("Please provide an input .txt file")

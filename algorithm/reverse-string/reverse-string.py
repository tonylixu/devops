def reverse_str(string):
    string_list = string.split(' ')
    rt = ''
    for i in string_list:
        rt += (i[::-1] + ' ')
    print "|"+rt.strip()+"|"

if __name__ == "__main__":
    str_orig = "Let's take LeetCode contest"
    reverse_str(str_orig)

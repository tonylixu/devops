def reverse_str(string):
    string_list = string.split(' ')
    # i = 0
    #while i < len(string_list):
    #    string_list[i] = string_list[i][::-1]
    #    i += 1
    #print ' '.join(string_list)
    rt = ''
    for i in string_list:
        rt += (i[::-1] + ' ')
    print "|"+rt.strip()+"|"

if __name__ == "__main__":
    str_orig = "Let's take LeetCode contest"
    reverse_str(str_orig)

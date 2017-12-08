 def self_dividing_numbers(self, left, right):
    """
    :type left: int
    :type right: int
    :rtype: List[int]
    """
    list = []
    for i in range(left, right+1):
        str_i = str(i)
        if i < 10:
            list.append(i)
        elif '0' in str_i:
            continue
        else:
            length = len(str_i)
            moduable = True
            for k in range(length):
                if i % int(str_i[k]) != 0:
                    moduable = False
                    break
            if moduable:
                list.append(i)
    return list

if __name__ == '__main__':
    left = 1
    right = 22
    print self_dividing_number(left, right)

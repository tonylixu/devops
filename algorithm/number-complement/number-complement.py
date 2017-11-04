def findComplement(num):
    """
    :type num: int
    :rtype: int
    """
    # Conver number into binary string
    num_str = format(num,'b')
    # List to hold individual bits
    num_list = []
    for i in num_str:
        # Calculate the reverse
        val = (int(i)+1)%2
        num_list.append(str(val))
    print int(''.join(num_list),2)

if __name__ == "__main__":
    number = 5
    findComplement(5)
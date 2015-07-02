def palindrome():
	string=raw_input("enter a string")
    return string == string[-1::-1]
    # result = True
    # str_len = len(string)
    # for i in range(0, int(str_len/2)):
    #     if string[i] == string[str_len-i-1]:
    #         result = True 
    #     else
    #     	break
    # return result
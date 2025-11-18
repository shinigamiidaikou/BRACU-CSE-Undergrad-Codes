def bin_to_dec(string,i,num):
	if len(string) == i :
		return num
	else:
		if string[i] == '0':
			num=2*num
		else:
			num=2*num+1
	return bin_to_dec(string,i+1,num)

print(bin_to_dec())

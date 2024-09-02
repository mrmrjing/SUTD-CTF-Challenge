# first stage
def stage_1_encrypt(string):
    matrix = [[],[]]
    for i in range(len(string)):
        if i%2 == 0:
            matrix[0].append(string[i])
        else:
            matrix[1].append(string[i])
    return "".join(matrix[0]) + "".join(matrix[1])

def stage_1_decrypt(string):
    n = len(string)
    output = ""
    mid = (n//2)+1
    row1 = string[:mid]
    row2 = string[mid:]
    for i in range(len(row2)):
        output += row1[i]+row2[i]
    output += row1[i+1]
    return output



print(stage_1_decrypt(stage_1_encrypt("https://ctf51.wordpress.com")))
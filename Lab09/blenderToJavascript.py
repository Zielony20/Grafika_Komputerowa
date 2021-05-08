input = open("wiocha.obj","rt")
output =  open("kodzik.txt","wt")

first_line = input.readline()
l1,l2,l3 = (1,1,1);
for last_line in input:
    if( last_line[0]=='v' and last_line[1]==' ' ):

        l1 = last_line[2:].find(' ')+2
        l2 = last_line[l1+1:].find(' ')+l1+1
       

        temp = "vertexPosition.push(...["+ last_line[ 2 :  l1]     +", "+ last_line[ l1 : l2 ]  +", "+ last_line[ l2 :len(last_line)-1 ]  + "]);\n"
        output.write(temp)  
    elif(last_line[0]=='f' and last_line[1]==' '):
        l1_end = last_line[2:].find('/')+2        

        l2_begin = last_line[l1_end:].find(' ')+l1_end
        l2_end = last_line[l2_begin:].find('/')+l2_begin

        l3_begin = last_line[l2_end:].find(' ')+l2_end
        l3_end = last_line[l3_begin:].find('/')+l3_begin        
        
        temp = "indexes.push(...["+last_line[2:l1_end]+", "+last_line[l2_begin:l2_end]+", "+  last_line[l3_begin:l3_end]  +"]);\n"
        output.write(temp)
input.close()
output.close()

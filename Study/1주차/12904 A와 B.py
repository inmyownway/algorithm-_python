
before =input()
after=input()

while True:
    if after[-1] == 'A':
        after= after[0:len(after)-1]
    elif after[-1] =='B':
        after= after[0:len(after)-1]
        after = after[::-1]

    if(after==before):
        print(1)
        break;
    elif(len(before) > len(after)):
        print(0)
        break;






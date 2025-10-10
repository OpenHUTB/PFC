print('你穿越到了二进制的世界，现在你眼前有一扇门\n这扇门上写着\'第4道门\'')
print('''tip:当看到文段尾部有\'&\'时需要按任意键以继续&''')
continue_0 = input()
print('你需要输入\'∮∝∂∇∏∑√\'以继续')

chance_dooropen = 3
while True:
    start = input()
    if start == "∮∝∂∇∏∑√":
        print('你复制并输入了以上文本，但什么事情都没发生')
        
    else:
        chance_dooropen = chance_dooropen - 1
        if chance_dooropen == 0:
            print('你已经没有机会了，现在门爆炸了！&')
            continue_1 = True
            continue_0 = input()
            break
        else:
            print('你输入错了!再输错',chance_dooropen,'次门就会爆炸！')
    
if continue_1 == True:
    print('所以门开了&')
    continue_0 = input()
    print('''接下来，你可以
1，往前走
2，向后看''')

    while True:
    
        choice_1 = input()
        if choice_1 == '1':
            print('你向前走，发现了另一扇门')
            break
        elif choice_1 == '2':
            print('后面是望不到边的走廊&')
            input()
        else:
            print('输错啦&')
            input()
            print('''接下来，你可以
1，往前走
2，向后看,但这是修改后的''')
        
#只是刚开始学python的测试
    

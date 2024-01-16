count=0
count1=0
for i in ['м','у','ж','ч','и', 'н','а']:
    for r in ['м','у','ж','ч','и', 'н','а']:
        for t in ['м','у','ж','ч','и', 'н','а']:
            for y in ['м','у','ж','ч','и', 'н','а']:
                for u in ['м','у','ж','ч','и', 'н','а']:
                    for g in ['м','у','ж','ч','и', 'н','а']:
                        line=i+r+t+y+u+g
                        if (line.count("м")<=1 and line.count("у")<=1 and line.count("ж")==1 and line.count("ч")<=1
                                and line.count("и")<=1 and line.count("н")<=1 and line.count("а")<=1 and line[0]!="ч"):
                            print (i+r+t+y+u+g)
                            count+=1
                            if count%2==1:
                                count1+=1
print(count1)

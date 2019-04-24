"""
1.中括号代表其中的内容是可选的，比如“歌[曲]”，能匹配“歌”和“歌曲”；

2.尖括号代表其中的内容是必选的，比如“<播>放”，能匹配“播放”；

3.括号是可以嵌套的；

4.竖线代表“或”的关系，即竖线分隔的内容是可替换的，比如“<播放|来首>歌曲”,能匹配“播放歌曲”和“来首歌曲”,再如“[播放|来首]歌曲”,能匹配”播放歌曲“，”来首歌曲“和”歌曲“（因为中括号里面是可选的，所以可以匹配”歌曲“）；

5.竖线在其所属的括号内，优先级大于括号中的其他括号，比如” <[播]放|来>首歌曲”，能匹配“播放首歌曲“，“放首歌曲“和”来首歌曲“；

6.竖线可以脱离括号独立存在，比如”在哪里|哪里有”，可以匹配“在哪里”和“哪里有”;

 

那么，给一个上述的语义模板表达式和用户的query，你能判断用户的query是否能匹配这个表达式吗？
"""

template = "<[播]放|来>[一|几]<首|曲|个>@{singer}的<歌[曲]|[流行]音乐>"

# template = raw_input()
# query = raw_input()

stack = []

for i in range(len(template)):
    word = ""
    if template[i] == '<':
        stack.append(word)
    elif template[i] == '>':
        stack.append(word)
    else:
        stack[-1] += template[i]

print(stack)
stack = stack[:-1]

for i in range(len(stack)):
    words = stack[i]
    words = words.split("|")
    for j in range(len(words)):
        word = words[i]
        for k in range(len(word)):
            
    stack[i] = word

print(stack)
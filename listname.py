s1 = ['张一华,男,40', '王二菲,女,100', '张飞,男,56', '李四,男,69']
s2 = []
for i in s1:
    s3 = i.split(',')
    if s3[1] == '男':
        s2.append(s3[0])
print(s2)

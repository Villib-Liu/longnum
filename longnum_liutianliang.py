# -*- coding: utf-8 -*-

def long_num_sum(lnm1,lnm2):

    maxnum = max(lnm1, lnm2)
    minnum = min(lnm1, lnm2)
    len1 = len(minnum)
    len2 = len(maxnum)
    ans = [0 for x in range(len2)]
    ans[-len1:] = minnum
    # print(ans)

    for i in range(1,len2 + 1):
        i = -i
        temp = ans[i] + maxnum[i]
        if temp >= 10:
            temp = temp - 10
            ans[i] = temp
            print ans
            if i == -len1:
                ans.insert(0,1)
            else:
                ans[i-1] = ans[i-1] + 1
        else:
            ans[i] = temp
        print(ans)


def long_num_multi(n1,n2):

    n1.reverse()
    n2.reverse()
    n3=[]
    # print n1,n2
    for i0 in xrange(len(n1)+len(n2)):
        n3.append(0)
    for i1 in xrange(len(n1)):
        for i2 in xrange(len(n2)):
            n3[i1+i2] += n1[i1]*n2[i2]
    for i3 in xrange(len(n3)):
        if(n3[i3]>9):
            n3[i3+1] += n3[i3]/10
            n3[i3] = n3[i3]%10
    n3.reverse()
    print(n3)


# 测试
if __name__ == '__main__':

    array1 = [9,9,9,9,9,9]
    array2 = [9,9,9]
    long_num_sum(array1,array2)
    long_num_multi(array1,array2)
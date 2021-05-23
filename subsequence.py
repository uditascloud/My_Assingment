def find_LIS_count(final):
    length=len(final)
    if(length==0):
        return 0
    dp=[1]*length
    for i in range(1,length):
        for j in range(0,i):
            if(final[i]>final[j]):
                if(dp[i]<=dp[j]):
                    dp[i]=dp[j]+1;
    return max(dp)


def make_array(first,second):
    new_list=[]
    ordered_map={}
    for i in first:
        ordered_map[i]=1
    for i in second:
        if i in ordered_map:
            new_list.append(i)

    return new_list


first_list=list(map(int,input().split()))
second_list=list(map(int,input().split()))
final_list=[]
final_list=make_array(first_list,second_list)
count=find_LIS_count(final_list)
print(count)

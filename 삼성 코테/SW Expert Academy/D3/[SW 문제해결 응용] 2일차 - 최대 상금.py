# T = int(input())
#         # 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
# for test_case in range(1, T + 1):
    # num, change = map(int, input().split())
    # num_list = list(map(int, str(num)))
    #     print(num_list)
    #         for i in range(change):
    #             temp_list = []
    #             temp_list = num_list(reversed=True)
    #
    #             change_indx = temp_list[i:].index(max(temp_list[i:0]))
    #
    #             temp1 = num_list[i]
    #             temp2 = num_list[len(num_list) - 1 - change_indx]
    #
    #     #print(temp1,temp2)
    #
    #     num_list[i]=temp2
    #     num_list[len(num_list)-1-change_indx]= temp1
    # print(num_list)

T = int(input())
for test_case in range(1, T + 1):
    num, change = map(int, input().split())
    num_list = list(map(int, str(num)))


    # 3 2 8 8 8
    # 8 2 8 8 3
    #
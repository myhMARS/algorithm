import time
import random
import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')


# 冒泡排序算法
def bubble_sort(items):
    logging.info('冒泡算法')
    for i in range(len(items)-1):
        for j in range(len(items)-1, i, -1):
            if items[j] < items[j-1]:  # 后数小于前数
                items[j], items[j-1] = items[j-1], items[j]  # j-1位置与j交换
                # logging.info('发生交换:' + str(items))
    check_sort(items, '原算法')


'''冒泡排序算法实际有很多种写法，核心原理为比较相邻两数大小然后进行交换将大数或小数向列表两侧推移，上面的示例程序为将从列表末位将比较的两个数的小的数向
列表首推移，例如列表[3,2,1]变化如下[3,2,1]->[3,1,2]->[1,3,2]->[1,2,3]，将列表看作垂直堆放的一列数据从最下面的一个元素起将较小的元素换到上面，
未经优化的冒泡算法排序次数最多为n-1次,比较次数为n(n-1)/2
演示视频:www.bilibili.com/video/BV1qY4y1h7Lz
(字符串比较ascii码值且只比较字符串首字符如果相同则比较下一字符且大小与长度无关,小写字母>大写字母>数字（数字为字符串格式））'''


# 进阶1:冒泡算法的优化方案
def optimization_bubble_sort_1(items):
    logging.info('优化1')
    for i in range(len(items)-1):
        flag = False
        for j in range(len(items)-1, i, -1):
            if items[j] < items[j-1]:  # 后数小于前数
                items[j], items[j-1] = items[j-1], items[j]  # j-1位置与j交换
                flag = True  # 发生交换
                logging.info('发生交换:' + str(items))
        if not flag:  # 未发生交换时执行
            break
    check_sort(items, '优化1')


'''优化方案一:由于冒泡算法每次遍历列表时如果列表无序则必定有位置交换，若无位置交换则列表已有序，由此可推得此优化方案。定义一个flag标记完成一次遍历后是
否发生交换,若未发生交换则使用break方法结束排序'''


# 进阶2:优化进阶(搅拌排序)
#  ∧＿∧
#  （｡･ω･｡)つ━☆・*。
#  ⊂　　 ノ 　　　・゜+.
# 　しーＪ　　　°。+ *´¨)
# 　　　 　　.· ´¸.·*´¨) ¸.·*¨)
# 　　　　　　　 　(¸.·´ (¸.·’*
def optimization_bubble_sort_2(items):
    logging.info('优化2')
    for i in range(len(items) - 1):
        flag = False
        for j in range(len(items) - 1 - i):  # 先进行正向排序将大数向列表末尾推移
            if items[j] > items[j + 1]:
                items[j], items[j + 1] = items[j + 1], items[j]
                logging.info('发生交换:' + str(items))
                flag = True
        if flag:  # 反向排序将小数向列表前端推移
            flag = False
            for j in range(len(items) - 2 - i, 0, -1):
                if items[j - 1] > items[j]:
                    items[j], items[j - 1] = items[j - 1], items[j]
                    logging.info('发生交换:' + str(items))
                    flag = True
            i += 1
        if not flag:
            break
    check_sort(items, '优化2')


'''搅拌排序也叫鸡尾酒排序，原理并不复杂，与优化方案2相同采用了flag表示已经有序，增加了反向排序段，对于大部分列表可节约时间
简单举例:列表=[1,5,4,3,2]
优化前(bubble_sort):[1,5,4,3,2]->[1,5,4,2,3]->[1,5,2,3,4]->[1,2,3,4,5]
优化后:[1,5,4,3,2]->[1,2,4,3,5]->[1,2,3,4,5]'''


def check_sort(items, function):
    i = 0
    for i in range(len(items)-1):
        if items[i] <= items[i+1]:
            continue
        else:
            print(function + '未有序')
            break
    if i == len(items)-2:
        print(function + '列表有序')


def run_time(function, name, list_sort):  # 测试指定函数运行时间
    time_start = time.perf_counter()
    function(list_sort)
    time_end = time.perf_counter()
    sum_time = time_end - time_start
    print(name + '运行时间:' + str(sum_time))


def random_list(length_list):  # 随机生成一个长度为length的列表
    list_rnd = random.sample([i for i in range(0, length_list)], length_list)
    return list_rnd


if __name__ == '__main__':
    sample_list = [3, 5, 6, 9, 7, 1, 2, 4, 8, 10]
    run_time(bubble_sort, '冒泡算法', sample_list)
    run_time(optimization_bubble_sort_1, '冒泡算法优化1', sample_list)
    run_time(optimization_bubble_sort_2, '冒泡算法优化2', sample_list)
    logging.disable(logging.INFO)
    length = 30000  # 实验数据长度
    list_long = random_list(length)
    print('大型(其实还是很小)列表实验：表格长度：' + str(length))
    run_time(bubble_sort, '原算法', list_long)
    run_time(optimization_bubble_sort_1, '优化1', list_long)
    run_time(optimization_bubble_sort_2, '优化2', list_long)

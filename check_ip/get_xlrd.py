# -*- ! coding=utf-8 -*-
from get_ip import get_ip
import xlrd,time
def get_xird():
    excel = xlrd.open_workbook('testcase.xlsx')
    sheet = excel.sheet_by_name('Sheet1')
    nums = sheet.nrows # 读取的文件的总的行数
    # print nums
    # f = open('log_s%.txt'%(time.strftime('%Y-%m-%d-%H-%M-%S',time.localtime(time.time()))),'a')
    f = open('log_%s.txt'%(time.strftime('%Y-%m-%d-%H-%M-%S',time.localtime(time.time()))),'a')
    f.write('TEST-STRT'.center(20,'*')+'\n')
    f.write('开始时间:%s\n'%time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    m = 0 # 通过的用例数
    n = 0 # 读取的用例数
    for i in range(1,nums):

        #f.write('TEST:%s, '%i)
        switch = (sheet.cell(i,0).value).encode('utf-8')
        yongli = (sheet.cell(i,1).value).encode('utf-8')
        ip = (sheet.cell(i,2).value).encode('utf-8')
        if switch == 'open':
            n = n + 1
            reponse = get_ip(ip)
            f.write('TEST:%s,  ''test_ip:%s, ''test_main:%s,  '%(i,ip,yongli))
            if reponse['code'] == 0:
                m = m + 1
                f.write('test_result:true 测试通过\n')
            else:
                f.write('test_result:False\n')
        '''
        else:
            f.write('TEST:%s, '%i)
            f.write(switch+'\n')
        '''
    s = nums-1
    f.write('总的用例数:%d\n''通过的用例数:%d\n''失败的用例数:%d\n''跳过的用例数:%d\n'%(s,m,n-m,s-n))
    f.write('结束时间:%s\n'%time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    f.write('TEST-END'.center(20,'*')+'\n')
    f.close()
time.sleep(3)
print '测试结束'




get_xird()


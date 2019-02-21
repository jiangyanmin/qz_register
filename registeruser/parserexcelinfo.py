#!/usr/bin/env python3
# -*- encoding:utf-8 -*-
# @Author:JiangM
# @Date:2018/9/12
# from registeruser.sqlutils import SqlDBUtil
# from registeruser.sqlcmdtextstore import SqlCmdTextStore
# from ddt import ddt, data, unpack
# from registeruser.registerinfo import RegisterInfo
# import re
# from registeruser.sqlutils import read_data_from_db
import xlrd
import xlrd.biffh


def parser_excel_info(excel_path, sheet_name, field_name_index, test_data_start_nrow, test_data_end_nrow=None):
    try:
        test_data_work_book = xlrd.open_workbook(excel_path)
    except Exception as e:
        print('无法打开excel文件，路径：%s，错误信息：%s' % (excel_path, e))
        raise IOError('Can not open excel,error message:%s' % e)
    if test_data_work_book is not None:
        try:
            test_data_sheet = test_data_work_book.sheet_by_name(sheet_name)
        except xlrd.biffh.XLRDError as e:
            print('Can not open sheet:%s,error message:%s' % (sheet_name, e))

    if test_data_sheet.nrows <= 0:
        raise Exception('未在工作表找到数据！')
    else:
        test_data_list = []
        total_col_of_testcase = len(test_data_sheet.row(field_name_index))  # 返回第6行的单元格对象序列的长度，即总列数
        if test_data_end_nrow is None:
            total_row_of_testcase = test_data_sheet.nrows  # 返回测试用例总行数
        else:
            total_row_of_testcase = test_data_end_nrow
        for r in range(test_data_start_nrow, total_row_of_testcase):
            every_row_test_data_list = []
            for n in range(total_col_of_testcase):
                cell_data_of_testcase = test_data_sheet.cell_value(r, n)  # 返回测试用例每一个单元格的值
                every_row_test_data_list.append(cell_data_of_testcase)
            # print(every_row_test_data_list)
            # print('========================')
            test_data_list.append(every_row_test_data_list)
        # print(test_data_list)
    return test_data_list


# if __name__ == '__main__':
#     parser_excel_info('registertestcase.xlsx', 'Register', 5, 6)
#









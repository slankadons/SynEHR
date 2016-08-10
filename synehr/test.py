import unittest
import numpy as np
import pandas as pd
import datetime

from synehr import syn_ehr
from errors import gender_misclassification, char_sub_str, char_omission, char_sub_date, char_transpo_str, char_transpo_date, char_insertion_str


# class Testsynehrpackage(unittest.TestCase):
    # def test_add(self):
    #     pass
    #     res=constrained_sum_sample_pos(5,1)
    #     self.assertEqual(sum(res),1)
    # def test_input_synehr(self):
    #     with self.assertRaises(SizeValueError):
    #         syn_ehr(size=20)



class TestErrors(unittest.TestCase):

    def test_gen_errors(self):
        pass

    def test_gender_misclassification(self):
        data = pd.DataFrame({'gender': ["M","M","F","F"]})
        res = gender_misclassification(data)
        data_result = pd.DataFrame({'gender': ["F","F","M","M"]})
        self.assertTrue(data_result.equals(res))

    def test_char_sub_str(self):
        string_test = ["Gaurika", "Shraddha", "Tennyson"]
        res = char_sub_str(string_test)
        for i in range(len(string_test)):
            # print string_test[i]
            # print res[i]
            self.assertFalse(string_test[i] is res[i])

    def test_char_omission(self):
        string_test = ["Gaurika", "Shraddha", "Tennyson"]
        res = char_omission(string_test)
        for i in range(len(string_test)):
            # print string_test[i]
            # print res[i]
            self.assertFalse(string_test[i] is res[i])

    def test_char_sub_date(self):
        date_test = [datetime.datetime.strptime("2010/2/10", "%Y/%m/%d"), datetime.datetime.strptime("2010/5/3", "%Y/%m/%d")]
        res = char_sub_date(date_test)
        for i in range(len(date_test)):
            # print date_test[i]
            # print res[i]
            self.assertFalse(date_test[i] is res[i])

    def test_char_transpo_str(self):
        string_test = ["Gaurika", "Shraddha", "Tennyson"]
        res = char_transpo_str(string_test)
        for i in range(len(string_test)):
            # print string_test[i]
            # print res[i]
            self.assertFalse(string_test[i] is res[i])

    def test_char_transpo_date(self):
        date_test = [datetime.datetime.strptime("2010/2/10", "%Y/%m/%d"), datetime.datetime.strptime("2010/5/3", "%Y/%m/%d")]
        res = char_transpo_date(date_test)
        for i in range(len(date_test)):
            # print date_test[i]
            # print res[i]
            self.assertFalse(date_test[i] is res[i])

    def test_char_insertion_str(self):
        string_test = ["gaurika", "shraddha", "tennyson"]
        res = char_insertion_str(string_test)
        for i in range(len(string_test)):
            # print string_test[i]
            # print res[i]
            self.assertFalse(string_test[i] is res[i])




if __name__=='__main__':
    unittest.main(verbosity=30)
import json
import logging as logger
import multiprocessing as mp
import os
import time
from datetime import datetime

now = time.time()

logger.basicConfig(format='%(asctime)s : %(levelname)-2s : %(message)s',
                   filename=r"../log/logging.txt",
                   level=logger.INFO,
                   datefmt='%Y-%m-%d %H:%M:%S')


class Solution:
    def __init__(self, nums, n):
        self.nums = nums
        self.n = n
        
    def multiply_data(self):
        start = datetime.now()
        num_list = []
        for num in self.nums:

            if int(num.replace("\n","")) == 100:
                logger.info("{} * {} = {}".format(num.replace("\n",""), str(self.n), int(num) * self.n))
            num_list.append({int(num): int(num) * self.n})
        mul_file = open("output/multiply_data.json", 'a')
        mul_file.truncate(0)
        mul_file.write(json.dumps(num_list))
        mul_file.close()
        logger.info("Time taken for Multiplication Process : {}".format(datetime.now() - start))

    
    def add_data(self):
        start = datetime.now()
        add_list = []
        for i in range(len(self.nums)):
            try:
                val = int(self.nums[i]) + int(self.nums[i+1])
                add_list.append(val)
                if i == 99:
                    logger.info("Sum = {}".format(val))
            except IndexError as e :
                pass
        add_file = open("output/add_data.txt", 'a')
        add_file.truncate(0)
        add_file.write(json.dumps(add_list))
    
        add_file.close()
        logger.info("Time taken for Addition Process : {}".format(datetime.now() - start))





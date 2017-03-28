#!/usr/bin/python3
# -*- coding: utf-8 -*-


import os
import sys
import math

import array

import statistics

from matplotlib import rc
rc('font', family='Droid Sans', weight='normal', size=14)

import matplotlib.pyplot as plt


class WikiGraph:

    def load_from_file(self, filename):
        print('Загружаю граф из файла: ' + filename )

        with open(filename) as f:
            (n, _nlinks) = map(int,f.readline().split())
            
            self._titles = []
            self._sizes = array.array('L', [0]*n)
            self._redirect = array.array('B', [0]*n)
            self._links = array.array('L', [0]*_nlinks)

            self._offset = array.array('L', [0]*(n+1))
            self._k = []
            # TODO: прочитать граф из файла
            for i in range (n):
                  self._titles.append(f.readline())
                  (self._sizes,self._redirect,self._k) = map(int,f.readline().split())
                  for j in range (self._k):
                       self._links.append(f.readline())

                       if i == 0:
                           self._offset[i]=0
                       else:
                           self._offset[i] = self._offset[i-1] + self._k[i]

        print('Граф загружен')

    def get_number_of_links_from(self, _id):
        return self._k[_id]

    def get_links_from(self, _id):
        return self._links[ self._offset[_id]: self._offset[_id+1]]

    def get_id(self, title):
        for _id in range (n) :
            if title ==  self._titles[_id]:
                return _id

    def get_number_of_pages(self):
        return n

    def is_redirect(self, _id):
        if self._redirect[_id] == 0:
            return False
        if self._redirect[_id] == 1:
            return True

    def get_title(self, _id):
        return self._titles[_id]

    def get_page_size(self, _id):
        return self._sizes[_id]


def hist(fname, data, bins, xlabel, ylabel, title, facecolor='green', alpha=0.5, transparent=True, **kwargs):
    plt.clf()
    # TODO: нарисовать гистограмму и сохранить в файл


if __name__ == '__main__':

    if len(sys.argv) != 2:
        print('Использование: wiki_stats.py <файл с графом статей>')
        sys.exit(-1)

    if os.path.isfile(sys.argv[1]):
        wg = WikiGraph()
        wg.load_from_file(sys.argv[1])
    else:
        print('Файл с графом не найден')
        sys.exit(-1)

    # TODO: статистика и гистограммы
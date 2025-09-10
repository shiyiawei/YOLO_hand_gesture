# -*- coding: utf-8 -*-

__version__ = '1.0'
__author__ = 'sxy'
__email__ = '1078107814@qq.com'
__url__ = 'https://github.com/shiyiawei'

AUTHOR_INFO = ("基于YOLOv8/v5的手势识别系统v1.0\n"
               "作者：宋轩逸\n"
               "GitHub: https://github.com/shiyiawei\n\n"
               "杭电圣光机联合学院2020级本科毕设作品")

ENV_CONFIG = ("[配置环境]\n"
              "(1)使用anaconda新建python3.10环境:\n"
              "conda create -n env_rec python=3.10\n"
              "(2)激活创建的环境:\n"
              "conda activate env_rec\n"
              "(3)使用pip安装所需的依赖，可通过requirements.txt:\n"
              "pip install -r requirements.txt\n")

with open('./环境配置.txt', 'w', encoding='utf-8') as f:
    f.writelines(ENV_CONFIG + "\n\n" + AUTHOR_INFO)

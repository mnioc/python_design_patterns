# !/usr/bin/env python 
# -*- coding: utf-8 -*-

# ------------------#
# 适配器模式: 是一种结构型设计模式， 它能使接口不兼容的对象能够相互合作。
# ------------------#

"""
适配器设计模式是懒得改动某些代码，或者某些接口不方便改动的时候
使用一个特定的封装，一些特定的编写办法，使不同的接口可以使用同种调用方式使用。
"""

class HuaweiCloud:

    def upload(self):
        print("使用华为云接口上传文件...")


class AliCloud:

    def upload(self):
        print("使用阿里云接口上传文件...")


# 需要进行适配，因为他实现的上传接口是tencent_upload，跟上传的两个类不一样。
class TencentCloud:

    def tencent_upload(self):
        print("使用腾讯云接口上传文件...")


class Application:

    def run(self, cloud_type):
        if cloud_type == "huawei":
            HuaweiCloud().upload()

        if cloud_type == "ali":
            AliCloud().upload()
        
        if cloud_type == "tencent":
            TencentCloud().tencent_upload()


# ---------------------------------------------------------------------------------------------
# NO NO NO !! 代码不美观，都是实现上传功能，但是调用的接口千奇百怪。。需要适配

class AdapterCloud:

    def __init__(self, cloud):
        self.cloud = cloud

    def upload(self) -> None:
        self.cloud().tencent_upload()


if __name__ == "__main__":
    HuaweiCloud().upload()
    AliCloud().upload()
    AdapterCloud(TencentCloud).upload()
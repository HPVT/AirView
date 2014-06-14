#!/usr/bin/env python
# -*- coding: cp936 -*-
# Copyright (c) 2014 The AirView Authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

import sys
import os
import shutil

def cur_file_dir():
        #��ȡ�ű�·��
        path = sys.path[0]
        #�ж�Ϊ�ű��ļ�����py2exe�������ļ�������ǽű��ļ����򷵻ص��ǽű���Ŀ¼�������py2exe�������ļ����򷵻ص��Ǳ������ļ�·��
        if os.path.isdir(path):
                 return path
        elif os.path.isfile(path):
                 return os.path.dirname(path)

#����ļ�·���Ƿ����
def check_file_path(chromium_src_path,mirror_path,backup_path):
        # check path
         if False  == os.path.exists(chromium_src_path):
                print chromium_src_path + ' don t exist'
         if False  == os.path.exists(mirror_path):
                print mirror_path + ' don t exist'
         if False  == os.path.exists(backup_path):
                print backup_path + ' don t exist! create it!'
                os.makedirs(backup_path)

def combine_path(path1,path2):
         #[TODO](lidabing):ʹ��os.path.join(src_file,mirror_file[mirror_path_len:]) ���ɵ�·�����ԣ���֪��Ϊʲô��
         return path1 + path2;

# ����ԭʼ�����е��ļ�
# src_path:chromiumԴ��·����mirror_path AirView Դ��λ�ã�dest_path�����ļ�·��
def backup_src_code(chromium_src_path,mirror_path,backup_path,topdown=True):
         print "===start backup_src_code==="
         check_file_path(chromium_src_path,mirror_path,backup_path)
         mirror_path_len = len(mirror_path)
         for root, dirs, files in os.walk(mirror_path, topdown):
                for name in files:
                  mirror_file = os.path.join(root,name)
                  chromium_src_file = combine_path(chromium_src_path,mirror_file[mirror_path_len:])
                  backup_file = backup_path + mirror_file[mirror_path_len:]
                  if False  == os.path.exists(backup_file):
		      if True  == os.path.exists(chromium_src_file):
                         shutil.copyfile(chromium_src_file,backup_file)
                         print "COPY FILE:"+chromium_src_file+' ---> '+backup_file
                for name in dirs:
                  mirror_dir = os.path.join(root,name)
                  chromium_src_dir = combine_path(chromium_src_path,mirror_dir[mirror_path_len:])
                  backup_dir= backup_path + mirror_dir[mirror_path_len:]
                  if False  == os.path.exists(backup_dir):
                        os.makedirs(backup_dir)
                        print "CREATE DIR:"+backup_dir
         print "===done backup_src_code==="

# ͬ��mirror_path ���룬��chromium������
def update_mirror_to_chromium_src(chromium_src_path,mirror_path,backup_path,topdown=True):
         print "===sync_mirror_to_chromium_src==="
         check_file_path(chromium_src_path,mirror_path,backup_path)
         mirror_path_len = len(mirror_path)
         for root, dirs, files in os.walk(mirror_path, topdown):
                for name in files:
                  mirror_file = os.path.join(root,name)
                  chromium_src_file = combine_path(chromium_src_path,mirror_file[mirror_path_len:])
                  shutil.copyfile(mirror_file,chromium_src_file)
                  print "COPY FILE:"+mirror_file+' ---> '+chromium_src_file
                for name in dirs:
                  mirror_dir = os.path.join(root,name)
                  chromium_src_dir = combine_path(chromium_src_path,mirror_dir[mirror_path_len:])
                  if False  == os.path.exists(chromium_src_dir):
                        os.makedirs(chromium_src_dir)
                        print "CREATE DIR:"+chromium_src_dir
         print "===done sync_mirror_to_chromium_src==="

# �ύchromium���޸ĵĲ��ִ����mirror����
def commit_chromium_code_to_mirror(chromium_src_path,mirror_path,backup_path,topdown=True):
         print "===start revert_chromium_code_from_backup==="
         check_file_path(chromium_src_path,mirror_path,backup_path)
         mirror_path_len = len(mirror_path)
         for root, dirs, files in os.walk(mirror_path, topdown):
             for name in files:
                 mirror_file = os.path.join(root,name)
                 chromium_src_file = combine_path(chromium_src_path,mirror_file[mirror_path_len:])
                 if os.path.exists(chromium_src_file):
                    backup_file = backup_path + mirror_file[mirror_path_len:]
                    shutil.copyfile(chromium_src_file,mirror_file)
                    print "COPY FILE:"+chromium_src_file + ' ---> '+ mirror_file
                 else:
                   print chromium_src_file + 'not exist';
         print "===done revert_chromium_code_from_backup==="


def main(argv):
     chromium_src_path = cur_file_dir()
     chromium_src_path = os.path.dirname(chromium_src_path)
     chromium_src_path = os.path.dirname(chromium_src_path)
     chromium_src_path=chromium_src_path + "\\chromium\\src"

     backup_path = cur_file_dir()
     backup_path = os.path.dirname(backup_path)
     backup_path = os.path.dirname(backup_path)
     backup_path=backup_path + "\\chromium_backup\\src"

     mirror_path = cur_file_dir()
     mirror_path = os.path.dirname(mirror_path)
     mirror_path=mirror_path + "\\src"

     print argv[1]

     if 'backup'==argv[1]:
            backup_src_code(chromium_src_path,mirror_path,backup_path)
            
     if 'update'==argv[1]:
            update_mirror_to_chromium_src(chromium_src_path,mirror_path,backup_path)
            
     if 'commit'==argv[1]:
            commit_chromium_code_to_mirror(chromium_src_path,mirror_path,backup_path)

if __name__ == '__main__':
  sys.exit(main(sys.argv))

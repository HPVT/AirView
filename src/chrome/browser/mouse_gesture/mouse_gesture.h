// Copyright (c) 2014 The AirView Authors. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

#ifndef AIR_VIEW_CONTENT_BROWSER_MOUSER_GESTURE_MOUSE_GESTURE_H_
#define AIR_VIEW_CONTENT_BROWSER_MOUSER_GESTURE_MOUSE_GESTURE_H_

#include "base/memory/singleton.h"
#include <list>
#include <vector>

typedef enum {
  MGD_NONE,
  MGD_UP,  //
  MGD_DOWN,
  MGD_LEFT,
  MGD_RIGHT
} XDirection;                                    //������Ƶķ���
typedef std::vector<XDirection> XMouseGestures;  //ʶ����������Ʒ��򼯺�

class MouseGestureWindow;
class MouseGesture {
 public:
  static MouseGesture* GetInstance() { return Singleton<MouseGesture>::get(); }
  MouseGesture();
  ~MouseGesture() {}

  // ==helper==================
  void SetDestWindow(HWND dest_window);
  bool IsMouseGestureWindowShow();

  // ==Message Handler =========
  bool DownEvent(const MSG* msg);
  bool MoveEvent(const MSG* msg);

  // false ����Ҫ�����˵�
  bool UpEvent(const MSG* msg);
  void CancelEvent();  //ȡ���������

 private:
  MouseGestureWindow* window_;  //������ƵĹ켣����
  HWND dest_window_;            //������Ƶ�Ŀ�괰��

  friend class Singleton<MouseGesture>;
  friend struct DefaultSingletonTraits<MouseGesture>;
  DISALLOW_COPY_AND_ASSIGN(MouseGesture);
};

#endif  // AIR_VIEW_CONTENT_BROWSER_MOUSER_GESTURE_MOUSE_GESTURE_H_
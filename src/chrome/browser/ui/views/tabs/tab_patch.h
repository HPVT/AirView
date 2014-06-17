// Copyright (c) 2012 The Chromium Authors. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

#ifndef CHROME_BROWSER_UI_VIEWS_TABS_TAB_PATCH_H_
#define CHROME_BROWSER_UI_VIEWS_TABS_TAB_PATCH_H_
#include "base/patch.h"
namespace ui{
class MouseEvent;
}
class Profile;
X_START_CLASS_PATCH(Tab)
public:
void Constructor(Profile* profile) {
  profile_ = profile;
}
//handle �Ƿ����˸���Ϣ����������ˣ���ô����Ҫ�������´���
//������������˫���ر���Ϣ
bool  OnMousePressed(const ui::MouseEvent& event,bool& handle);
private:
Profile* profile_;
X_END_PATCH(Tab)

#endif
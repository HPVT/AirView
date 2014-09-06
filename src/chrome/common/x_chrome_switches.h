// Copyright (c) 2014 The AirView Authors. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

// Defines all the command-line switches used by Chrome.

#ifndef CHROME_COMMON_CHROME_SWITCHES_H_
#define CHROME_COMMON_CHROME_SWITCHES_H_

#include "build/build_config.h"
#include "base/base_switches.h"

namespace switches {
extern const char kDefaultUseChromeLayout[];  //Ĭ��ʹ��chrome�Ĳ���ģʽ
extern const char kDefaultUseChromeSignin[];  //ʹ��chromeĬ�ϵ�¼��ʽ
extern const char kEnableSidebar[];           //ʹ�ò����
extern const char kShowSigninLogo[];          //��ʾ�û�ͷ��
extern const char kAllowAllCrxInstall[];      //���google��Crx��װ����
}

#endif
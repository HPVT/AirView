:: Copyright (c) 2014 The AirView Authors. All rights reserved.
:: Use of this source code is governed by a BSD-style license that can be
:: found in the LICENSE file.

%~d0  
cd %~dp0
cd ../..
cd chromium
cd src
set GYP_MSVS_VERSION=2013
set GYP_GENERATORS=msvs-ninja,ninja
python build/gyp_chromium --depth=. -Dtarget_arch=x64


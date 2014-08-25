// Copyright 2013 The AirView Authors. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

#ifndef CHROME_BROWSER_PROFILES_GLOBLE_PREF_SERVICE_H_
#define CHROME_BROWSER_PROFILES_GLOBLE_PREF_SERVICE_H_

#include "base/basictypes.h"
#include "base/compiler_specific.h"
#include <string>
#include "base/memory/singleton.h"
//-----
//ȫ�ֵ����ã���ͨ��PrefService�������ȡ����,����Profile����
//������ʱʹ��һ��������ʵ��,�����̰߳�ȫ����Ҫ���з��ʶ���UI�߳�����
//-----
class JsonPrefStore;
class GloblePrefService{
public:
	static GloblePrefService* GetInstance() {
		return Singleton<GloblePrefService>::get();
	}

	std::string GetString(const std::string& key,const std::string& default_value) const;
	void SetString(const std::string& key, const std::string& value);
	bool GetBoolean(const std::string& key, bool default_value) const;
	void SetBoolean(const std::string& key, bool value);
	int GetInt(const std::string& key, int default_value) const;
	void SetInt(const std::string& key, int value);

protected:
	GloblePrefService();
	~GloblePrefService();
private:
	scoped_refptr<JsonPrefStore> prefs_;

	friend class Singleton<GloblePrefService>;
	friend struct DefaultSingletonTraits<GloblePrefService>;
	DISALLOW_COPY_AND_ASSIGN(GloblePrefService);
};

#endif //CHROME_BROWSER_PROFILES_GLOBLE_PREF_SERVICE_H_
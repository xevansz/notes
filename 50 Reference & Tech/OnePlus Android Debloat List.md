---
title: OnePlus / ColorOS Android Debloat List
tags:
  - android
  - oneplus
  - debloat
  - adb
  - reference
---

# OnePlus / ColorOS Android Debloat List

> Comprehensive ADB package list for safe removal of telemetry, carrier bloat, background diagnostic trackers, and unnecessary OEM apps on OnePlus / Oppo (ColorOS / OxygenOS).

---

## ⚡ ADB Quick Command Reference

To uninstall for the current user (reversible without root):
```bash
adb shell pm uninstall -k --user 0 <package_name>
```

To restore an uninstalled package:
```bash
adb shell cmd package install-existing <package_name>
```

To batch debloat in bash:
```bash
for pkg in $(cat package_list.txt); do adb shell pm uninstall -k --user 0 $pkg; done
```

---

## 1. OnePlus / ColorOS / Oppo Bloatware

```text
com.coloros.video
com.coloros.scenemode
com.coloros.smartsidebar
com.coloros.operationManual
com.coloros.childrenspace
com.coloros.accessibilityassistant
com.coloros.floatassistant
com.oplus.metis
com.oplus.stdsp
com.oplus.healthservice
com.oplus.qualityprotect
com.oplus.sauhelper
com.oplus.dmp
com.oplus.securitykeyboard
com.oplus.obrain
com.oplus.omojis
com.oplus.onetrace
com.oplus.lfeh
com.oplus.powermonitor
com.oplus.encryption
com.oplus.location
com.oplus.engineercamera
com.oplus.engineernetwork
com.oplus.eyeprotect
com.oplus.logkit
com.oplus.postmanservice
com.oplus.eid
com.oplus.engineermode
com.oplus.statistics.rom
com.oplus.bttestmode
com.oplus.locationproxy
com.oplus.aiwriter
net.oneplus.weather
com.oneplus.membership
com.oppo.quicksearchbox
android.autoinstalls.config.oneplus
```

---

## 2. HeyTap & Roaming Services

```text
com.heytap.mcs
com.heytap.cloud
com.heytap.browser
com.redteamobile.roaming
```

---

## 3. Microsoft Preloaded Services

```text
com.microsoft.appmanager
com.microsoft.deviceintegrationservice
com.microsoftsdk.crossdeviceservicebroker
```

---

## 4. Google Analytics, AdServices & Tracking

```text
com.google.android.gms.supervision
com.google.android.accessibility.switchaccess
com.google.android.gms.location.history
com.google.android.onetimeinitializer
com.google.android.odad
com.google.android.apps.walletnfcrel
com.google.android.apps.setupwizard.searchselector
com.google.mainline.adservices
com.google.android.feedback
com.google.android.apps.tachyon
com.google.android.apps.nbu.files
com.google.android.apps.work.clouddpc
com.google.ambient.streaming
com.google.android.ondevicepersonalization.services
com.google.android.federatedcompute
com.google.android.overlay.modules.healthfitness.forframework
com.google.android.adservices.api
com.google.android.apps.restore
```

---

## 5. Qualcomm Telemetry & Background Daemons

```text
com.qualcomm.qti.powersavemode
com.qti.qcc
com.qualcomm.qti.xrcb
com.qualcomm.qti.xrvd.service
com.qualcomm.location
com.qualcomm.atfwd
com.qualcomm.qti.devicestatisticsservice
com.qualcomm.qti.qms.service.trustzoneaccess
com.qualcomm.qti.uimGbaApp
com.qualcomm.uimremoteclient
com.qualcomm.uimremoteserver
com.qti.dcf
```

---

## 6. Android Stub & Diagnostic Packages

```text
com.android.traceur
com.wapi.wapicertmanage
com.android.hotwordenrollment.okgoogle
com.android.hotwordenrollment.xgoogle
com.android.email.partnerprovider
com.android.microdroid.empty_payload
com.android.providers.partnerbookmarks
com.android.systemui.accessibilitymenu
com.android.egg
```

---
*Related: [[00 Meta/Dashboard|Dashboard]]*

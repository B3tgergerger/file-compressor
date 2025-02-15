# MyCompressor

برنامج لضغط واستخراج الملفات باستخدام تقنيات متعددة مثل 7z وZIP وTAR وGZIP، مع واجهة مستخدم رسومية متطورة باستخدام `customtkinter`.

## كيفية استخدام البرنامج

### ضغط الملفات

1. اختر طريقة الضغط:
   - ZIP
   - TAR
   - GZIP
   - 7z

2. أدخل مستوى الضغط (رقم بين 1 و 22).
3. أدخل كلمة المرور (اختياري).
4. انقر على "Select Files" لاختيار الملفات.
5. انقر على "Start Compression" لبدء عملية الضغط.
6. بعد الانتهاء، سيظهر ملف مضغوط في المجلد الحالي.

### استخراج الملفات

1. انقر على "Extract Files".
2. اختر الملف المضغوط من جهاز الكمبيوتر.
3. سيتم استخراج الملفات إلى المجلد الحالي.

### متى تستخدم كل نوع من أنواع الضغط؟

- **ZIP**: للاستخدام العام والتوافق العالي.
- **TAR**: لأرشفة الملفات في بيئات UNIX.
- **GZIP**: لضغط سريع وفعال في بيئات UNIX.
- **7z**: لأرشيفات كبيرة وضغط عالي.

## تثبيت وتشغيل البرنامج

1. حمل الملف التنفيذي (`compressor_gui.exe`) من صفحة الإصدارات.
2. شغل البرنامج بالنقر المزدوج على الملف التنفيذي.
3. اتبع التعليمات في واجهة المستخدم لضغط أو استخراج الملفات.

## متطلبات النظام

- نظام تشغيل Windows 10 أو أعلى.
- Python 3.9 أو أعلى (لتطوير البرنامج).

## المساهمة

نرحب بالمساهمات لتحسين البرنامج. الرجاء فتح مشكلة جديدة على GitHub لمناقشة أي تحسينات أو أخطاء.

## الترخيص

هذا المشروع مرخص بموجب ترخيص MIT. انظر ملف `LICENSE` لمزيد من التفاصيل.

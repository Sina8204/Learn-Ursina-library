```markdown
# آموزش Ursina - مفاهیم پایه

این سورس کد بر اساس مستندات کتابخانه Ursina برای آموزش مفاهیم پایه مانند مدل‌ها، بافت‌ها، رنگ‌ها، موقعیت، چرخش و مقیاس تهیه شده است.

## ساختار اصلی برنامه

```python
from ursina import *

app = Ursina()

# کدهای آموزشی اینجا قرار می‌گیرند

app.run()
```

- `from ursina import *`: تمام کلاس‌ها و توابع مورد نیاز Ursina را وارد می‌کند
- `app = Ursina()`: نمونه اصلی برنامه را ایجاد می‌کند
- `app.run()`: حلقه اصلی بازی را اجرا می‌کند

## 1. مدل‌ها (Models)

مدل‌ها اشیاء سه‌بعدی یا دو‌بعدی هستند که در صحنه نمایش داده می‌شوند.

```python
# ایجاد یک مکعب با بافت تصویری
e1 = Entity(model='cube', texture='Asset/img.jpeg')

# ایجاد یک مکعب با بافت ویدئویی
e4 = Entity(model='cube', texture='Asset/movie.mp4')
```

- `Entity`: کلاس پایه برای ایجاد اشیاء در Ursina
- `model='cube'`: شکل مکعبی را برای entity تعیین می‌کند
- `texture`: بافت سطح entity را مشخص می‌کند (تصویر یا ویدئو)

## 2. بافت‌ها (Textures)

بافت‌ها برای پوشش دادن سطح مدل‌ها استفاده می‌شوند.

```python
# ایجاد یک Sprite با بافت تصویری
s = Sprite('Asset/img.jpeg') 
print(s.aspect_ratio)  # چاپ نسبت ابعاد تصویر
```

- `Sprite`: Entity دوبعدی برای نمایش تصاویر
- `aspect_ratio`: نسبت عرض به ارتفاع تصویر را نشان می‌دهد

## 3. رنگ‌ها (Colors)

روش‌های مختلف برای تعیین رنگ اشیاء:

```python
e = Sprite()

# استفاده از رنگ‌های predefined
e.color = color.red

# استفاده از سیستم رنگی HSV
e.color = hsv(120, .5, .5)

# استفاده از سیستم رنگی RGB
e.color = rgb(.8, .1, 0)

# استفاده از کد هگزادسیمال
e.color = '#aabbcc'

# تینت کردن رنگ (روشن/تاریک کردن)
e.color = e.color.tint(.1)

# رنگ تصادفی
e.color = color.random_color()

# درون‌یابی بین دو رنگ
e.color = lerp(color.red, color.green, .5)
```

- `hsv(hue, saturation, value)`: رنگ بر اساس فام، اشباع و مقدار
- `tint()`: رنگ را روشن‌تر (مقدار مثبت) یا تیره‌تر (مقدار منفی) می‌کند
- `lerp()`: درون‌یابی خطی بین دو رنگ

## 4. موقعیت (Position)

تعیین موقعیت اشیاء در فضای سه‌بعدی:

```python
e = Entity(model='cube')

# روش‌های مختلف تعیین موقعیت
e.position = Vec3(0, 0, 0)  # موقعیت سه‌بعدی
e.position = Vec2(0, 0)      # موقعیت دو‌بعدی
e.position = (0, 0, 0)       # تاپل سه‌عددی
e.position = (0, 0)          # تاپل دو‌عددی

# تعیین موقعیت با استفاده از خصوصیات جداگانه
e2 = Entity(model='cube', position=Vec3(1, 1, 1))
e2.x = 0  # تغییر فقط مختصات x
print(e2.position)

# موقعیت نسبی به والد
parent_entity = Entity(model='cube', position=Vec3(0, 2, 0))
e = Entity(model='cube', parent=parent_entity, position=Vec3(0, 2, 0))
print(e.position)        # موقعیت محلی نسبت به والد
print(e.world_position)  # موقعیت جهانی در صحنه

# تنظیم موقعیت جهانی
e.world_position = Vec3(0, 0, 0)
print(e.position)  # موقعیت محلی به روز شده
```

- `position`: موقعیت محلی نسبت به والد
- `world_position`: موقعیت جهانی در صحنه
- `parent`: entity والد که موقعیت فرزند نسب به آن محاسبه می‌شود

## 5. چرخش (Rotation)

کنترل جهت و چرخش اشیاء:

```python
e = Entity(model='cube')

# تنظیم چرخش
e.rotation = (0, 0, 0)  # (چرخش حول X, چرخش حول Y, چرخش حول Z)
e.rotation_y = 90       # چرخش 90 درجه حول محور Y

# نگاه کردن به entity دیگر
other_entity = Entity(position=(10, 1, 8))
e.look_at(other_entity)              # محور Z به سمت entity اشاره می‌کند
e.look_at(other_entity, axis='up')   # تعیین محور دلخواه برای جهت‌گیری
```

- `rotation`: تاپل چرخش در هر سه محور
- `rotation_x`, `rotation_y`, `rotation_z`: چرخش حول محورهای خاص
- `look_at()`: entity را به سمت نقطه یا entity دیگر می‌چرخاند

## 6. مقیاس (Scale)

تغییر اندازه اشیاء:

```python
# مقیاس دهی مکعب (عرض, ارتفاع, عمق)
e = Entity(model='cube', scale=(3, 1, 1))
```

- `scale`: تعیین اندازه در هر محور
- مقادیر بیشتر از 1 بزرگ‌تر و کمتر از 1 کوچک‌تر نشان می‌دهند

## نکات مهم

1. **سیستم مختصات**: محور X (راست/چپ)، محور Y (بالا/پایین)، محور Z (جلو/عقب)

2. **انواع داده‌های موقعیت**: 
   - `Vec2`: برای موقعیت دو‌بعدی (x, y)
   - `Vec3`: برای موقعیت سه‌بعدی (x, y, z)

3. **بهترین praktyce‌ها**:
   - همیشه Assets را در پوشه مناسب قرار دهید
   - برای کارایی بهتر، از بافت‌های بهینه شده استفاده کنید
   - موقعیت والد-فرزندی را برای سازماندهی بهتر صحنه استفاده کنید

4. **رنگ‌ها**: Ursina از سیستم‌های رنگی مختلف پشتیبانی می‌کند که آزادی عمل زیادی در طراحی می‌دهد

## اجرای برنامه

برای اجرای این کد:
1. فایل را با پسوند `.py` ذخیره کنید
2. کتابخانه ursina را نصب کنید: `pip install ursina`
3. فایل را اجرا کنید: `python filename.py`
```

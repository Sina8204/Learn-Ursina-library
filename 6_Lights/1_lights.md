مبحث **نور (Lighting)** در پکیج `ursina` یکی از مباحث کلیدی برای زیبا و واقع‌گرایانه کردن بازی‌های سه‌بعدی است. 

در `ursina` (که در واقع یک لایه‌ی ساده‌شده روی موتور `Panda3D` است)، نورپردازی به دو روش اصلی انجام می‌شود:

1. **نور محیطی (Ambient Light)**: نوری یکنواخت که همه‌جا را به یک اندازه روشن می‌کند (سایه ندارد).
2. **نورهای جهت‌دار، نقطه‌ای و نقطه‌ای جهتی (Directional, Point, Spot)**: نوری که از یک منبع خاص ساطع می‌شود و باعث ایجاد سایه و عمق می‌شود.

---

### مرحله 1: ساختار اولیه (بدون نور)
اول یک صحنه ساده می‌سازیم که در آن یک مکعب و یک صفحه (زمین) داریم، اما **هیچ نوری** به آن نمی‌دهیم تا ببینید چه شکلی می‌شود.

```python
from ursina import *

app = Ursina()

# ایجاد زمین و مکعب بدون هیچ نوری
ground = Entity(model='plane', scale=(10, 1, 10), color=color.gray, texture='white_cube')
cube = Entity(model='cube', scale=1, position=(0, 0.5, 0), color=color.orange)

# دوربین را بچرخانیم تا صحنه را خوب ببینیم
EditorCamera()  # با کلید راست ماوس می‌چرخد

app.run()
```
اگر این کد را اجرا کنید، مکعب و زمین را به صورت یکدست و تخت (Flat) می‌بینید. چون خبری از سایه و عمق نیست.

---

### مرحله 2: اضافه کردن نور محیطی (Ambient Light)
نور محیطی، پایه‌ترین نور است. اگر این نور نباشد، پشت اشیاء کاملاً سیاه دیده می‌شود.

```python
from ursina import *

app = Ursina()

# اضافه کردن نور محیطی با رنگ سفید و شدت 0.5
ambient_light = AmbientLight(color=color.rgb(100, 100, 100))  # خاکستری روشن

ground = Entity(model='plane', scale=(10, 1, 10), color=color.gray, texture='white_cube')
cube = Entity(model='cube', scale=1, position=(0, 0.5, 0), color=color.orange)

EditorCamera()
app.run()
```
**نکته:** شدت نور محیطی نباید زیاد باشد (حداکثر ۰.۵ یا ۱۵۰ از ۲۵۵) تا جلوه‌ی نورهای دیگر را خراب نکند.

---

### مرحله 3: نور جهت‌دار (Directional Light) - مهم‌ترین نور
نور جهت‌دار مثل خورشید است. از یک جهت می‌تابد و تمام صحنه را تحت تأثیر قرار می‌دهد. **برای دیدن سایه، حتماً باید از این نوع نور استفاده کنید.**

```python
from ursina import *

app = Ursina()

# نور محیطی ملایم
ambient_light = AmbientLight(color=color.rgb(50, 50, 50))

# نور خورشید (جهت‌دار) از بالا و مایل
directional_light = DirectionalLight()
directional_light.look_at(Vec3(1, -1, -1))  # جهت تابش

# برای فعال کردن سایه‌ها (Shadow)
directional_light.shadow_map_resolution = (1024, 1024)  # کیفیت سایه

ground = Entity(model='plane', scale=(10, 1, 10), texture='grass', collider='box')
cube = Entity(model='cube', scale=1, position=(0, 0.5, 0), color=color.orange, collider='box')

# برای دیدن سایه، باید اشیاء را کمی جابجا کنیم
cube2 = Entity(model='sphere', scale=0.8, position=(2, 0.4, 1), color=color.blue)

EditorCamera()
app.run()
```
**نکته طلایی:** اگر سایه‌ها را نمی‌بینید، مطمئن شوید که `collider='box'` یا `collider='mesh'` را به اشیاء اضافه کرده‌اید (سایه‌ها روی Colliderها محاسبه می‌شوند).

---

### مرحله 4: نور نقطه‌ای (Point Light) - مثل لامپ یا آتش
نور نقطه‌ای از یک نقطه در فضا به تمام جهات می‌تابد. برای شمع، چراغ‌ها و آتش بازی مناسب است.

```python
from ursina import *

app = Ursina()

ambient_light = AmbientLight(color=color.rgb(30, 30, 30))

# ساخت یک نور نقطه‌ای قرمز رنگ در سمت راست
point_light = PointLight(color=color.red, position=(2, 2, 0))
# تنظیمات شعاع و شدت نور نقطه‌ای
point_light.attenuation = (0, 0, 0.1)  # (ثابت, خطی, درجه‌2) - هرچه عدد درجه‌2 بیشتر باشد، نور سریع‌تر کمرنگ می‌شود.

ground = Entity(model='plane', scale=(10, 1, 10), texture='white_cube')
cube = Entity(model='cube', scale=1, position=(0, 0.5, 0), color=color.orange)
sphere = Entity(model='sphere', scale=0.8, position=(2, 0.4, 0), color=color.blue)

# یک نشانگر برای محل نور بگذاریم
light_indicator = Entity(model='sphere', scale=0.2, position=(2, 2, 0), color=color.red)

EditorCamera()
app.run()
```
توجه کنید که سمت راست مکعب (نزدیک به نور قرمز) پررنگ‌تر و سمت چپ آن تاریک‌تر است.

---

### مرحله 5: نور نقطه‌ای جهتی (Spot Light) - مثل چراغ قوه
این نور مخروطی شکل از یک نقطه به یک جهت خاص می‌تابد (مثل چراغ مطالعه یا چراغ جلوی ماشین).

```python
from ursina import *

app = Ursina()

ambient_light = AmbientLight(color=color.rgb(30, 30, 30))

# نور چراغ قوه‌ای که به سمت مکعب می‌تابد
spot_light = SpotLight(position=(0, 3, 3), direction=(0, -1, -1), color=color.yellow)
spot_light.spot_angle = 20  # زاویه‌ی مخروط بر حسب درجه (عدد کمتر = نور باریک‌تر)

ground = Entity(model='plane', scale=(10, 1, 10), texture='white_cube')
cube = Entity(model='cube', scale=1, position=(0, 0.5, 0), color=color.orange)

# نشانگر محل چراغ قوه
indicator = Entity(model='cube', scale=0.2, position=(0, 3, 3), color=color.yellow)

EditorCamera()
app.run()
```

---

### مرحله 6: حرکت دادن نور (نور پویا)
در بازی‌ها، نورها می‌توانند متحرک باشند (مثل خورشید که حرکت می‌کند یا چراغ قوه‌ی دست بازیکن).

```python
from ursina import *

app = Ursina()

ambient_light = AmbientLight(color=color.rgb(30, 30, 30))
point_light = PointLight(color=color.orange, position=(0, 5, 0))

ground = Entity(model='plane', scale=(10, 1, 10), texture='white_cube')
cube = Entity(model='cube', scale=1, position=(0, 0.5, 0), color=color.blue)

# تابعی برای به‌روزرسانی هر فریم
def update():
    # نور دور یک دایره به دور مکعب می‌چرخد
    point_light.x = 3 * math.sin(time.time())  # سینوس زمان
    point_light.z = 3 * math.cos(time.time())  # کسینوس زمان
    point_light.y = 2 + math.sin(time.time() * 2)  # بالا و پایین می‌رود

EditorCamera()
app.run()
```
با اجرای این کد، می‌بینید که سایه‌ی مکعب مدام تغییر جهت می‌دهد.

---

### جدول جمع‌بندی انواع نور در Ursina

| نوع نور | کلاس | کاربرد | ویژگی مهم |
| :--- | :--- | :--- | :--- |
| **نور محیطی** | `AmbientLight` | روشن کردن کلی صحنه (پیش‌فرض) | شدت آن نباید زیاد باشد |
| **نور جهت‌دار** | `DirectionalLight` | خورشید، ایجاد سایه‌های قوی | حتماً `look_at` برای جهت‌دهی استفاده کنید |
| **نور نقطه‌ای** | `PointLight` | لامپ، آتش، شمع | دارای `attenuation` برای کمرنگ‌شدن تدریجی |
| **نور نقطه‌ای جهتی** | `SpotLight` | چراغ قوه، نورافکن | دارای `spot_angle` برای باریک یا پهن کردن نور |

---

### ۳ ترفند حرفه‌ای که کمتر کسی می‌داند:

1. **رنگ نور با رنگ آبجکت ترکیب می‌شود:** اگر نور قرمز به یک مکعب آبی بتابد، رنگ بنفش دیده می‌شود (ترکیب RGB).
2. **برای عملکرد بهتر (Performance):** اگر بازی شما سنگین شد، تعداد نورهای `PointLight` و `SpotLight` را کم کنید و به جای آن از `DirectionalLight` استفاده کنید.
3. **غیرفعال کردن نور:** برای خاموش کردن یک نور، کافی است `enabled = False` را به آن نسبت دهید:
   ```python
   point_light.enabled = False  # خاموش
   point_light.enabled = True   # روشن
   ```

---

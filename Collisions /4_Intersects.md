## تابع intersects() چیست؟

`intersects()` یک متد برای **تشخیص برخورد (collision detection)** بین Entity‌هایی هست که **collider** دارند. این تابع بررسی می‌کنه که آیا یک Entity با Entity دیگه برخورد کرده یا نه.

## ساختار کلی

```python
result = entity1.intersects(entity2)
```

## مقدار بازگشتی (Return Value)

تابع `intersects()` یک آبجکت برمی‌گردونه که خصوصیت `.hit` داره:
- **`.hit = True`** : اگر برخورد رخ داده باشد
- **`.hit = False`** : اگر برخوردی در کار نباشد

## مثال کامل از مستندات

```python
from ursina import *

app = Ursina()

# بازیکن با collider جعبه‌ای
player = Entity(
    model='cube', 
    color=color.orange, 
    collider='box', 
    origin_y=-.5
)

# جعبه محرک (Trigger Box)
trigger_box = Entity(
    model='wireframe_cube', 
    color=color.gray, 
    scale=2, 
    collider='box', 
    position=Vec3(1,0,2), 
    origin_y=-.5
)

EditorCamera()  # دوربین برای ویرایش صحنه

def update():
    # حرکت بازیکن با کلیدهای WASD
    player.z += (held_keys['w'] - held_keys['s']) * time.dt * 6
    player.x += (held_keys['d'] - held_keys['a']) * time.dt * 6

    # بررسی برخورد بین بازیکن و جعبه محرک
    if player.intersects(trigger_box).hit:
        trigger_box.color = color.lime  # تغییر رنگ به سبز هنگام برخورد
        print('player is inside trigger box')
    else:
        trigger_box.color = color.gray  # رنگ خاکستری در حالت عادی

app.run()
```

## نکات مهم در مثال

| عنصر | توضیح |
|------|-------|
| **origin_y=-.5** | نقطه محور Entity را پایین می‌برد تا برخورد از پایین شیء محاسبه شود |
| **collider='box'** | هر دو Entity باید collider داشته باشند تا برخورد تشخیص داده شود |
| **held_keys** | برای حرکت دادن بازیکن با صفحه کلید |
| **time.dt** | ضریب زمانی برای حرکت صاف و مستقل از فریم ریت |

## مفهوم Trigger Box

در این مثال، **trigger_box** مانند یک منطقه محرک (trigger zone) عمل می‌کند:
- وقتی بازیکن وارد جعبه می‌شه → رنگش سبز می‌شه
- وقتی خارج می‌شه → برمی‌گرده به رنگ خاکستری

## کاربردهای رایج intersects()

```python
# 1. تشخیص برخورد ساده
if player.intersects(enemy).hit:
    player.health -= 10

# 2. برداشتن آیتم
if player.intersects(coin).hit:
    destroy(coin)
    score += 1

# 3. فعال کردن درب
if player.intersects(door_trigger).hit:
    door.open()

# 4. تشخیص ورود به منطقه
if player.intersects(zone).hit:
    print("وارد منطقه امن شدی!")
```

## محدودیت‌ها و نکات

⚠️ **نکات مهم:**
- هر دو Entity باید **collider** داشته باشند
- می‌توانید از انواع مختلف collider استفاده کنید (box, sphere, mesh)
- تابع `intersects()` می‌تواند بین هر دو Entity با هر نوع collider ای کار کند

## خروجی نمونه

وقتی بازیکن وارد trigger_box می‌شه:
```
player is inside trigger box
player is inside trigger box
...
```

و رنگ جعبه از خاکستری به سبز تغییر می‌کنه.

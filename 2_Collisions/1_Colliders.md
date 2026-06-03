## Collider در Ursina چیست؟

**Collider** ها برای تشخیص برخورد (collision detection) بین اشیاء در بازی استفاده می‌شوند. اون‌ها شکل‌های نامرئی هستند که دور Entity قرار می‌گیرند تا برخوردها رو تشخیص بدن.

## روش‌های اضافه کردن Collider

### 1. **روش ساده (با استفاده از باندهای Entity)**

```python
e = Entity(model='sphere', x=2)
e.collider = 'box'      # یک BoxCollider بر اساس ابعاد entity اضافه می‌کنه
e.collider = 'sphere'   # یک SphereCollider بر اساس ابعاد entity اضافه می‌کنه
e.collider = 'mesh'     # یک MeshCollider بر اساس ابعاد entity اضافه می‌کنه
```

در این روش، collider به صورت خودکار اندازه و موقعیتش را از **bounds** (ابعاد و موقعیت) Entity می‌گیره.

### 2. **روش پیشرفته (با مشخص کردن سایز و موقعیت دلخواه)**

```python
# BoxCollider با سایز و موقعیت سفارشی
e.collider = BoxCollider(e, center=Vec3(0,0,0), size=Vec3(1,1,1))

# SphereCollider با شعاع و موقعیت سفارشی
e.collider = SphereCollider(e, center=Vec3(0,0,0), radius=.75)

# MeshCollider با شکل سفارشی
e.collider = MeshCollider(e, mesh=e.model, center=Vec3(0,0,0))
```

## **نکته مهم: ترتیب تعریف**

طبق مستندات، اگر می‌خواهید collider با **bounds** Entity هماهنگ باشه، باید **مدل رو قبل از collider** تعریف کنید:

```python
# ✅ درست - collider با مدل هماهنگ میشه
e = Entity(model='cube', collider='box')

# ✅ یا به این صورت:
e = Entity(model='cube')
e.collider = 'box'  # حالا collider با اندازه cube هماهنگه

# ❌ اشتباه - collider اندازه درستی نخواهد داشت
e = Entity(collider='box')
e.model = 'cube'  # collider قبلاً ساخته شده و با مدل جدید تطابق نداره
```

## انواع Collider و کاربردشان

| نوع | کاربرد |
|------|--------|
| **box** | برای اشیای مکعبی یا جعبه‌ای، سریع‌ترین گزینه |
| **sphere** | برای اشیای گرد مثل توپ، سیاره |
| **mesh** | دقیق‌ترین گزینه، اما سنگین‌تر. برای اشکال پیچیده |

## مثال عملی

```python
from ursina import *

app = Ursina()

# استفاده ساده
player = Entity(model='cube', color=color.blue, collider='box')
enemy = Entity(model='sphere', x=2, color=color.red, collider='sphere')

# collider سفارشی
door = Entity(model='cube', scale=(1, 2, 0.2))
door.collider = BoxCollider(door, center=Vec3(0,0,0), size=Vec3(1, 2, 0.2))

def update():
    # حرکت با کلیدهای WASD
    player.x += held_keys['d'] * time.dt
    player.x -= held_keys['a'] * time.dt
    
    # تشخیص برخورد
    if player.intersects(enemy).hit:
        print("برخورد شد!")

app.run()
```

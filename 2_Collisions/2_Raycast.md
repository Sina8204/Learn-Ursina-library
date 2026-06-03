## Raycast چیست؟

Raycast یه پرتوی فرضیه که از یه نقطه در جهت مشخص شلیک میشه تا ببینه به چه چیزی برخورد میکنه. مثل یه لیزر که از یه نقطه شلیک میکنی و میبینی به کدوم دیوار یا شیء میخوره.

## ساختار تابع Raycast

```python
raycast(origin, direction=(0,0,1), distance=inf, traverse_target=scene, ignore=list(), debug=False)
```

### پارامترها:

1. **`origin`** (اجباری): نقطه شروع پرتو (موقعیت سه‌بعدی)
2. **`direction`**: جهت پرتو، پیش‌فرض `(0,0,1)` یعنی جلو
3. **`distance`**: حداکثر فاصله برای بررسی، پیش‌فرض `inf` (بینهایت)
4. **`traverse_target`**: فقط اشیاء خاص و فرزندانشون رو بررسی کن
5. **`ignore`**: لیست اشیایی که باید نادیده گرفته بشن
6. **`debug`**: اگر `True` باشه، خط رو روی صفحه نشون میده

## خروجی (HitInfo)

تابع یه آبجکت **HitInfo** برمیگردونه با ویژگی‌های مهم:

- **`hit`**: `True` اگر به چیزی برخورد کرده باشه، `False` اگه نه
- **`entity`**: شیئی که بهش برخورد شده
- **`point`**: نقطه دقیق برخورد (مختصات سه‌بعدی)
- **`world_point`**: نقطه برخورد در مختصات جهانی
- **`distance`**: فاصله از مبدا تا نقطه برخورد
- **`normal`**: نرمال سطح برخورد (جهت عمود بر سطح)

## مثال ساده

```python
from ursina import *

app = Ursina()

player = Entity(model='cube', color=color.orange, collider='box')
wall = Entity(model='cube', collider='box', color=color.azure, 
              position=(0,0,5), scale=(3,3,0.5))

def update():
    # پرتو از موقعیت بازیکن به سمت جلو
    hit_info = raycast(player.position, direction=(0,0,1), 
                      distance=10, debug=True)
    
    if hit_info.hit:
        print(f"برخورد به: {hit_info.entity}")
        print(f"فاصله: {hit_info.distance}")
        wall.color = color.red
    else:
        wall.color = color.azure

app.run()
```

## کاربرد واقعی: حرکت بازیکن با تشخیص برخورد

این کدی که خودت فرستادی رو بررسی کنم:

```python
class Player(Entity):
    def update(self):
        # ۱. محاسبه جهت حرکت
        self.direction = Vec3(
            self.forward * (held_keys['w'] - held_keys['s'])
            + self.right * (held_keys['d'] - held_keys['a'])
        ).normalized()
        
        # ۲. شروع پرتو از کمی بالاتر از زمین
        origin = self.world_position + (self.up * 0.5)
        
        # ۳. شلیک پرتو در جهت حرکت
        hit_info = raycast(origin, self.direction, 
                          ignore=(self,), distance=0.5, debug=False)
        
        # ۴. فقط اگه برخورد نکرده باشه حرکت کن
        if not hit_info.hit:
            self.position += self.direction * 5 * time.dt
```

### توضیح گام به گام:
- **`self.up * 0.5`**: پرتو از کمر بازیکن شروع میشه (نه از پاهاش) تا بتونه از رمپ‌ها بالا بره
- **`ignore=(self,)`**: خود بازیکن رو نادیده میگیره تا به خودش برخورد نکنه
- **`distance=0.5`**: فقط تا نیم متر جلو رو چک میکنه
- **`if not hit_info.hit`**: اگه به دیوار برخورد نکرده باشه، اجازه حرکت میده

## نکات مهم

1. **همیشه `collider` بدید**: Raycast فقط به اشیایی که `collider` دارن برخورد میکنه:
   ```python
   wall = Entity(model='cube', collider='box')  # درست ✅
   wall2 = Entity(model='cube')  # غلط ❌ - raycast بهش برخورد نمیکنه
   ```

2. **انواع collider**: میتونید از `'box'`, `'sphere'`, `'mesh'` یا `'plane'` استفاده کنید

3. **عکس‌العمل به برخورد**:
   ```python
   hit = raycast(origin, direction, distance=5)
   if hit.hit:
       if hit.entity.name == "enemy":
           hit.entity.health -= 10
   ```

## مثال پیشرفته: تشخیص سطح زمین

```python
def update(self):
    # پرتو به سمت پایین برای تشخیص زمین
    ground_check = raycast(self.position + (0, 1, 0), 
                          direction=(0,-1,0), 
                          distance=1.2)
    
    if ground_check.hit:
        self.is_grounded = True
        self.y = ground_check.point[1] + 0.5  # بچسب به زمین
    else:
        self.is_grounded = False
        self.y -= 0.1  # گرانش
```

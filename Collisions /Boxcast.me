## Boxcast چیه؟

Boxcast مثل Raycast عمل میکنه، با این تفاوت که به جای یه پرتو نازک (خط)، یه **جعبه** رو در جهت مشخص حرکت میده و برخورد این جعبه رو با اشیاء دیگه چک میکنه. این خیلی مفیده برای تشخیص برخورد بازیکن یا اشیایی که ابعاد دارن.

## تفاوت اصلی با Raycast

- **Raycast**: یه خط فرضی (بدون ضخامت) - فقط برخورد با مرکز خط رو چک میکنه
- **Boxcast**: یه جعبه با عرض و ارتفاع مشخص - برخورد کل جعبه رو چک میکنه (واقع‌بینانه‌تر)

## ساختار تابع Boxcast

```python
boxcast(origin, direction=(0,0,1), distance=9999, 
        thickness=(1,1), traverse_target=scene, 
        ignore=list(), debug=False)
```

### پارامترهای جدید:

**`thickness=(width, height)`**: 
- جزء اول (`width`): عرض جعبه (در محور X)
- جزء دوم (`height`): ارتفاع جعبه (در محور Y)
- عمق (Z) همون فاصله حرکت هست

## خروجی (همون HitInfo)

دقیقاً مثل Raycast خروجی میده:
- `hit`: برخورد کرده؟
- `entity`: شیء برخورد شده
- `point`: نقطه برخورد
- `world_point`: نقطه برخورد جهانی
- `distance`: فاصله

## مثال ساده

```python
from ursina import *

app = Ursina()

# بازیکن با ابعاد واقعی
player = Entity(model='cube', color=color.orange, 
                collider='box', scale=(1,2,1))
                
# دیوار باریک ولی بلند
wall = Entity(model='cube', collider='box', color=color.azure,
              position=(2,0,5), scale=(0.2,3,0.2))

def update():
    # حرکت با WASD
    move = Vec3(
        held_keys['d'] - held_keys['a'],
        0,
        held_keys['w'] - held_keys['s']
    ).normalized()
    
    if move.length() > 0:
        # با Boxcast چک کن جلو راه باز هست؟
        future_pos = player.position + move * 0.5
        
        # باکسکست از موقعیت فعلی به سمت جلو
        hit_info = boxcast(
            origin=future_pos,  # جایی که میخوایم بریم رو چک کن
            direction=move,      # جهت حرکت
            distance=1,          # چقدر جلو رو چک کنه
            thickness=(player.scale_x, player.scale_y),  # اندازه بازیکن
            ignore=[player],     # خودشو نادیده بگیر
            debug=True           # جعبه رو نشون بده (برای دیباگ)
        )
        
        if not hit_info.hit:
            player.position = future_pos
            print("حرکت کردم")
        else:
            print(f"برخورد به: {hit_info.entity.name}, فاصله: {hit_info.distance}")

EditorCamera()  # دوربین قابل چرخش برای دید بهتر
app.run()
```

## کاربردهای عملی

### ۱. تشخیص برخورد بازیکن با دیوارها

```python
class Player(Entity):
    def __init__(self):
        super().__init__(
            model='cube', 
            collider='box', 
            scale=(1, 2, 1),
            color=color.orange
        )
        self.speed = 5
    
    def update(self):
        direction = Vec3(
            held_keys['d'] - held_keys['a'],
            0,
            held_keys['w'] - held_keys['s']
        ).normalized()
        
        if direction.length() > 0:
            # محاسبه موقعیت جدید
            new_pos = self.position + direction * self.speed * time.dt
            
            # Boxcast برای تشخیص برخورد
            hit = boxcast(
                origin=new_pos,  # موقعیت جدید رو چک کن
                direction=direction,
                thickness=(self.scale_x, self.scale_y),
                distance=0.1,
                ignore=[self],
                debug=False
            )
            
            # اگه برخورد نکرد، حرکت کن
            if not hit.hit:
                self.position = new_pos
            else:
                # میتونیم در امتداد دیوار بلغزیم
                print("به دیوار خوردی!")
```

### ۲. تشخیص پله یا لبه پرتگاه

```python
class AdvancedPlayer(Entity):
    def update(self):
        # چک کردن زیر پا (برای تشخیص زمین)
        feet_check = boxcast(
            origin=self.position,
            direction=(0, -1, 0),  # به سمت پایین
            thickness=(self.scale_x - 0.2, 0.1),  # یه ذره از خود بازیکن باریکتر
            distance=1.5,  # تا یک و نیم متر پایین رو چک کن
            ignore=[self],
            debug=False
        )
        
        if not feet_check.hit:
            # افتادن (هوا)
            self.y -= 0.2
            print("در حال سقوط!")
        else:
            # روی زمین ایستاده
            self.y = feet_check.point[1] + self.scale_y/2
```

### ۳. پرش و تشخیص سقف

```python
class JumpingPlayer(Entity):
    def __init__(self):
        super().__init__(collider='box', scale=(1,2,1))
        self.velocity_y = 0
        self.is_grounded = False
    
    def update(self):
        # تشخیص زمین
        ground_hit = boxcast(
            origin=self.position,
            direction=(0, -1, 0),
            thickness=(0.8, 0.1),
            distance=1.1
        )
        self.is_grounded = ground_hit.hit
        
        # پرش
        if self.is_grounded and held_keys['space']:
            self.velocity_y = 8
        
        # تشخیص سقف
        if self.velocity_y > 0:  # وقتی داره بالا میره
            ceiling_hit = boxcast(
                origin=self.position + (0, self.scale_y/2, 0),
                direction=(0, 1, 0),
                thickness=(0.8, 0.1),
                distance=abs(self.velocity_y * time.dt)
            )
            if ceiling_hit.hit:
                self.velocity_y = 0  # به سقف خورد، نپر
                print("به سقف خوردی!")
        
        # اعمال فیزیک
        self.velocity_y -= 0.5  # جاذبه
        self.y += self.velocity_y * time.dt
```

## مقایسه Raycast vs Boxcast با مثال

```python
from ursina import *

app = Ursina()

# سناریو: یه راهرو باریک با یه مانع کوچیک وسط
player = Entity(model='cube', collider='box', scale=(1,1,1), 
                color=color.orange, position=(-3,0,0))
obstacle = Entity(model='cube', collider='box', scale=(0.3,1,1),
                  color=color.red, position=(0,0,3))

def raycast_move():
    # Raycast - فقط خط مرکزی رو چک میکنه
    hit = raycast(player.position, direction=(0,0,1), distance=2)
    if not hit.hit:
        player.z += 1
        print("Raycast: حرکت کردم")
    else:
        print("Raycast: مانع دیدم")

def boxcast_move():
    # Boxcast - کل عرض بازیکن رو چک میکنه
    hit = boxcast(player.position, direction=(0,0,1), 
                  thickness=(player.scale_x, player.scale_y), distance=2)
    if not hit.hit:
        player.z += 1
        print("Boxcast: حرکت کردم")
    else:
        print("Boxcast: برخورد تشخیص دادم")

# نتیجه: 
# Raycast از کنار مانع رد میشه چون مانع باریکه و مرکز خط آزاده!
# Boxcast درست تشخیص میده که بازیکن به مانع میخوره!
```

## تنظیم thickness مثل یه شخصیت

```python
# برای شخصیت‌های ایستاده (بلند و باریک)
thickness=(0.8, 1.8)  # عرض 0.8، ارتفاع 1.8

# برای شخصیت‌های پهن (مثل ماشین)
thickness=(1.5, 0.6)  # عرض 1.5، ارتفاع 0.6

# برای یه توپ
thickness=(1, 1)  # عرض و ارتفاع برابر
```

## مزایای Boxcast نسبت به Raycast

1. ✅ **دقت بیشتر**: برخورد اشیاء با ابعاد واقعی رو تشخیص میده
2. ✅ **لغزش روی دیوار**: بازیکن به جای گیر کردن، در امتداد دیوار میلغزه
3. ✅ **تشخیص لبه‌ها**: میتونه ببینه پاها روی لبه پرتگاه هست یا نه
4. ✅ **واقع‌بینانه‌تر**: مخصوص شخصیت‌های بازی که ابعاد دارن

## نکات مهم

1. **حواست به performance باشه**: Boxcast سنگین‌تر از Raycast هست، پس تو هر فریم زیاد استفاده نکن
2. **ignore رو همیشه بذار**: خود شخصیت رو نادیده بگیر تا به خودش برخورد نکنه
3. **debug موقع تست**: از `debug=True` موقع دیباگ استفاده کن تا ببینی جعبه کجاست

```python
# ترکیب هوشمندانه Raycast و Boxcast
def optimized_movement():
    # اول یه Raycast سریع برای تشخیص دور
    far_check = raycast(player.position, player.forward, distance=5)
    
    if far_check.hit:
        # اگه چیزی نزدیک بود، با Boxcast دقیق چک کن
        near_check = boxcast(player.position, player.forward, 
                            thickness=player.scale, distance=far_check.distance)
        return near_check.hit
    
    return False
```

## Distance Check چیست؟

بررسی فاصله (Distance Check) یک روش ساده برای تشخیص نزدیکی دو Entity به همدیگر است، بدون نیاز به collider پیچیده. این روش برای مواقعی که نیاز به دقت بالایی ندارید، بسیار مناسب است.

## تابع distance()

```python
distance(entity1, entity2)  # فاصله بین دو Entity را محاسبه می‌کند
```

## مثال کامل از مستندات

```python
from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()

# زمین
ground = Entity(
    model='plane', 
    texture='grass', 
    scale=10, 
    collider='box'
)

# بازیکن اول شخص
player = FirstPersonController(
    model='cube', 
    origin_y=-.5, 
    color=color.orange, 
    has_pickup=False  # وضعیت برداشتن آیتم
)

camera.z = -5

# آیتم قابل برداشتن (یک کره)
pickup = Entity(
    model='sphere', 
    position=(1, 0.5, 3)
)

def update():
    # بررسی فاصله بازیکن تا آیتم
    if not player.has_pickup and distance(player, pickup) < pickup.scale_x / 2:
        print('pickup')  # آیتم برداشته شد
        
        player.has_pickup = True
        pickup.animate_scale(0, duration=.1)  # انیمیشن کوچک شدن
        destroy(pickup, delay=.1)  # حذف آیتم بعد از 0.1 ثانیه

app.run()
```

## تحلیل شرط برخورد

```python
distance(player, pickup) < pickup.scale_x / 2
```

این شرط چطور کار می‌کند؟

| بخش | توضیح |
|------|-------|
| `distance(player, pickup)` | فاصله بین بازیکن و آیتم |
| `pickup.scale_x / 2` | نصف عرض آیتم (شعاع کره) |
| شرط `<` | اگر فاصله کمتر از شعاع باشد → برخورد رخ داده |

## مزایای Distance Check نسبت به intersects()

| ویژگی | Distance Check | intersects() |
|-------|----------------|---------------|
| **نیاز به collider** | ❌ خیر | ✅ بله |
| **سرعت** | ⚡ خیلی سریع | 🐢 کمی سنگین‌تر |
| **دقت** | 📏 کمتر (فاصله محض) | 🎯 دقیق (شکل واقعی) |
| **کاربرد** | آیتم‌ها، مناطق دایره‌ای | برخوردهای دقیق فیزیکی |

## مثال‌های کاربردی بیشتر

### 1. **سیستم جمع‌آوری سکه**

```python
coins = []

def create_coins():
    for i in range(10):
        coin = Entity(model='sphere', color=color.yellow, scale=0.3, 
                     position=(random.uniform(-5,5), 0.5, random.uniform(-5,5)))
        coins.append(coin)

def update():
    for coin in coins:
        if distance(player, coin) < 0.5:  # شعاع برداشتن
            coins.remove(coin)
            destroy(coin)
            score += 1
            print(f"Score: {score}")
```

### 2. **نشانگر نزدیکی به دشمن**

```python
def update():
    if distance(player, enemy) < 3:
        print("دشمن نزدیک است! ⚠️")
        enemy.color = color.red
    elif distance(player, enemy) < 5:
        print("دشمن در محدوده هشدار")
        enemy.color = color.orange
    else:
        enemy.color = color.gray
```

### 3. **فعال کردن منطقه شفابخش**

```python
healing_zone = Entity(model='circle', color=color.lime, scale=2, 
                     position=(0,0,0), alpha=0.5)

def update():
    if distance(player, healing_zone) < healing_zone.scale_x / 2:
        player.health = min(player.health + 0.01, 100)  # بازیابی سلامتی
        print(f"Health: {player.health:.1f}")
```

## نکات مهم

### ⚠️ **چه زمانی از Distance Check استفاده کنیم؟**

✅ **مناسب برای:**
- آیتم‌های قابل برداشتن (pickups)
- مناطق دایره‌ای شکل
- چیزهایی که شکل دقیق مهم نیست
- وقتی به Collider نیاز ندارید
- بهینه‌سازی عملکرد

❌ **مناسب نیست برای:**
- برخوردهای دقیق فیزیکی
- اشیای با شکل نامنظم
- وقتی نیاز به واکنش دقیق به زاویه برخورد دارید

### 💡 **مقایسه فاصله‌ها**

```python
# راه‌های مختلف بررسی فاصله
if distance(a, b) < threshold:        # روش ساده
if distance(a, b) ** 2 < threshold**2: # روش بهینه (بدون جذر)
if a.intersects(b).hit:                # روش دقیق با collider
```

## خروجی برنامه

وقتی بازیکن به اندازه کافی به کره نزدیک بشه:
```
pickup
```

و آیتم با انیمیشن کوچک شدن ناپدید می‌شه.

```markdown
# آموزش Ursina - بخش دوم: رویدادها و ورودی‌ها

این بخش از آموزش به بررسی رویدادهای تحدید (Update)، ورودی صفحه کلید، ورودی ماوس و توابع جادویی مانند on_enable، on_disable و on_destroy می‌پردازد.

## 1. رویداد Update (تحدید)

رویداد Update هر فریم یکبار اجرا می‌شود و برای ایجاد انیمیشن‌ها، حرکت اشیاء و بررسی شرایط مداوم استفاده می‌شود.

### روش اول: تابع update جداگانه

```python
e = Entity(model='cube')

def my_update():
    # time.dt زمان سپری شده از فریم قبلی (دلتا تایم)
    e.x += 1 * time.dt  # حرکت با سرعت ثابت 1 واحد در ثانیه

e.update = my_update
```

- `time.dt`: زمان سپری شده بین دو فریم (دلتا تایم)
- استفاده از `time.dt` برای حرکت مستقل از نرخ فریم ضروری است

### روش دوم: کلاس با متد update

```python
class Player(Entity):
    def __init__(self):
        super().__init__()
        self.model = 'cube'
        self.color = color.blue
        self.speed = 2

    def update(self):
        # حرکت مداوم به راست با سرعت مشخص
        self.x += self.speed * time.dt
        
        # برخورد با لبه‌ها و تغییر جهت
        if self.x > 5 or self.x < -5:
            self.speed *= -1  # معکوس کردن جهت
    
player = Player()
```

- `super().__init__()`: فراخوانی سازنده کلاس والد (Entity)
- متد `update()`: هر فریم به صورت خودکار اجرا می‌شود
- این روش برای مدیریت اشیاء پیچیده مناسب‌تر است

## 2. ورودی صفحه کلید (Keyboard Input)

### روش اول: تابع input سراسری

```python
e = Entity(model='quad', color=color.green)

def input(key):
    if key == "s":        # حرکت به پایین
        e.y -= 1
    elif key == "w":      # حرکت به بالا
        e.y += 1
    elif key == "a":      # حرکت به چپ
        e.x -= 1
    elif key == "d":      # حرکت به راست
        e.x += 1
```

- تابع `input(key)`: برای دریافت ورودی‌های سراسری استفاده می‌شود
- `key`: نام کلید فشرده شده (مثل 'w', 's', 'space', 'shift')

### روش دوم: کلاس با متد input

```python
class Player(Entity):
    def __init__(self):
        super().__init__()
        self.model = 'cube'
    
    def input(self, key):
        if key == 'w':
            # حرکت به سمت جلو (جهتی که entity رو به آن است)
            self.position += self.forward

        if key == 'd':
            # انیمیشن چرخش 90 درجه به راست
            self.animate('rotation_y', self.rotation_y + 90, duration=.5)

        if key == 'a':
            # انیمیشن چرخش 90 درجه به چپ
            self.animate('rotation_y', self.rotation_y - 90, duration=.5)

player = Player()
```

- `self.forward`: بردار جهت جلو entity (محور Z)
- `animate()`: ایجاد انیمیشن روی یک ویژگی
  - پارامتر اول: نام ویژگی (مثل 'rotation_y', 'x', 'scale')
  - پارامتر دوم: مقدار نهایی
  - پارامتر `duration`: مدت زمان انیمیشن بر حسب ثانیه

## 3. ورودی ماوس (Mouse Input)

برای تشخیص برخورد ماوس با اشیاء نیاز به کامپوننت `collider` است.

### تشخیص hovering (قرارگیری ماوس روی شیء)

```python
# ایجاد سه مکعب با رنگ‌های مختلف
blue_cube = Entity(model='cube', color=color.blue, position=Vec3(-2,0,0))
green_cube = Entity(model='cube', color=color.green, position=Vec3(0,0,0))
red_cube = Entity(model='cube', color=color.red, position=Vec3(2,0,0))

# افزودن collider به هر entity برای تشخیص برخورد
blue_cube.collider = 'box'
green_cube.collider = 'box'
red_cube.collider = 'box'

def input(key):
    if key == "left mouse down" and blue_cube.hovered:
        print(mouse.hovered_entity, "Blue cube")
    elif key == "left mouse down" and green_cube.hovered:
        print(mouse.hovered_entity, "Green cube")
    elif key == "left mouse down" and red_cube.hovered:
        print(mouse.hovered_entity, "Red cube")
```

- `collider = 'box'`: جعبه برخورد را به entity اضافه می‌کند
- `entity.hovered`: بررسی می‌کند آیا ماوس روی این entity خاص است
- `mouse.hovered_entity`: entity ای که ماوس روی آن قرار دارد را برمی‌گرداند

## 4. توابع کلیک (Click Functions)

### on_click و on_double_click

```python
def action():
    print('Ow! That hurt!')

# ایجاد دکمه با رویداد تک کلیک
one_click_Entity = Entity(
    model='quad', 
    position=Vec3(-2, 0, 0),
    collider='box', 
    on_click=action  # تابعی که با یک کلیک اجرا می‌شود
)

# ایجاد دکمه با رویداد دابل کلیک
double_click_Entity = Entity(
    model='quad',
    position=Vec3(0, 0, 0),
    collider='box', 
    on_double_click=lambda: print("Ahhh, I died")  # تابع لامبدا
)
```

- `on_click`: رویداد یک بار کلیک
- `on_double_click`: رویداد دو بار کلیک سریع
- `lambda`: تابع بدون نام و کوتاه برای عملیات ساده

### on_mouse_enter و on_mouse_exit

```python
# ایجاد دکمه با قابلیت تغییر متن هنگام ورود/خروج ماوس
b = Button(scale=(.5, .25), text='zzz')
b.on_mouse_enter = Func(setattr, b, 'text', 'Hi, friend :D')
b.on_mouse_exit = Func(setattr, b, 'text', '''No! Don't leave me ;-;''')
```

- `on_mouse_enter`: وقتی ماوس وارد محدوده entity می‌شود
- `on_mouse_exit`: وقتی ماوس از محدوده entity خارج می‌شود
- `Func()`: تابعی که با تاخیر یا شرط اجرا می‌شود
- `setattr`: تابع داخلی پایتون برای تنظیم ویژگی اشیاء

## 5. توابع جادویی (Magic Functions)

این توابع در زمان‌های خاصی از چرخه حیات entity اجرا می‌شوند.

### on_enable و on_disable

```python
class MagicLamp(Entity):
    def __init__(self, position=(0,0,0)):
        super().__init__(
            model='cube',
            color=color.yellow,
            scale=1,
            collider='box',
            position=position
        )
        self.is_lit = False
        self.light_effect = None
        
    def on_enable(self):
        """زمانی که entity فعال می‌شود (enabled = True)"""
        print("🟢 Magic lamp activated!")
        # ایجاد افکت نور هنگام فعال شدن
        self.light_effect = Entity(
            model='sphere',
            color=color.yellow,
            scale=1.5,
            position=self.position,
            alpha=0.5
        )
        
    def on_disable(self):
        """زمانی که entity غیرفعال می‌شود (enabled = False)"""
        print("🔴 Magic lamp deactivated!")
        # حذف افکت نور هنگام غیرفعال شدن
        if self.light_effect:
            destroy(self.light_effect)
            self.light_effect = None
```

- `on_enable()`: بعد از `entity.enabled = True` اجرا می‌شود
- `on_disable()`: بعد از `entity.enabled = False` اجرا می‌شود
- کاربرد: راه‌اندازی/توقف انیمیشن‌ها، افکت‌ها، مدیریت منابع

### on_destroy

```python
def on_destroy(self):
    """درست قبل از نابود شدن entity اجرا می‌شود"""
    print("💥 Magic lamp destroyed!")
    
    # ایجاد انفجار جرقه‌ای
    explosion = Entity(
        model='sphere',
        color=color.orange,
        scale=0,
        position=self.position
    )
    explosion.animate_scale(3, duration=0.5, curve=curve.out_elastic)
    destroy(explosion, delay=0.5)  # حذف انفجار بعد از 0.5 ثانیه
    
    # نمایش پیام
    msg = Text(f"Lamp destroyed!", position=(0, 0.3), scale=2, color=color.red)
    destroy(msg, delay=1)

def input(self, key):
    if self.hovered:
        if key == 'right mouse down':
            destroy(self)  # این خط باعث اجرای on_destroy() می‌شود
```

- `on_destroy()`: درست قبل از نابود شدن entity توسط `destroy()` اجرا می‌شود
- کاربرد: افکت‌های نهایی، آزادسازی حافظه، ذخیره آمار
- `destroy(entity, delay)`: entity را بعد از delay ثانیه نابود می‌کند

### مثال کامل: دکمه کنترل

```python
def toggle_lamp():
    lamp.enabled = not lamp.enabled
    status = "Activated" if lamp.enabled else "Deactivated"
    print(f"💡 Lamp status: {status}")

# دکمه فعال/غیرفعال کردن لامپ
button = Button(
    text='Activate/Deactivate Lamp',
    color=color.azure,
    scale=0.2,
    position=(0, -0.4)
)
button.on_click = toggle_lamp

# نمایش راهنما
info = Text(
    text="🖱️ Left Click: On/Off\n🖱️ Right Click: Destroy Lamp\n🔘 Bottom Button: Activate/Deactivate",
    position=(-0.85, -0.4),
    scale=1,
    origin=(-0.5, 0)
)

EditorCamera()  # دوربین قابل کنترل برای ناوبری در صحنه
```

- `EditorCamera()`: دوربینی که با کلیک راست و drag می‌توان صحنه را چرخاند
- `Button`: Entity از پیش ساخته شده با قابلیت‌های دکمه
- `Text`: نمایش متن روی صفحه (UI)

## خلاصه توابع و رویدادهای مهم

| رویداد/تابع | زمان اجرا | کاربرد |
|------------|----------|---------|
| `update()` | هر فریم | حرکت، انیمیشن، بررسی شرایط |
| `input(key)` | هنگام فشردن کلید | کنترل با صفحه کلید |
| `on_click` | یک بار کلیک | عملگرهای ساده |
| `on_double_click` | دو بار کلیک سریع | عملگرهای خاص |
| `on_mouse_enter` | ورود ماوس به محدوده | هایلایت، تغییر ظاهر |
| `on_mouse_exit` | خروج ماوس از محدوده | بازگردانی ظاهر |
| `on_enable()` | فعال شدن entity | راه‌اندازی مجدد |
| `on_disable()` | غیرفعال شدن entity | توقف، پاکسازی |
| `on_destroy()` | قبل از نابودی | افکت نهایی، ذخیره‌سازی |

## نکات مهم

1. **همیشه از time.dt در update استفاده کنید** تا حرکت مستقل از نرخ فریم باشد
2. **برای تشخیص hover و کلیک، collider ضروری است**
3. **از lambda برای توابع ساده و کوتاه استفاده کنید**
4. **ترتیب اجرا**: input → update → render
5. **EditorCamera() برای دیباگ و تست بسیار مفید است**

## اجرای برنامه

برای اجرای کدهای این بخش، تمام قطعات کد را در یک فایل Python قرار داده و اجرا کنید:

```bash
python filename.py
```

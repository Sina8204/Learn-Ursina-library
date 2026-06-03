## Mouse Collision چیست؟

Ursina به صورت خودکار یک **Raycast** از موس انجام میده و میتونه برخورد با Entity‌هایی که **collider** دارند رو تشخیص بده. این کار هم برای المان‌های UI و هم برای اشیاء سه بعدی صحنه کار میکنه.

## ویژگی‌های کلیدی Mouse Collision

### 1. **تشخیص خودکار**
موس به طور خودکار Raycast انجام میده و میتونه Entity‌هایی با collider رو تشخیص بده.

### 2. **المان‌های UI**
المان‌های UI (که به `camera.ui` والد شده‌اند) می‌تونن برخورد رو تشخیص بدن و **اشیاء پشت خودشون رو مسدود می‌کنن**.

## اطلاعات قابل دسترسی از طریق موس

```python
mouse.hovered_entity   # Entity که موس روش هست (یا None اگر هیچی نباشه)
mouse.normal           # نرمال چندضلعی برخورد خورده (فضای محلی)
mouse.world_normal     # نرمال چندضلعی برخورد خورده (فضای جهانی)
mouse.point            # نقطه برخورد (فضای محلی)
mouse.world_point      # نقطه برخورد (فضای جهانی)
```

## روش ساده: استفاده از on_click

ساده‌ترین راه برای مدیریت کلیک، اضافه کردن `collider` و `on_click` به Entity هست:

```python
def action():
    print('Ow! That hurt!')

# المان UI (دکمه)
Entity(
    model='quad', 
    parent=camera.ui,  # والد شدن به دوربین UI
    scale=.1, 
    collider='box', 
    on_click=action    # تابعی که هنگام کلیک صدا زده میشه
)
```

## مثال‌های کامل

### مثال 1: **اشیاء قابل کلیک در صحنه سه بعدی**

```python
from ursina import *

app = Ursina()

def on_click_button():
    print("دکمه کلیک شد!")
    button.color = color.lime

def on_click_enemy():
    print("به دشمن شلیک کردی!")
    enemy.color = color.red
    enemy.y -= 0.1

# دکمه در فضای سه بعدی
button = Entity(
    model='cube', 
    position=(2, 0, 2), 
    color=color.blue,
    collider='box',
    on_click=on_click_button
)

# دشمن قابل کلیک
enemy = Entity(
    model='sphere', 
    position=(-2, 0, 2), 
    color=color.orange,
    collider='sphere',
    on_click=on_click_enemy
)

# نمایش اطلاعات موس در کنسول
def update():
    if mouse.hovered_entity:
        print(f"روی: {mouse.hovered_entity}")
        print(f"نقطه برخورد: {mouse.world_point}")

EditorCamera()
app.run()
```

### مثال 2: **سیستم دکمه‌های UI**

```python
from ursina import *

app = Ursina()

def start_game():
    print("شروع بازی!")
    start_button.visible = False
    # کد شروع بازی...

def settings():
    print("تنظیمات باز شد")

def quit_game():
    print("خروج از بازی")
    application.quit()

# دکمه شروع
start_button = Entity(
    model='quad',
    parent=camera.ui,
    texture='white_cube',
    color=color.green,
    scale=(0.3, 0.1),
    position=(0, 0.2),
    collider='box',
    on_click=start_game
)

# متن روی دکمه
start_text = Text(
    text='شروع بازی',
    parent=start_button,
    origin=(0, 0),
    color=color.white
)

# دکمه تنظیمات
settings_button = Entity(
    model='quad',
    parent=camera.ui,
    color=color.blue,
    scale=(0.3, 0.1),
    position=(0, 0),
    collider='box',
    on_click=settings
)

settings_text = Text(
    text='تنظیمات',
    parent=settings_button,
    origin=(0, 0)
)

# دکمه خروج
quit_button = Entity(
    model='quad',
    parent=camera.ui,
    color=color.red,
    scale=(0.3, 0.1),
    position=(0, -0.2),
    collider='box',
    on_click=quit_game
)

quit_text = Text(
    text='خروج',
    parent=quit_button,
    origin=(0, 0)
)

app.run()
```

### مثال 3: **سیستم درگ و دریفت (Drag & Drop)**

```python
from ursina import *

app = Ursina()

dragging = False
drag_offset = Vec3(0, 0, 0)

def on_click_drag():
    global dragging, drag_offset
    dragging = True
    # محاسبه افست بین موس و مرکز شیء
    drag_offset = draggable.world_position - mouse.world_point

def on_release():
    global dragging
    dragging = False
    print("رها شد!")

def update():
    if dragging and mouse.world_point:
        # حرکت شیء با موس
        draggable.position = mouse.world_point + drag_offset

# شیء قابل درگ کردن
draggable = Entity(
    model='cube',
    color=color.yellow,
    scale=0.5,
    collider='box',
    on_click=on_click_drag,
    on_release=on_release
)

# نمایش موقعیت موس
info = Text(position=(-0.8, 0.4))

def update_info():
    if mouse.hovered_entity:
        info.text = f"روی: {mouse.hovered_entity.name if mouse.hovered_entity.name else 'شیء'}"
    else:
        info.text = "هیچی"

EditorCamera()
app.run()
```

### مثال 4: **سیستم هایلایت روی موس**

```python
from ursina import *

app = Ursina()

def on_hover():
    """وقتی موس روی شیء میره"""
    if mouse.hovered_entity:
        mouse.hovered_entity.original_color = mouse.hovered_entity.color
        mouse.hovered_entity.color = color.lime

def on_leave():
    """وقتی موس از روی شیء میره بیرون"""
    if hasattr(mouse.hovered_entity, 'original_color'):
        mouse.hovered_entity.color = mouse.hovered_entity.original_color

# چند شیء قابل کلیک
for i in range(5):
    box = Entity(
        model='cube',
        position=(i*1.5 - 3, 0, 0),
        color=color.random_color(),
        scale=0.8,
        collider='box',
        on_click=lambda x=i: print(f"جعبه {x} کلیک شد!"),
        on_mouse_enter=on_hover,
        on_mouse_exit=on_leave
    )

EditorCamera()
app.run()
```

## نکات مهم

### ✅ **کاربردهای Mouse Collision**

| کاربرد | توضیح |
|--------|-------|
| **دکمه‌های UI** | منوها، دکمه‌های شروع و تنظیمات |
| **انتخاب اشیاء** | انتخاب واحدها در بازی استراتژی |
| **سیستم هدفگیری** | شلیک به دشمنان در بازی‌های تیراندازی |
| **Drag & Drop** | جابجایی آیتم‌ها با موس |
| **Tooltips** | نمایش اطلاعات با هاور کردن |

### ⚠️ **نکات کلیدی**

1. **collider ضروری است**: Entity باید حتماً collider داشته باشه تا برخورد موس تشخیص داده بشه.

2. **UI مسدود کننده**: المان‌های UI (والد شده به `camera.ui`) اشیاء پشت خودشون رو می‌پوشونن و مسدود می‌کنن.

3. **on_click قابلیت‌ها**: میتونه باشه:
   - تابع (function)
   - آبجکت قابل صدا زدن (callable)
   - لیست توابع (Sequence)

4. **فاصله**: Raycast موس محدودیت فاصله نداره و هر چیزی با collider رو می‌تونه تشخیص بده.

## مثال پیشرفته: سیستم Target Practice

```python
from ursina import *
import random

app = Ursina()

score = 0
score_text = Text(text=f'Score: {score}', position=(-0.85, 0.45))

def hit_target():
    global score
    score += 1
    score_text.text = f'Score: {score}'
    print(f"هدف زده شد! امتیاز: {score}")
    
    # جابجایی هدف به مکان تصادفی
    target.x = random.uniform(-5, 5)
    target.z = random.uniform(-5, 5)
    target.color = color.random_color()

# هدف متحرک
target = Entity(
    model='sphere',
    color=color.red,
    scale=0.5,
    collider='sphere',
    on_click=hit_target
)

# نشانگر موس
cursor = Entity(model='quad', scale=0.05, color=color.white, parent=camera.ui)
mouse.visible = False

def update():
    # حرکت نشانگر با موس
    cursor.position = mouse.position
    
    # حرکت هدف به صورت دایره‌ای
    target.x = 3 * math.sin(time.time())
    target.z = 3 * math.cos(time.time() * 0.7)

EditorCamera()
app.run()
```

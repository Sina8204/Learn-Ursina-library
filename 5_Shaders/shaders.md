## آموزش مبحث Shader ها در پکیج Ursina

در Ursina، از Shader ها برای کنترل دقیق نحوه渲染 (رندر) اشیا استفاده می‌شود. با Shader می‌توانید جلوه‌های نوری، سایه، بافت‌های پیشرفته مانند Normal Map و حتی افکت‌های کاملاً سفارشی را به بازی خود اضافه کنید. در ادامه با نحوه استفاده از Shaderهای داخلی و نوشتن Shader سفارشی آشنا می‌شوید.

### ۱. استفاده از Shader های داخلی (Built-in Shaders)

ساده‌ترین راه برای شروع، استفاده از Shaderهای از پیش ساخته شده‌ای است که در Ursina وجود دارند. این Shaderها برای رایج‌ترین نیازها طراحی شده‌اند.

#### یک مثال کامل و کاربردی

فرض کنید می‌خواهید یک مکعب و یک صفحه ساده داشته باشید که نور و سایه روی آنها اعمال شود. کد زیر را ببینید :

```python
from ursina import *
from ursina.shaders import lit_with_shadows_shader  # Shader مورد نظر را ایمپورت کنید

app = Ursina()

# یک دوربین برای حرکت راحت در صحنه
EditorCamera()

# ایجاد صفحه (زمین) با Shader سایه‌دار
ground = Entity(model='plane', scale=10, color=color.gray, shader=lit_with_shadows_shader)

# ایجاد مکعب با Shader سایه‌دار
cube = Entity(model='cube', y=1, shader=lit_with_shadows_shader)

# ایجاد یک نور جهت‌دار برای ایجاد سایه
pivot = Entity()
DirectionalLight(parent=pivot, y=2, z=3, shadows=True, rotation=(45, -45, 45))

app.run()
```
در این مثال:
- Shader مربوط به نور و سایه (`lit_with_shadows_shader`) را به دو شیء اعمال کرده‌ایم.
- یک `DirectionalLight` شبیه‌سازی کننده نور خورشید ایجاد کرده‌ایم که سایه‌ها را فعال می‌کند.

#### Shaderهای داخلی مهم

علاوه بر Shader بالا، Ursina Shaderهای دیگری هم دارد که هر کدام برای هدف خاصی هستند :

| نام Shader | کاربرد |
| :--- | :--- |
| `basic_lighting_shader` | یک Shader نوری ساده بدون سایه. برای اجرای سریع و سبک مناسب است . |
| `lit_with_shadows_shader` | Shader کامل با پشتیبانی از سایه. برای صحنه‌های واقع‌گرایانه . |
| `normals_shader` | برای استفاده از **نقشه‌ی نرمال** (Normal Map) به کار می‌رود تا جزئیات بافت‌ها را بیشتر نشان دهد . |
| `fxaa_shader` | یک Shader برای **ضدآلیاسینگ** (نرم‌سازی لبه‌های تصویر) که می‌توان آن را به دوربین اعمال کرد . |

#### تنظیم Shader پیش‌فرض برای تمام اشیا

اگر می‌خواهید همه‌ی اشیاء جدید به‌طور خودکار از یک Shader خاص استفاده کنند، می‌توانید آن را به‌صورت سراسری تنظیم کنید :

```python
from ursina.shaders import basic_lighting_shader
Entity.default_shader = basic_lighting_shader
```

### ۲. کار با Normal Map (نقشه‌ی نرمال)

برای اینکه بافت‌هایتان سه‌بعدی‌تر و دارای جزئیات به نظر برسند، می‌توانید از `normals_shader` استفاده کنید :

```python
from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()

# ایجاد یک شیء با بافت و نقشه‌ی نرمال
model = Entity(model='cube', texture='brick')
model.normal_map = 'brick_normal'  # مسیر فایل Normal Map
model.shader = 'normals_shader'    # اعمال Shader مخصوص

# تنظیم شدت اثر نقشه‌ی نرمال
model.shader.i_channel0_intensity = 2.0

player = FirstPersonController()
app.run()
```

### ۳. نوشتن Shader سفارشی

اگر Shaderهای داخلی نیاز شما را برآورده نمی‌کنند، می‌توانید Shaderهای اختصاصی خود را با استفاده از زبان GLSL بنویسید. از آنجایی که Ursina بر پایه‌ی Panda3D ساخته شده است، باید از قواعد آن پیروی کنید .

#### مراحل نوشتن Shader سفارشی

**قدم اول: ایجاد فایل‌های Shader**

دو فایل جداگانه برای Vertex Shader و Fragment Shader ایجاد کنید. توجه داشته باشید که Panda3D پسوندهای خاصی را انتظار دارد. بهتر است از پسوندهای `.vert` و `.frag` استفاده کنید تا با خطا مواجه نشوید .

**قدم دوم: بارگذاری و اعمال Shader**

در کد پایتون، Shader را بارگذاری و به شیء مورد نظر اعمال کنید :

```python
from ursina import *

app = Ursina()

# بارگذاری Shader سفارشی از فایل‌ها
my_shader = Shader(Shader.GLSL,
                   vertex="my_vertex_shader.vert",   # نام فایل Vertex Shader
                   fragment="my_fragment_shader.frag") # نام فایل Fragment Shader

# اعمال Shader به یک شیء
my_entity = Entity(model='sphere', shader=my_shader)

app.run()
```
> **نکته مهم:** اگر هنگام اجرا با خطای `GLSL shader created-shader does not contain a #version line!` مواجه شدید، مطمئن شوید که در اولین خط فایل‌های Shader خود (`my_vertex_shader.vert` و `my_fragment_shader.frag`) دستور `#version 150` یا نسخه‌ی مناسب دیگر را نوشته باشید و از پسوندهای `.vert` و `.frag` استفاده کنید .

### جمع‌بندی

استفاده از Shaderها در Ursina به شما امکان می‌دهد تا از یک بازی ساده، به یک تجربه‌ی بصری غنی و حرفه‌ای برسید. با Shaderهای داخلی به‌راحتی می‌توان نور، سایه و بافت‌های پیشرفته را اضافه کرد و در صورت نیاز، با یادگیری GLSL می‌توان افکت‌های کاملاً جدید و منحصربه‌فردی خلق کرد.

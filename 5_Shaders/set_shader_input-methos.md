## تابع `set_shader_input` در Ursina چیست؟

تابع `set_shader_input` یک متد قدرتمند در Ursina (و Panda3D) است که به شما اجازه می‌دهد **متغیرهای سفارشی را از سمت پایتون به Shader ارسال کنید**. این متغیرها در Shader به عنوان `uniform` در دسترس خواهند بود و می‌توانید مقادیر آنها را در حین اجرای برنامه تغییر دهید.

---

### نحوه عملکرد در کد شما

در کد ارائه شده، شما از `set_shader_input` برای ارسال ماتریس تبدیل (Transform Matrix) شیء به Shader استفاده کرده‌اید:

```python
b.set_shader_input('transform_matrix', b.getNetTransform().getMat())
```

**این خط چه کاری انجام می‌دهد؟**

1. **`'transform_matrix'`** : نام متغیر `uniform` در Shader است که مقدار به آن ارسال می‌شود.
2. **`b.getNetTransform().getMat()`** : ماتریس تبدیل نهایی شیء (شامل موقعیت، چرخش و مقیاس) را محاسبه و به عنوان یک ماتریس ۴×۴ به Shader ارسال می‌کند.

اگر به کد Shader دقت کنید، این متغیر در هیچ کجای Vertex یا Fragment Shader تعریف نشده است! یعنی **این Shader در حال حاضر از این متغیر استفاده نمی‌کند** و کد فقط برای نمایش نحوه ارسال داده نوشته شده است.

---

### کاربردهای مهم `set_shader_input`

#### ۱. **ارسال داده‌های پویا به Shader**

می‌توانید هر نوع داده‌ای را به Shader بفرستید:

```python
# ارسال عدد
entity.set_shader_input('time', time.time())

# ارسال بردار
entity.set_shader_input('light_direction', Vec3(1, 2, 3))

# ارسال رنگ
entity.set_shader_input('custom_color', Vec4(1, 0.5, 0, 1))

# ارسال ماتریس
entity.set_shader_input('model_matrix', entity.getNetTransform().getMat())
```

#### ۲. **ایجاد افکت‌های پویا**

با به‌روزرسانی متغیرها در حلقه `update()` می‌توانید افکت‌های متحرک بسازید:

```python
def update():
    # ارسال زمان به Shader برای ایجاد موج
    entity.set_shader_input('time', time.time())
    
    # ارسال موقعیت نور به صورت پویا
    entity.set_shader_input('light_pos', mouse.world_position)
```

#### ۳. **دریافت داده در Shader**

برای استفاده از داده‌های ارسال شده، باید آنها را در Shader به عنوان `uniform` تعریف کنید:

```glsl
// در Vertex یا Fragment Shader
uniform float time;
uniform vec3 light_direction;
uniform vec4 custom_color;
uniform mat4 model_matrix;
```

---

### مثال کامل استفاده از `set_shader_input`

فرض کنید می‌خواهیم یک افکت موج‌دار روی یک صفحه ایجاد کنیم:

**کد پایتون:**
```python
from ursina import *

app = Ursina()

# Shader سفارشی با پشتیبانی از زمان
wave_shader = Shader(
    vertex='''
    #version 140
    uniform mat4 p3d_ModelViewProjectionMatrix;
    uniform float time;  // متغیر سفارشی
    in vec4 p3d_Vertex;
    in vec2 p3d_MultiTexCoord0;
    out vec2 texcoord;
    
    void main() {
        vec3 pos = p3d_Vertex.xyz;
        // ایجاد موج با استفاده از زمان
        pos.y += sin(pos.x * 2.0 + time) * 0.2;
        gl_Position = p3d_ModelViewProjectionMatrix * vec4(pos, 1.0);
        texcoord = p3d_MultiTexCoord0;
    }
    ''',
    fragment='''
    #version 140
    uniform sampler2D p3d_Texture0;
    in vec2 texcoord;
    out vec4 fragColor;
    
    void main() {
        fragColor = texture(p3d_Texture0, texcoord);
    }
    '''
)

# ایجاد صفحه با Shader موج‌دار
plane = Entity(model='plane', scale=5, texture='white_cube', shader=wave_shader)

# ارسال زمان به Shader در هر فریم
def update():
    plane.set_shader_input('time', time.time())

EditorCamera()
app.run()
```

---

### نکات کلیدی

| ویژگی | توضیح |
|-------|-------|
| **نام متغیر** | باید با نام `uniform` در Shader مطابقت داشته باشد |
| **نوع داده** | می‌توانید `int`، `float`، `Vec2`، `Vec3`، `Vec4`، `Mat4` و ... ارسال کنید |
| **به‌روزرسانی** | برای تغییر مقدار، کافی است دوباره `set_shader_input` را صدا بزنید |
| **عملکرد** | ارسال داده در هر فریم ممکن است سنگین باشد، پس فقط در صورت نیاز انجام دهید |

---

### رفع مشکل کد شما

در کد فعلی، `transform_matrix` به Shader ارسال می‌شود اما استفاده نمی‌شود. اگر می‌خواهید از آن استفاده کنید، باید در Shader تعریفش کنید:

```glsl
uniform mat4 transform_matrix;
```

سپس می‌توانید از آن برای تبدیل‌های دستی استفاده کنید:

```glsl
gl_Position = p3d_ModelViewProjectionMatrix * transform_matrix * p3d_Vertex;
```

---

### جمع‌بندی

`set_shader_input` پلی بین پایتون و Shader است که به شما امکان می‌دهد:
- داده‌های پویا را به Shader ارسال کنید
- افکت‌های متحرک و تعاملی ایجاد کنید
- پارامترهای Shader را در زمان اجرا تغییر دهید
- کنترل کامل بر روی ظاهر اشیا داشته باشید

این تابع یکی از ابزارهای کلیدی برای ایجاد جلوه‌های بصری پیشرفته در Ursina محسوب می‌شود.

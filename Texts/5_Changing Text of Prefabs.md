**Changing Text of Prefabs** در Ursina به این صورت عمل می‌کند:

## دسترسی به text_entity در Prefabها

اشیاء آماده (Prefab) مانند **Slider**، **InputField** و دیگر موارد معمولاً دارای یک attribute به نام **`.text_entity`** هستند که می‌توانید در صورت نیاز به آن دسترسی پیدا کنید.

## مثال‌های عملی

### 1. تغییر متن Slider:
```python
slider = Slider(text='Volume', min=0, max=100)
slider.text_entity.text = 'Sound Level'  # تغییر متن راهنما
# یا
slider.text_entity.world_scale = 1.5  # تغییر سایز متن
```

### 2. تغییر متن InputField:
```python
input_field = InputField(text='Enter your name')
input_field.text_entity.text = 'نام خود را وارد کنید'  # تغییر متن پیش‌فرض
input_field.text_entity.color = color.blue  # حتی می‌توانید رنگ را هم تغییر دهید
```

### 3. تغییر سایز متن در Prefabها:
```python
button = Button(text='Click Me')
button.text_entity.world_scale = 2  # دو برابر کردن سایز متن دکمه

slider = Slider(text='Volume')
slider.text_entity.scale = (0.5, 0.5)  # تغییر مقیاس متن اسلایدر
```

## نکات مهم:

✅ **چه Prefabهایی text_entity دارند؟**  
مواردی مثل:
- Button
- Slider  
- InputField
- و سایر Prefabهایی که متن نمایش می‌دهند

✅ **با text_entity چه کارهایی می‌توان کرد؟**  
از آنجایی که `text_entity` یک شیء از نوع **Text** است، می‌توانید تمام ویژگی‌های معمول Text را روی آن اعمال کنید:
- تغییر `.text` (متن)
- تغییر `.world_scale` (سایز)
- تغییر `.color` (رنگ)
- تغییر `.font` (فونت)
- و ...

✅ **مثال ترکیبی:**
```python
slider = Slider(text='Speed', min=0, max=100)
slider.text_entity.text = 'سرعت'  # تغییر به فارسی
slider.text_entity.world_scale = 1.2  # بزرگتر کردن
slider.text_entity.color = color.orange  # تغییر رنگ
slider.text_entity.font = 'VeraMono.ttf'  # تغییر فونت
```

💡 **نکته کاربردی:** همیشه از `.text_entity` برای دسترسی و تغییر متن و خصوصیات آن در Prefabها استفاده کنید، نه اینکه مستقیماً سعی کنید متن را تغییر دهید!

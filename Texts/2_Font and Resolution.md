## Font (قلم یا فونت)

### ۱. برای یک Text Entity خاص:
```python
text = Text(font='VeraMono.ttf', resolution=100*Text.size)
text.text = "توضیحات شما"
```
با این کار فقط فونت همان متن خاص تغییر می‌کند.

### ۲. برای تمام Text Entityها (سراسری):
```python
Text.default_font = 'VeraMono.ttf'
```
با این کار همه متون پروژه از این فونت استفاده می‌کنند مگر اینکه برای یک متن خاص فونت دیگری تعیین کنید.

## Resolution (رزولوشن یا وضوح)

### ۱. برای یک Text Entity خاص:
```python
text = Text(font='VeraMono.ttf', resolution=100*Text.size)
```

### ۲. برای تمام Text Entityها (سراسری):
```python
Text.default_resolution = 100 * Text.size
```

## نکات مهم:

✅ **آیا همیشه نیاز به تغییر رزولوشن دارید؟**  
خیر، همیشه لازم نیست. اما برای **فونت‌های پیکسلی** (مثل فونت‌های بازی‌های قدیمی)، رزولوشن بالاتر باعث می‌شود متن **تار (blurry)** به نظر نرسد.

✅ **رابطه رزولوشن و سایز:**  
در مثال‌ها می‌بینید که رزولوشن بر اساس `Text.size` محاسبه می‌شود:
```python
resolution=100 * Text.size
```

✅ **مثال کامل:**
```python
# تنظیم سراسری
Text.default_font = 'VeraMono.ttf'
Text.default_resolution = 100 * Text.size

# یا برای یک متن خاص
pixel_text = Text(font='pixel_font.ttf', resolution=200 * Text.size)
```

💡 **نکته کاربردی:** اگر متن‌های پیکسلی شما تار می‌شوند، رزولوشن را افزایش دهید تا شارپ و شفاف شوند.

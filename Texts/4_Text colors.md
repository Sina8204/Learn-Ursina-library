**Text Colors** در Ursina دو روش اصلی برای رنگ‌آمیزی متن دارد:

## ۱. رنگ‌آمیزی کل متن (Whole Text)

با استفاده از پارامتر `color` می‌توانید کل متن را یکدست رنگ کنید:

```python
t = Text('This is some text', color=color.blue)
```
این کار باعث می‌شود تمام متن به رنگ آبی نمایش داده شود.

## ۲. رنگ‌آمیزی بخش‌هایی از متن (Using Tags)

با استفاده از **تگ‌ها (tags)** می‌توانید بخش‌های مختلف متن را به رنگ‌های متفاوت درآورید:

```python
t = Text('This is some <pink>colored text. <default>Reset color back to default.', color=color.blue)
```

### نحوه عملکرد تگ‌ها:

- **`<رنگ>`** : از این نقطه به بعد، متن به آن رنگ تغییر می‌کند
- **`<default>`** : رنگ را به حالت پیش‌فرض (که در ابتدا با `color` تعیین شده) برمی‌گرداند

### مثال کاربردی:

```python
# کل متن آبی می‌شود
text1 = Text('Hello World', color=color.blue)

# ترکیب رنگ‌ها: قرمز و سبز و سپس بازگشت به آبی
text2 = Text('This is <red>red<default> and this is <green>green<default> back to blue.', 
             color=color.blue)

# می‌توانید از هر رنگی که در Ursina تعریف شده استفاده کنید
text3 = Text('Rainbow: <red>R<orange>a<yellow>i<green>n<blue>b<purple>o<default>w', 
             color=color.white)
```

### رنگ‌های رایج در Ursina:
- `color.red`
- `color.green`
- `color.blue`
- `color.yellow`
- `color.pink`
- `color.purple`
- `color.orange`
- `color.white`
- `color.black`
- `color.default`

💡 **نکته مهم:** اگر از `color` برای کل متن استفاده کنید و همزمان از تگ‌ها هم استفاده کنید، متن ابتدا به رنگ کلی درمی‌آید و سپس تگ‌ها رنگ قسمت‌های مشخص شده را تغییر می‌دهند. تگ `<default>` رنگ را به همان رنگ اولیه (که با `color` تنظیم شده) برمی‌گرداند.

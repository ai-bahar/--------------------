from transformers import pipeline
from transformers import pipeline

from transformers import pipeline

ner = pipeline(
    "ner",
    model="./مدل_من",
    tokenizer="./مدل_من",
    use_fast=False,
    aggregation_strategy="simple"
)
FEATURE_MAP = {
    "رم": "رم",
    "قیمت": "قیمت",
    "وزن": "وزن",
    "باتری": "باتری",
    "صفحه": "صفحه_نمایش",
    "سی‌ پی‌ یو": "سی_پی_یو",
    "جی‌ پی‌ یو": "جی_پی_یو",
    "حافظه": "حافظه"
}

def استخراج_نام_محصول(متن, نام‌های_شناخته_شده):
    """
    ورودی:
      متن → جمله کاربر
      نام‌های_شناخته_شده → لیست همه لپ‌تاپ‌ها از دیتابیس (تابع همه_نام_ها در db.py)

    خروجی:
      لیست حداکثر دو نام لپ‌تاپ که در متن کاربر پیدا شده
    """
    entities = ner(متن)

    found = {e['word'].strip() for e in entities}

    for name in نام‌های_شناخته_شده:
        if name in متن:
            found.add(name)

    return list(found)[:2]
    
def استخراج_ویژگی(متن):
    for k, v in FEATURE_MAP.items():
        if k in متن:
            return v
    return None

    
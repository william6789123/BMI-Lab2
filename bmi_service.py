import math


def bmi_guidance(bmi):
    if bmi < 18.5:
        return {
            "label": "體重過輕",
            "tone": "low",
            "advice": "留意是否攝取足夠且均衡的營養，規律進食並搭配適度肌力活動；若體重持續下降，建議諮詢醫師或營養師。",
        }
    if bmi < 24:
        return {
            "label": "健康體位",
            "tone": "healthy",
            "advice": "維持均衡飲食與規律運動，並持續留意睡眠及生活習慣，幫助保持健康體位。",
        }
    if bmi < 27:
        return {
            "label": "體重過重",
            "tone": "high",
            "advice": "可從減少含糖飲料、增加蔬菜與日常活動量開始，循序建立適合自己的健康習慣。",
        }
    return {
        "label": "肥胖",
        "tone": "high",
        "advice": "建議與醫師或營養師討論適合自己的飲食及運動計畫，並留意血壓、血糖等健康指標。",
    }


def military_service_status(bmi):
    if bmi < 18.5 or bmi >= 27:
        return {
            "service_label": "需進一步評估",
            "service_status": "BMI 偏離常見範圍，建議依照體檢與醫療評估結果再確認是否適合服役。",
        }
    return {
        "service_label": "可列入兵役評估",
        "service_status": "BMI 在常見範圍內，應可依正式體檢標準進一步判定是否適合服役。",
    }


def parse_positive_number(value):
    try:
        number = float(value)
    except (TypeError, ValueError):
        return None
    return number if math.isfinite(number) and number > 0 else None


def calculate_bmi(height, weight):
    height_meters = height / 100
    height_squared = height_meters * height_meters
    if not math.isfinite(height_squared) or height_squared == 0:
        return None

    bmi = weight / height_squared
    return bmi if math.isfinite(bmi) and bmi != 0 else None

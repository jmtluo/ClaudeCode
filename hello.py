import sys
from datetime import datetime, timezone, timedelta

sys.stdout.reconfigure(encoding="utf-8")

TZ_GMT8 = timezone(timedelta(hours=8))

print("哈囉，世界！")
print(f"目前時間（GMT+8）：{datetime.now(TZ_GMT8).strftime('%Y-%m-%d %H:%M:%S %Z')}")
print("Claude 祝你今天愉快！")

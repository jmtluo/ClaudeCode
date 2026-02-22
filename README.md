# ClaudeCode

這是一個使用 Python 撰寫的 Hello World 範例專案，由 Claude AI 協助開發。

## 專案說明

本專案示範如何使用 Python 輸出問候語，並顯示目前的 GMT+8 時區時間。

## 環境需求

- Python 3.8 以上版本

## 使用方式

```bash
python hello.py
```

### 輸出範例

```
哈囉，世界！
目前時間（GMT+8）：2026-02-23 01:10:03 UTC+08:00
Claude 祝你今天愉快！
```

## hello.py 說明

### 程式碼結構

| 行數 | 說明 |
|------|------|
| 1 | 匯入 `sys` 模組，用於設定輸出編碼 |
| 2 | 匯入 `datetime`、`timezone`、`timedelta`，用於處理時間與時區 |
| 4 | 將標準輸出設為 UTF-8，確保中文在 Windows 正常顯示 |
| 6 | 定義 GMT+8 時區（台灣／香港／中國標準時間） |
| 8 | 輸出問候語「哈囉，世界！」 |
| 9 | 取得目前 GMT+8 時間並格式化輸出 |
| 10 | 輸出祝福語 |

### 使用模組

- **`sys`** — 設定 stdout 編碼為 UTF-8，解決 Windows 中文亂碼問題
- **`datetime`** — 取得當下時間
- **`timezone` / `timedelta`** — 指定 GMT+8 時區，不依賴系統時區設定

## 作者

- **jmtluo** — [GitHub](https://github.com/jmtluo)

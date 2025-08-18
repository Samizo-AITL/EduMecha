---
title: "Part Numbering System"
---

# 🔢 部品コード体系 | Part Numbering System  
**Part Numbering Rules**

---

## 🏗 基本構造 | Basic Structure

```
ABCDEF-XX
```

- **ABCDEF（6桁 / 6 digits）**  
  → 部品アイデンティティ / **Part identity**  
  → 「何の部品か」を一意に示す / Defines *what the part is*.  

- **-XX（枝番 / Suffix）**  
  → 条件差・改訂履歴 / **Version or condition difference**  
  → 製造条件やバージョン管理に使用 / Tracks revisions, molds, factories.  

---

## 📊 第1桁カテゴリ | 1st Digit Categories

| **1桁目 / Digit** | **意味 / Meaning** | **例 / Examples** |
|------------------|--------------------|------------------|
| **1** | 機械部品 / Mechanical Parts | ネジ, ギア, 筐体 / Screws, gears, housings |
| **2** | 電子部品 / Electronic Parts | 抵抗, IC, コンデンサ / Resistors, ICs, capacitors |
| **6** | 材料 / Materials | 樹脂, 接着剤, 溶剤 / Resin, adhesives, solvents |
| **9** | 治具・工具 / Jigs & Tools | 組立治具, 測定治具 / Assembly & measurement jigs |

🔎 **ポイント | Notes**  
- 1桁目でカテゴリ分類することで検索・集計が容易。  
  *Easy classification & search by first digit.*  
- **「6番＝材料 / Materials」** は規制対応必須（SDS・消防法・環境規制）。  
  *Digit 6 (Materials) requires strict compliance with SDS, Fire Law, and environmental regulations.*  

---

## 🏷 枝番ルール | Suffix Rules

| **枝番 / Suffix** | **意味 / Meaning** | **適用例 / Examples** |
|-------------------|--------------------|------------------------|
| **-01, -02** | バージョンアップ / Version update | メッキ厚変更、寸法公差修正 / Plating thickness change, tolerance adjustment |
| **-11, -21** | 金型違い / Different mold | 同一部品を複数金型で製造 / Produced with multiple molds |
| **-51, -52** | 製造地違い / Different factory | 生産工場ごとの区別 / Different production sites |
| **-99** | 暫定・特採 / Temporary or special approval | 正式承認前の利用 / Pre-approval or special adoption |

👉 **機能が変わる場合は新しい6桁コードを発行**  
*If the **function changes**, a **new 6-digit part code** must be issued.*  

---

## 💡 解説ポイント | Key Insights

1. **6桁コード = 機能アイデンティティ / Functional Identity**  
   - 図面・仕様と必ずリンク / Always linked with drawings & specs.  
   - 機能が変わらない限り同じ6桁を維持 / 6-digit stays the same unless function changes.  

2. **枝番 = 改版・条件管理 / Revision & Condition Tracking**  
   - 軽微な変更や製造条件差を記録 / Records minor changes, mold, or site differences.  
   - トレーサビリティ確保に必須 / Critical for traceability.  

3. **材料コードは特別扱い / Materials Need Special Handling**  
   - 環境法規制（RoHS/REACH）、消防法、輸出規制に直結 / Directly tied to RoHS/REACH, Fire Law, export control.  
   - **SDS & 環境データをセット登録 / Register with SDS & environmental data together.**  

---

✅ **このルールを徹底することで | By following these rules:**  
- 設計変更の影響範囲を迅速に判断  
  *Quickly assess impact of design changes*  
- 製造・環境・輸出管理との整合性を確保  
  *Ensure consistency with manufacturing, environmental, and export controls*  
- トレーサビリティを担保し、監査にも耐えられる体系を実現  
  *Maintain traceability and withstand audits*  

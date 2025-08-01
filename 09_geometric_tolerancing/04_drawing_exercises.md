# 04_drawing_exercises.md

## 📝 幾何公差の演習課題 / GD&T Drawing Exercises

本章では、**幾何公差（GD&T）に関する演習課題**を通じて、設計意図の明示、図面記述力、基準面設定の理解を深めます。Creoによる注記演習や、手書き図面形式での演習も含まれます。

This section provides **practical exercises on GD&T**, focusing on design intent, drawing annotations, and datum system understanding. Tasks include Creo annotation practices and paper-based drawing exercises.

---

## 🎯 目的 / Objectives

- 幾何特性記号を適切に用いる力を養う  
- 組立・測定を意識した基準面の選定スキルを得る  
- CAD操作と連動したGD&T記述能力を育てる

---

## 🧪 基本課題（レベル1）/ Basic Exercises (Level 1)

### ✍️ 課題1：平面度の記入

- 以下のプレート部品に対し、下面に **平面度 0.05** を付加してください。

```
[図面略図：矩形プレート、下面にGTOL Ⓕ|0.05 を追加する想定]
```

- 回答例：
  ```
  ┌──────┐
  │ Ⓕ | 0.05 │
  └──────┘
     ↑
     └── 下側面を指す
  ```

---

### ✍️ 課題2：直角度の記入

- 側面Aを基準として、上面Bに **直角度 0.1 A基準** を指示してください。

- 回答例：
  ```
  ┌────────────┐
  │ ⊥ | 0.1 | A │
  └────────────┘
  ```

---

## ⚙️ 中級課題（レベル2）/ Intermediate Exercises (Level 2)

### ✍️ 課題3：位置度＋複数基準

- φ10の穴に対して、**位置度 0.2**, MMC, 基準A/Bを用いたGD&Tを追加せよ。

- 回答例：
  ```
  ┌────────────────────┐
  │ Ⓜ | 0.2 | M | A | B │
  └────────────────────┘
  ```

- 補足：基準Aは下面、Bは左側面を想定

---

### ✍️ 課題4：対称度の適用

- 2つの側面間の対称性を示すため、**対称度 0.1, 基準C** を記述せよ。

- 回答例：
  ```
  ┌────────────┐
  │ ⌖ | 0.1 | C │
  └────────────┘
  ```

---

## 🧠 応用課題（レベル3）/ Advanced Exercises (Level 3)

### ✍️ 課題5：3DモデルへのGD&T付与（MBD対応）

- 添付されたCreoモデル `gtol_sample.prt` を用い、以下を3D注記してください：
  - 平面度 0.03（上面）
  - 位置度 0.15（穴、基準A/B）
  - 円周振れ 0.05（回転軸）

- 実行後、3D PDFとして保存し、アノテーションステートも確認。

---

## 🧩 課題データ / Exercise Files

| ファイル名 | 内容 |
|------------|------|
| `gtol_sample.prt` | Creo演習用サンプル部品（3D） |
| `gtol_drawing.drw` | 2D図面テンプレート付き |
| `answers.pdf` | 回答例一覧（オプション） |

---

## 📘 関連章 / Related Sections

- `01_gdt_basics.md`：GD&T記号と定義の確認
- `03_creo_examples.md`：注記方法の手順確認
- `05_measurement_and_inspection.md`：公差と検査手法の連動

---

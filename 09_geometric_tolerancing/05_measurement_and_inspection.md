# 05_measurement_and_inspection.md

## 🔍 幾何公差の検査と測定 / Measurement and Inspection of GD&T

本章では、幾何公差（GD&T）に関する**検査手法・測定機器・トレーサビリティ管理**について解説します。設計で定義された幾何特性を**現実の製造現場でどのように評価するか**を理解することが目的です。

This chapter explains **inspection methods, measurement tools, and traceability** for Geometric Dimensioning and Tolerancing (GD&T). The goal is to understand how specified geometric features are practically verified in manufacturing.

---

## 🧪 測定対象ごとの代表的手法 / Typical Measurement Methods by GD&T Type

| 幾何特性 / GD&T Type | 測定手法 / Measurement Method | 備考 / Remarks |
|----------------------|------------------------------|----------------|
| 平面度 Flatness | 表面プレート＋ダイヤルゲージ<br>3Dスキャナ / CMM | サブミクロン精度ならCMM |
| 真直度 Straightness | マイクロメータ＋Vブロック<br>光学プロファイラ | 細軸形状に有効 |
| 直角度 Perpendicularity | マスタースクエア＋ゲージ<br>CMM三次元測定機 | 基準面との直交度評価 |
| 位置度 Position | CMM or デジタル投影機 | MMC使用時は注意 |
| 同軸度 Concentricity | 回転＋ダイヤルゲージ<br>非接触センサ | 振れとの違いに注意 |
| 振れ Runout / Total Runout | 回転ステージ＋接触プローブ | 回転中心との相関が重要 |

---

## 🧰 主な測定機器 / Main Equipment

| 測定機器 / Equipment | 用途 / Usage |
|----------------------|--------------|
| CMM（三次元測定機） | 座標による幾何的特徴の測定、GD&Tに最も対応可能 |
| ダイヤルゲージ | 基本的な偏差測定、回転測定との組み合わせで活用 |
| サーフテスト / 表面粗さ計 | 平面度、真直度、粗さ評価 |
| デジタルプロジェクタ / 測定顕微鏡 | 小型部品の精密位置度測定 |
| 3Dレーザースキャナ / ホワイトライト | 複雑形状の非接触全体測定（面分布） |

---

## 🧩 公差評価とトレーサビリティ / Tolerance Verification and Traceability

### ✅ トレーサビリティとは？

- 測定機器の校正履歴や基準の**国家標準への系統的接続**
- 設計値 ⇄ 測定値 の**信頼性と再現性の保証**
- ISO 9001 / IATF 16949 における**品質管理の必須要件**

### ✅ 測定結果の管理項目

- 測定者 / 測定機器番号  
- 測定日時 / 環境条件（温度・湿度）  
- 基準点設定 / ゼロ補正の有無  
- NG判定時の対応フロー（再測定／不適合処理）

---

## 📘 測定レポート例 / Example Inspection Report

```
部品番号：ABC1234
検査項目：位置度 Ⓜ | 0.2 | M | A | B
測定値（5点）：0.12 / 0.15 / 0.19 / 0.16 / 0.18 mm
判定：OK
測定機器：Mitutoyo CMM CRYSTA-Apex V544
校正日：2025-04-10
測定者：T.Suzuki
```

---

## 🧠 教育的ポイント / Educational Notes

- 「測定できない公差」は**設計不良**とみなされる  
- 公差と測定機能は**セットで理解することが必須**
- CMMのプログラミングやフィーチャー定義は設計意図の反映に直結

---

## 🔗 関連ファイル / Related Resources

- `01_gdt_basics.md`：幾何公差記号の定義  
- `03_creo_examples.md`：CADによる公差指定  
- `04_drawing_exercises.md`：設計⇄検査の連動演習  
- ISO/IEC 17025：試験所・校正機関の能力に関する一般要求事項

---

# 01_gdt_basics.md

## 📘 幾何公差の基本定義 / Basics of Geometric Dimensioning and Tolerancing (GD&T)

本章では、**幾何公差（GD&T: Geometric Dimensioning and Tolerancing）**の基本的な記号、意味、使い方を紹介します。各幾何特性は、寸法公差だけでは不十分な形状・位置・姿勢の要件を明確にするために用いられます。

This chapter introduces the basic **symbols, meanings, and usage** of GD&T. These geometric characteristics define form, orientation, location, and runout requirements that dimensional tolerances alone cannot adequately describe.

---

## 🧭 公差の分類 / Types of Geometric Tolerances

| カテゴリ / Category | 内容 / Description | 使用記号 / Symbol |
|---------------------|--------------------|-------------------|
| 形状公差 / Form | 個々の形状のみに適用 | Ⓕ Flatness<br>Ⓒ Straightness<br>⓴ Roundness<br>⌭ Cylindricity |
| 姿勢公差 / Orientation | 基準に対する方向 | ⊥ Perpendicularity<br>∠ Parallelism<br>∠ Angularity |
| 位置公差 / Location | 基準に対する位置 | Ⓜ Position<br>⊕ Concentricity<br>⌖ Symmetry |
| 振れ公差 / Runout | 回転要素の変動 | ⌰ Circular Runout<br>⌰⌰ Total Runout |

---

## 🧩 幾何公差の要素構成 / GD&T Feature Structure

幾何公差の指示は、以下のような **公差枠（Feature Control Frame）** によって行います：

```
| 幾何特性記号 | 公差値 | 基準情報（必要に応じて） |
```

例（位置度）:

```
| Ⓜ | 0.1 | A | B | C |
```

- Ⓜ（位置度）：位置に関する公差  
- 0.1：許容される最大変位量  
- A, B, C：基準となるフィーチャー

---

## 📐 代表的な記号一覧 / Common GD&T Symbols

| 記号 | 意味（日本語） | 英語名称 | 用途例 |
|------|----------------|-----------|--------|
| Ⓒ | 真直度 | Straightness | シャフトの軸方向の歪み抑制 |
| Ⓕ | 平面度 | Flatness | 接地面や嵌合面の平坦さ確保 |
| ⊥ | 直角度 | Perpendicularity | 垂直方向の組立誤差防止 |
| ∠ | 平行度 | Parallelism | プレート間の平行度 |
| ⌰ | 円周振れ | Circular Runout | 回転体の精度管理 |
| ⌖ | 対称度 | Symmetry | 中心軸に対する形状対称性 |

---

## 📘 補足用語 / Supplementary Terms

| 用語 | 意味 / Meaning |
|------|----------------|
| 基準（Datum） | 他の要素の測定基準となる参照面や軸 |
| MMB（最大実体公差） | 最大材料状態での公差管理（記号：Ⓜ） |
| 公差ゾーン / Tolerance Zone | 対象要素が収まるべき空間的領域 |

---

## 🎓 演習課題への導入 / Exercises Preview

次節 `04_drawing_exercises.md` にて、以下のような実践課題を取り扱います：

- 平面度0.05の注記図面作成  
- 複数基準を用いた位置度公差枠の記述  
- CreoによるGD&T注記実習（`03_creo_examples.md` 参照）

---

## 🔗 関連リンク / Related Links

- JIS B 0021: 製品の幾何特性仕様（GPS）幾何公差  
- ISO 1101: Geometrical Product Specifications (GPS) — Geometrical tolerancing  
- `03_creo_examples.md`: CADでのGD&T記入例  
- `05_measurement_and_inspection.md`: 公差評価と検査手法  

---

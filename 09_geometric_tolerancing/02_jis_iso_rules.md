# 02_jis_iso_rules.md

## 📘 JIS / ISOに基づく幾何公差の記法と図示ルール  
📘 GD&T Notation and Representation Based on JIS / ISO Standards

本章では、**JIS B 0021** および **ISO 1101** に基づく幾何公差の記法規則と、図面上での表記方法・矢印・補助記号の使い方を解説します。

This section explains the GD&T notation rules based on **JIS B 0021** and **ISO 1101**, including how to indicate geometric tolerances on drawings, the use of symbols, arrows, and datum references.

---

## 🧭 基本記法のルール / Basic Notation Rules

### ✅ 公差枠（Feature Control Frame）

```
| 幾何特性記号 | 公差値 | 資材状態 / モディファイア | 基準 / Datums |
```

例（位置度）：

```
| Ⓜ | 0.2 | M | A | B | C |
```

- Ⓜ：位置度（Position）
- 0.2：許容値（Tolerance value）
- M：最大実体状態（Maximum Material Condition, MMC）
- A, B, C：使用される基準面や軸

---

### ✅ 基準（Datum）の定義と優先順位

- 複数基準は **左から右へ** 優先順位を持つ
- 基準には通常、アルファベット（A, B, C...）を使用
- 公差枠内での基準指定は**軸・面・線**などに基づく

---

## 📐 図面上の配置ルール / Placement Rules on Drawings

### 🖊️ リーダー線と公差枠の配置

- 公差枠は**対象フィーチャーを指す矢印**に接続
- 必要に応じて補助記号（⏤, ⌀, SΦ など）を使用
- データム記号は、**角付きフレーム（箱）**内にアルファベットで記載

```
例：
┌───────┐
│ ⊥ | 0.1 | A │
└───────┘
   ↑
   └── 対象面を指すリーダー線
```

---

## 🔣 補助記号 / Auxiliary Symbols

| 記号 | 意味（日本語） | 英語名称 |
|------|----------------|-----------|
| ⌀    | 直径           | Diameter |
| SΦ   | 球の直径       | Spherical Diameter |
| ⏤    | 表面           | Surface |
| M    | 最大実体状態   | Maximum Material Condition (MMC) |
| L    | 最小実体状態   | Least Material Condition (LMC) |
| U    | 公差追加可能状態 | Regardless of Feature Size (RFS) |

---

## 🧩 JISとISOの差異（補足） / JIS vs ISO Differences (Supplement)

| 項目 | JIS B 0021 | ISO 1101 |
|------|------------|-----------|
| 記号体系 | 原則同一 | 原則同一 |
| 表記言語 | 日本語（和文表記併用可） | 英語・記号中心 |
| 使用頻度 | 日本国内の図面に多い | グローバルな取引・設計で使用 |
| 注意点 | 和文寸法と混在する場合あり | 英文寸法・単位（mm）統一推奨 |

---

## 🧠 実践上の注意点 / Practical Tips

- 基準は明確かつ一貫して設定する（複数図面間の整合性を確保）
- 寸法公差と幾何公差の**冗長記載に注意**
- 基準面の選定は、組立・測定の現場性を考慮すること

---

## 🔗 関連資料 / Related Documents

- `01_gdt_basics.md`: 記号と意味の一覧
- `03_creo_examples.md`: CreoでのGD&T表記例
- JIS B 0021（日本工業規格）：幾何公差に関する定義
- ISO 1101: Geometrical tolerancing — Notation and rules

---

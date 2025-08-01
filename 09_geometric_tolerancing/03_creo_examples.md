# 03_creo_examples.md

## 🎓 CreoによるGD&T注記例 / GD&T Annotation Examples in Creo Parametric

本章では、PTC Creo Parametricを用いた**幾何公差（GD&T）の注記手順**を解説します。2D図面だけでなく、3Dモデル（MBD対応）への直接注記も対象とし、設計品質・検査準備性の向上を目的とします。

This chapter provides step-by-step examples of adding **GD&T annotations in Creo Parametric**. Both 2D drawing and 3D model annotations (MBD-ready) are covered to improve design intent clarity and inspection readiness.

---

## 📘 対象バージョン / Applicable Version

- Creo Parametric 7.0 以降（MBD対応強化）
- 旧バージョンでも基本操作は類似

---

## 🧭 基本手順 / Basic Workflow

### ✅ 2D図面にGD&T注記を追加する方法（Drawingモード）

1. **図面モードに切り替え**  
   - 3Dモデルから図面を生成済であることを前提とする。

2. **注記タブを開く**  
   - メニューから「注記（Annotation）」を選択。

3. **幾何公差（GTOL）を選択**  
   - ツールバーの「GTOL（幾何公差）」ボタンをクリック。

4. **対象面またはエッジを選択**  
   - 寸法対象となるフィーチャーをクリック。

5. **公差フレームを編集**  
   - ダイアログで以下を設定：  
     - 幾何特性記号（例：⊥, Ⓕ）  
     - 公差値（例：0.1）  
     - 基準（Datum）参照（例：A, B）  
     - 修飾記号（例：MMC）

6. **配置とリーダー線の調整**  
   - 公差枠を適切な位置に配置し、リーダー線で要素と接続。

7. **確認・保存**  
   - 表示位置や形式を確認し、図面ファイルを保存。

---

### ✅ 3DモデルにGD&Tを追加する方法（MBD対応 / Annotateモード）

1. **モデルを開く**  
   - パーツまたはアセンブリを開く。

2. **「注記」タブを選択（Annotate）**  
   - 「GD&T Advisor」も使用可能。

3. **幾何公差を追加**  
   - 「公差記入（Geometric Tolerance）」を選択  
   - 対象面またはエッジを選択  
   - 公差枠を定義（特性、値、基準）

4. **データムフィーチャーを作成（必要時）**  
   - 「Datum Feature Symbol」を用いて A/B/C を定義

5. **表示状態の保存**  
   - 表示ステートを登録し、3D PDF出力も可能

---

## 🖼️ 図示例 / Annotation Examples

### 例1：平面度（Flatness）

```
┌──────┐
│ Ⓕ | 0.05 │
└──────┘
   ↑
   └── 平面フィーチャーを指すリーダー線
```

### 例2：直角度（Perpendicularity）＋基準A

```
┌────────────┐
│ ⊥ | 0.1 | A │
└────────────┘
```

### 例3：位置度（Position）＋ MMC修飾

```
┌────────────────────┐
│ Ⓜ | 0.2 | M | A | B │
└────────────────────┘
```

---

## 💡 操作上のヒント / Tips

- **寸法と重複しない**幾何公差の利用が推奨される
- MBDモデルでは**アノテーションセット**を活用して可視性管理
- データム設定は「モデルの機能的基準」に基づくべき

---

## 🔗 関連ファイル / Related Files

- `01_gdt_basics.md`：GD&T記号と定義一覧  
- `02_jis_iso_rules.md`：JIS/ISOに基づく記法ルール  
- `04_drawing_exercises.md`：実践図面と演習課題

---

## 📎 添付予定 / Attachments (optional)

- Creo画面キャプチャ付きPDF（`assets/creo_gtol_examples.pdf`）  
- サンプルパーツ：`gtol_sample.prt` / `gtol_drawing.drw`

---

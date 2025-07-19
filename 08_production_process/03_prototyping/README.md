# 03_prototyping

**3Dモデルの試作と出力形式の検討**  
**Prototyping and Exporting 3D Models**

---

## 📘 概要 | Overview

このセクションでは、設計した3Dモデルを試作品として出力するプロセスを学びます。  
STL形式への変換、積層方向の考慮、サポート材の設定、スライサーソフトの操作など、**製造性・加工性を意識したデータ出力**のスキルを習得します。

In this section, learners practice converting their 3D models into formats suitable for prototyping (e.g., STL).  
Topics include slicing, print orientation, support structure planning, and design-for-manufacturing principles.

---

## 🧑‍🏫 学習目標 | Learning Objectives

- CreoからSTL形式などへのエクスポート方法を理解する  
- 積層造形を想定した形状設計の工夫を学ぶ  
- スライサーソフト（例：Cura）での条件設定を体験する  
- 3Dプリンタや加工機の仕様を意識したモデル変換を行う  
- 試作結果に基づく設計フィードバックの視点を得る  

---

## 📂 サブディレクトリ構成 | Subdirectories

```text
03_prototyping/
├── stl_exports/           # STLファイルと出力設定
├── slicing_examples/      # スライス設定例（Cura等）
├── prototyping_notes/     # 試作設計メモ・反省点
└── prototype_photos/      # 試作品の写真（任意）
```

---

## 📝 添付ファイル一覧 | Planned Files (後で作図予定)

| ファイル名 | 内容 | 備考 |
|------------|------|------|
| `box_model.stl` | 試作用モデルのSTLデータ | Creo→STL出力（予定） |
| `cura_settings.json` | スライサーの条件ファイル（Cura用） | 任意添付 |
| `prototype_observation.md` | 試作結果の気付き・改善点メモ | 教材文書 |

---

## 🔗 関連セクション | Related Sections

- [`02_drawing_creation/`](../02_drawing_creation/)  
  → 図面情報に基づいた試作モデルの出力
- [`04_measurement_report/`](../04_measurement_report/)  
  → 試作品の実測と評価・改善レポートへ連携
- [`06_bom_generation/`](../06_bom_generation/)  
  → 試作費用や数量情報をBOMに反映

---

## 💬 コメント・共有 | Feedback

3Dプリンタや加工機での試作経験、スライス条件の工夫など、実体験に基づくコメントを歓迎します。  
Discussionsでの共有もぜひご活用ください。

We welcome your experiences and tips on slicing, exporting, or prototyping!  
Feel free to share via [Discussions](https://github.com/Samizo-AITL/EduMecha/discussions).

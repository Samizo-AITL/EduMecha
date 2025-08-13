# ⚙️ **EduMecha** 

**機械設計教育のためのパラメトリック設計教材（Creo対応）**  
**Parametric Mechanical Design Educational Materials (for Creo users)**

---

🇺🇸 **[English version available here](./README_en.md)**

---

## ⚠️ **この教材についての重要な注意事項 | Important Notice**

> ❗️**本リポジトリには、PTC Creo 用の演習ファイル（.prt / .asm / .drw などのCADデータ）は含まれていません。**  
> **EduMecha** は、**機械設計教育における「教材構成・設計意図・カリキュラム構造」**を共有するための**テンプレート教材／構想仕様書**として公開されています。  
> 実ファイルを含む演習教材ではなく、**教育設計者・講師・教材開発者向けのリファレンス資料**としてご活用ください。

> ❗️**This repository does not include exercise files such as .prt, .asm, or .drw for PTC Creo.**  
> **EduMecha** is intended as a **curriculum framework and instructional design specification** for parametric mechanical design education.  
> It serves as a **reference for educators and instructional designers**, rather than a **ready-to-use student exercise set**.

---

### 📥 **モデルデータ（.prt / .asm）入手・作成方法のご案内 | How to Obtain or Create Model Files**

PTC社が提供する **無料プラン**（以下参照）を利用することで、演習用の `.prt` や `.asm` ファイルを自身で作成・取得することができます。

- **Creo Parametric Free Trial（14日間）**：  
  商用CADと同等機能を備えた評価版。**短期間で教材モデルを構築**する際に適しています。  
  [Try Creo Free Trial – PTC公式サイト](https://www.ptc.com/en/try-and-buy/free-trials)

- **Creo University Student Version（1年間）**：  
  教員・学生向けの**教育用途限定ライセンス**。**継続的な教材開発・学生教育**に適しています。  
  [Free Creo for Students and Educators](https://www.ptc.com/en/education/free-software/creo-university-download)

📄 **詳細な作成・保存・エクスポート手順については以下をご覧ください：**  
[`docs/creo_modeling_guidance.md`](./docs/creo_modeling_guidance.md)

> By using **PTC's official free versions** of Creo Parametric (trial or university edition),  
> you can create `.prt`, `.asm`, and `.drw` files yourself for use in exercises.  
> See the companion guide here: [`docs/creo_modeling_guidance.md`](./docs/creo_modeling_guidance.md)

---

## 📘 **概要 | Overview**

**EduMecha** は、**パラメトリック3D CAD（PTC Creo Parametric）**を活用し、  
**機械設計の基礎から応用までを体系的に学ぶ教育教材構成テンプレート**です。  
**2D図面からの3Dモデリング**、**設計意図の可視化**、**筐体設計**、**三角法**、**アセンブリ設計**、**CAEとの連携**など、  
**実践的な学習構造を設計者の視点で可視化**しています。

**EduMecha** is an educational repository designed to outline **structured learning paths for mechanical design**  
using **parametric 3D CAD** (primarily **PTC Creo Parametric**).  
It provides a framework for **2D-to-3D modeling**, **design intent visualization**, **enclosure modeling**,  
**third-angle projection**, **assembly design**, and **CAE integration**.

---

## 🔧 **特徴 | Features**

- ✏️ **三面図からの3Dモデリング演習案**  
  *2D → 3D modeling exercise structures*

- 📐 **拘束条件と設計意図の理解支援**  
  *Clarifying parametric constraints and design intent*

- 🧩 **組立設計と部品図演習の教材構成**  
  *Assembly modeling and drawing template design*

- 🛠 **AITL-H知能制御との統合設計構想**  
  *Integration with AITL-H intelligent control system*

- 📊 **CAE連携の教育設計視点**  
  *Pedagogical integration with tools like Creo Simulate*

---

## 🧱 **教材構成 | Directory Structure**

```text
EduMecha/
├── 00_overview/                 
├── 01_parametric_basics/        
├── 02_assembly_design/          
├── 03_drawing_skills/           
├── 04_legacy2parametric/        
├── 05_mechatronic_integration/  
├── 06_drafting_fundamentals/    
├── 07_measurement_tools/        
├── 08_production_process/       
├── 09_geometric_tolerancing/    ←★ 追加
├── templates/                   
└── assets/                      
```

| **ディレクトリ** | **内容** |
|------------------|----------|
| [`00_overview/`](./00_overview/)                 | 教材概要とマップ |
| [`01_parametric_basics/`](./01_parametric_basics/)        | Creo操作入門と設計演習構成 |
| [`02_assembly_design/`](./02_assembly_design/)          | 組立設計の学習構成テンプレート |
| [`03_drawing_skills/`](./03_drawing_skills/)           | 三角法・図面生成の教材設計 |
| [`04_legacy2parametric/`](./04_legacy2parametric/)        | 手描き図面 → 3D演習設計案 |
| [`05_mechatronic_integration/`](./05_mechatronic_integration/)  | 制御筐体連携の演習構成案 |
| [`06_drafting_fundamentals/`](./06_drafting_fundamentals/)    | 製図基本要素の整理 |
| [`07_measurement_tools/`](./07_measurement_tools/)        | 寸法評価・トレーサビリティ演習構成 |
| [`08_production_process/`](./08_production_process/)       | 製造プロセス教育の構成案 |
| [`09_geometric_tolerancing/`](./09_geometric_tolerancing/) | 幾何公差（GD&T）の記法・演習・検査の総合教材 |
| [`templates/`](./templates/)                   | テンプレート仕様設計（Creoを前提） |
| [`assets/`](./assets/)                         | 教材用画像・参考図面（演習データは含まず） |

---

## 🔗 **関連プロジェクト | Related Projects**

- [**Edusemi**](https://github.com/Samizo-AITL/Edusemi-v4x) – 半導体設計教材（sky130）
- [**EduController**](https://github.com/Samizo-AITL/EduController) – 制御理論／AI制御教材
- [**AITL-H**](https://github.com/Samizo-AITL/AITL-H) – 知能制御統合アーキテクチャ
- [**SamizoGPT**](https://github.com/Samizo-AITL/SamizoGPT) – 教材構成・プロンプト支援
- [**PTC Creo Parametric**（公式）](https://www.ptc.com/en/products/creo)

---

## 📜 **ライセンス | License**

This project is released under the **MIT License**.  
**Educational and non-commercial reuse is welcome.**  
MIT License に基づき公開しています。**非営利・教育目的での再利用を歓迎**します。

---

## 👤 **執筆者情報 / Author**

**三溝 真一（Shinichi Samizo）**  
- **信州大学大学院 電気電子工学 修了**  
- 元 **セイコーエプソン**株式会社 技術者（1997年〜）

📌 **経験領域**：  
- **半導体デバイス（ロジック・メモリ・高耐圧混載）**  
- **インクジェット薄膜ピエゾアクチュエータ**  
- **PrecisionCoreプリントヘッド製品化・BOM管理・ISO教育**

📬 **連絡先**  
- ✉️ [shin3t72@gmail.com](mailto:shin3t72@gmail.com)  
- 🐦 [https://x.com/shin3t72](https://x.com/shin3t72)  
- 💻 [https://samizo-aitl.github.io/](https://samizo-aitl.github.io/)

---

## 💬 **フィードバック・質問 | Feedback & Discussion**

教材に関するご質問・改善提案・派生教材の展開などは  
**GitHub Discussions** にて歓迎します。  
**教育関係者・研究者・技術者の皆様からのご参加をお待ちしています。**

👉 [EduMecha Discussions ページへ移動](https://github.com/Samizo-AITL/EduMecha/discussions)

---

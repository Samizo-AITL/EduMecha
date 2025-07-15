# EduMecha 概要 | EduMecha Overview

**EduMecha** は、PTC Creo Parametric を活用した、機械設計教育のためのオリジナル教材群です。  
基本操作からアセンブリ設計、図面生成、制御対象の筐体設計、さらには産業応用例までを段階的に学ぶことができます。

**EduMecha** is a specialized educational project for mechanical design using PTC Creo Parametric.  
It provides a structured learning path from basic modeling and assembly to technical drawings, enclosure design for control systems, and real-world industrial applications.

---

## 📁 ディレクトリ構成 | Directory Structure

| ディレクトリ | 内容（日本語） | Description (English) |
|--------------|------------------|-------------------------|
| [`00_overview/`](./00_overview/) | 教材の概要と構成マップ | Overview and structure map |
| [`01_parametric_basics/`](./01_parametric_basics/) | Creo入門とパーツ設計の基礎 | Basic part modeling with Creo |
| [`02_assembly_design/`](./02_assembly_design/) | 部品の拘束・組立設計 | Assembly and constraint modeling |
| [`03_drawing_skills/`](./03_drawing_skills/) | 三角法・図面生成と読解 | Orthographic projection and drawing practice |
| [`04_legacy2parametric/`](./04_legacy2parametric/) | 手描き図面からの3D再構築 | 3D reconstruction from legacy drawings |
| [`05_mechatronic_integration/`](./05_mechatronic_integration/) | 制御対象との統合設計（筐体設計） | Mechatronic integration and enclosure design |
| [`06_drafting_fundamentals/`](./06_drafting_fundamentals/) | 製図の基本（寸法・公差・JIS） | Technical drawing fundamentals (JIS standards) |
| [`07_measurement_tools/`](./07_measurement_tools/) | 寸法測定・校正・トレーサビリティ | Dimensional measurement and calibration |
| [`assets/`](./assets/) | モデル・図面・教材用画像など | Models, drawings, and visual assets |

---

## 🧭 学習フロー | Learning Flow

```plaintext
01: Creo入門（基本操作・スケッチ・押し出し）
 ↓
02: アセンブリ設計（拘束・干渉・接続）
 ↓
03: 図面生成（三角法・寸法記入・製図規格）
 
04: 図面からの3D再構築（逆設計・意図推定）
 ↓
05: 制御対象の筐体設計（FSM/PID構造と接続）
 ↓

06: 応用設計（インクジェット構造などの産業設計例）

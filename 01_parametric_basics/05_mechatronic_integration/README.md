# 🤖 05 - Mechatronic Integration

この演習では、**メカトロニクス設計と Creo モデリングの統合**に向けて、制御対象（センサ・サーボモータ）との接続構造を設計します。AITL-H などの制御教材と連携可能な基本構造体の構築が目的です。

---

## 🧭 学習目標

- センサ／サーボを固定する筐体部品の設計
- 機構自由度（回転・移動）を意識した構造検討
- 統合設計における部品間のインタフェース設計
- Creo によるパーツ組合せとアセンブリ設計の準備

---

## 📁 各演習フォルダと構成

| フォルダ名 | 内容 | 構成ファイル |
|-----------|------|--------------|
| [`01_sensor_mount_base/`](./01_sensor_mount_base/) | センサ実装基板のモデル化と取付穴設計 | [01_intro](./01_sensor_mount_base/01_intro.md) / [02_steps](./01_sensor_mount_base/02_steps.md) / [03_explanation](./01_sensor_mount_base/03_explanation.md) / [04_exercise](./01_sensor_mount_base/04_exercise.md) |
| [`02_servo_joint_bracket/`](./02_servo_joint_bracket/) | サーボモータ接続部の調整機構設計 | [01_intro](./02_servo_joint_bracket/01_intro.md) / [02_steps](./02_servo_joint_bracket/02_steps.md) / [03_explanation](./02_servo_joint_bracket/03_explanation.md) / [04_exercise](./02_servo_joint_bracket/04_exercise.md) |
| [`03_gimbal_frame/`](./03_gimbal_frame/) | 2軸ジンバル機構によるフレーム組立 | [01_intro](./03_gimbal_frame/01_intro.md) / [02_steps](./03_gimbal_frame/02_steps.md) / [03_explanation](./03_gimbal_frame/03_explanation.md) / [04_exercise](./03_gimbal_frame/04_exercise.md) |

> 各フォルダには、 `01_intro.md` ～ `04_exercise.md` の4つのファイルが含まれています。

---

## 🛠 使用ツール

- PTC Creo Parametric（2022 以降推奨）
- AITL-H 制御教材（参考連携）

---

## 🔗 関連リンク

- 🔙 [01_parametric_basics/ に戻る](../README.md)
- 🚀 [EduController（AITL 制御教材）](https://github.com/Samizo-AITL/EduController)

# 03_gimbal_frame - 知能制御対象ジンバルの設計教材

## 概要
本教材は、AITL-Hアーキテクチャ（FSM×PID×LLM）を制御対象に適用するための2軸ジンバル構造を設計・制御する演習です。
Yaw（外枠）とPitch（内枠）をもつ構造に、IMUを搭載することで、動的安定化や目標追従を実現します。

## 学習目標
- Creoを用いたジンバル構造の設計（Yaw/Pitch/IMUマウント）
- FSMによる状態遷移制御（センサトリガ／過負荷検出など）
- PIDによる姿勢安定化制御
- LLMによる目標指令やログ評価の連携（AITL-H）

## 使用パーツ
| ファイル名 | 説明 |
|------------|------|
| `frame_outer_yaw.prt` | 外枠（Yaw軸回転） |
| `frame_inner_pitch.prt` | 内枠（Pitch軸回転） |
| `imu_mount_base.prt` | センサ固定用台座（IMU搭載部） |

## 制御構成（FSM × PID × LLM）
- `fsm.yaml`：状態定義（idle → move → error）
- `pid_params.md`：各軸のPIDゲインと調整法
- `llm_prompts.md`：ChatGPTによる目標生成・異常対話の支援

## 実習課題例
1. ジンバル構造をCreoで構成し、2軸回転可能な拘束条件を設定せよ
2. FSM制御（`fsm.yaml`）を用いて状態遷移シミュレーションを行え
3. PID調整によりIMU値の安定性を高め、振動抑制制御を設計せよ
4. LLM（ChatGPT）との連携により、異常ログから目標生成・対話補助を行え

---

著作：三溝真一（Samizo-AITL）  
ライセンス：MIT（教育目的の使用・PoC活用を歓迎）

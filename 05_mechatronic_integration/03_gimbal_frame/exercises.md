# 統合演習課題 - Gimbal構造 × FSM × PID × LLM

この演習は、ジンバル制御対象の3D設計と、FSM・PID・LLMを連動させた制御教材として構成されています。以下のステップに従って、段階的に設計・制御・考察を行ってください。

---

## 📘 STEP 1：ジンバル構造の設計（Creo）
```
　1.	frame_outer_yaw.prt（Yaw軸外枠）を作成
　2.	frame_inner_pitch.prt（Pitch軸内枠）を設計し、外枠に回転拘束で接続
　3.	imu_mount_base.prt をPitch軸に固定（IMU想定位置）
　4.	gimbal.asm にすべて組み込み、アセンブリを完成
```
---

## ⚙️ STEP 2：FSMによる状態遷移制御
```
　1.	fsm.yaml を参照し、以下の状態遷移を実装：
	•	idle → move：センサ入力（sensor_triggered）
	•	move → error：過負荷検出（overload）
	•	error → idle：リセット指令（reset）
　2.	状態変化に応じて、PID制御のON/OFFを切り替える
　3.	状態ログ（state_log.md）を記録し、後でLLMに渡せる形式に整える
```
 ---

## 🔧 STEP 3：PIDによる姿勢制御
```
　1.	初期パラメータを pid_params.md に従って設定：
	•	Yaw：Kp=1.5, Ki=0.05, Kd=0.2
	•	Pitch：Kp=2.0, Ki=0.1, Kd=0.25
　2.	目標姿勢に対して応答を測定（IMU出力ログを記録）
　3.	PythonやCSVで imu_response_plot.png を生成し、可視化
　4.	応答が不安定な場合、以下のステップで調整：
	•	Kp → 応答速度とオーバーシュートに影響
	•	Kd → 振動と過渡応答に影響
	•	Ki → 長期的な偏差（バイアス補正）に影響
```
---

## 🤖 STEP 4：ChatGPTとの連携（LLM制御支援)
```
　1.	状態遷移ログを llm_prompts.md の「状態遷移診断」プロンプトに渡す
　2.	IMUログをもとに、PID調整案を対話形式で確認
　3.	error状態発生時に、ChatGPTに異常原因と復旧条件を相談
　4.	任意で、目標姿勢をLLMに生成させ、PIDで追従できるか検証
```
---

## 📝 STEP 5：考察とレポート作成
```
　1.	FSMとPIDの連携による安定性への効果を考察せよ
　2.	LLMを活用した制御支援の有効性・限界を記述せよ
　3.	設計した構造の変更点が制御特性に与える影響をまとめよ
　4.	以上を markdown または PDFでまとめ、提出またはZenn記事として整理
```
 ---

## 提出物一覧（例）

- `gimbal.asm`（Creoアセンブリ）
- `fsm.yaml`
- `pid_params.md`（実調整値に更新済）
- `imu_response_plot.png`
- `state_log.md`（FSMログ）
- `llm_dialog_log.md`（ChatGPT対話ログ）
- `report.md` または `report.pdf`

---

著作：三溝真一（Samizo-AITL）  
ライセンス：MIT（教育目的の複製・改変・提出を歓迎）


 

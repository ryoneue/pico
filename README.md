# pico library
ラズピコ向けに各センサーごとにクラスを作成したものを置いておく用
micropythonだけ
  ## 現状作成済み一覧
  - サーボモータ (fs90r)
    - 簡単な動作（正転，反転，停止）
    - 
  - 音センサ (grove)
    - 音検出（閾値，音の長さ）
    - 音量取得
  - 光センサ (grove)
    - 光検出
    - 明るさ取得
  - lcd (AQM0802)
    - i2c接続
    - 画面リフレッシュ
    - 文字表示（上下選択，文字ずらし）
  - 時間計測
    - pioによる正確な時間計測用モジュール

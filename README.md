# 概要
#### このプログラムはGoProの.MP4動画からGPSデータを抽出するプログラムです．
参考：https://github.com/JuanIrache/gopro-utils

# 必要な環境
- 動作確認済み環境 -> Mac OS Catalina ver.10.15.1
- 必要言語：Python3
- 必要環境：FFmpeg

# 導入方法
    ==================================================================
    環境が無いならこれを実行
    - brew install python3
    - brew install ffmpeg
    ==================================================================
    - git clone https://github.com/yodai-hi/gopro_gps_dumper.git
    - cd gopro_gps_dumper
    - pip install -r requirement.txt
    - gopro_gps_dumper/gps_dumper/video/ に抽出したい動画を入れる（複数可）
    - python3 dumper.py
    
    done

# 抽出データ

データは gopro_gps_dumper/output/ 内に保存される

pd.load_pickle('video_gps_data.zip') でDataFrameに復元可能

|      |VIDEO_NAME|UNIX_TIME|LATITUDE|LONGITUDE|TIME_SPAN|
|------|----------|---------|--------|---------|---------|
|ラベル|動画名     |GPSの時間|緯度     |経度     |時間の差分|

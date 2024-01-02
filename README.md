# NTNU Computer Programming and Data Analysis in Sports (Fall 2023)
## 期末專題
### 專題主旨
運用近 10 年（2013~2022）內 MLB 各隊例行賽出賽球員數據，預測 2023 各隊奪冠機率。
> [!NOTE]\
> [HackMD 說明文件](https://hackmd.io/@twdanielcheng112/112-1cpdas)

### 檔案說明
- MLB stats 爬蟲
  - `mlb_stats_auto_crawler.ipynb`：自動爬取指定年分間的 MLB 所有隊伍例行賽出賽球員數據
  - `mlb_stats_signal_crawler.ipynb`：單一球隊球員數據爬取
  - `mlb_stats_signal_crawler.py`：單一球隊球員數據爬取
  - `mlb_stats_urls` folder：用於儲存各球隊數據網址，以便前述檔案運行
- 資料處理
  - `data_processing.py`：用於清理爬取後的資料、加上標籤，讓資料可以餵給模型訓練
- 資料集
  - `mlb_stats` 資料夾
    - 進十年各隊伍所有出賽球員數據集，共 13228 筆資料，整理後按年份資料夾、球隊名稱命名為 csv 格式檔案存放
    - `data_filter.csv`：將對於球隊影響力低的球員刪除後清理的資料，用於模型訓練
    - `data_origin.csv`：將所有資料直接清理，用於模型訓練
    - `MLB_rank.csv`：近十年各隊伍的成績排名數據
- 模型與結果
  - `model` 資料夾
    - `result` 中按照模型名稱儲存，分為原始資料訓練結果與篩選資料訓練結果
      - txt file 中紀錄模型評估數據
      - 圖表呈現模型效能：Q-Q Plot of Residuals、Residual Plot、Scatter Plot of True vs Predicted Values
    - Regression 模型
      - Gradient Boosting Regressor
      - Linear Regression
      - Random Forest Regressor
      - SGD Regressor
      - SVR

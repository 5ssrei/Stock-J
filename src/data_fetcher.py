import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

def fetch_stock_data(ticker, start_date, end_date):
    """
    获取股票数据并清理。
    :param ticker: 股票代码（如 'AAPL' 表示 Apple）
    :param start_date: 起始日期，格式为 'YYYY-MM-DD'
    :param end_date: 结束日期，格式为 'YYYY-MM-DD'
    :return: 清理后的数据
    """
    # 下载数据
    data = yf.download(ticker, start=start_date, end=end_date)
    # 重置索引以保留日期列
    data.reset_index(inplace=True)
    # 删除缺失值
    data.dropna(inplace=True)
    return data

def plot_close_price(data, ticker):
    """
    绘制收盘价趋势图。
    :param data: 股票数据（DataFrame 格式）
    :param ticker: 股票代码
    """
    plt.figure(figsize=(10, 5))
    plt.plot(data['Date'], data['Close'], label='Close Price', linewidth=2)
    plt.title(f'{ticker} Close Price Trend')
    plt.xlabel('Date')
    plt.ylabel('Close Price (USD)')
    plt.grid(True)
    plt.legend()
    plt.show(block=True)  # 强制等待图表窗口关闭

if __name__ == "__main__":
    # 定义股票代码和日期范围
    ticker = "AAPL"  # 替换为您感兴趣的股票代码
    start_date = "2023-01-01"
    end_date = "2023-12-01"

    # 获取数据
    stock_data = fetch_stock_data(ticker, start_date, end_date)

    # 打印数据预览
    print(stock_data.head())  # 打印前几行数据

    # 绘制收盘价趋势图
    plot_close_price(stock_data, ticker)

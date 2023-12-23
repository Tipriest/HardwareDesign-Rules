import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.family'] = 'SimHei'  # 设置使用的中文字体，比如SimHei

# 读取文本文件
data = pd.read_csv('/home/tipriest/Documents/calCANRate/data.txt', delimiter='\t', encoding='gbk')

# 处理时间列
data['时间标识'] = pd.to_datetime(data['时间标识'], errors='coerce')  # 将无效的时间值转换为NaT
data = data.dropna(subset=['时间标识'])  # 删除包含空时间值的行
data = data.set_index('时间标识')

# 计算每秒传输的数据个数
data['每秒传输数据个数'] = data.resample('S')['数据'].count()

# 绘制每秒传输数据个数随时间的变化图
plt.plot(data.index.values, data['每秒传输数据个数'].values)
plt.xlabel('Time')
plt.ylabel('Data Transfered per sec')
plt.title('Data Transfered Cal')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()
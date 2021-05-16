import requests
import pygal
from pygal.style import LightColorizedStyle as LCS
from pygal.style import LightStyle as LS

# 执行API调用存储响应
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print("Status code:", r.status_code)  # 返回状态

# 将响应数据存入变量中
response_dict = r.json()  # 使用json()将这些转换为python字典
# print(response_dict.keys())  # 打印response_dict的键
print("Total repositories:", response_dict['total_count'])
# print("items:", response_dict['items'])  # ’items‘是一个键，其值的元素是字典


# 获取一个仓库数据
repo_dicts = response_dict['items']  # repo_dicts为一个list
print("Repositories returned:", len(repo_dicts))  # 仓库数
print(repo_dicts)
names, plot_dicts = [], []

# repo_dict = repo_dicts[0]  # 获得第一个仓库
# # print("\nKeys: ",
# #       len(repo_dict))  # 第一个repository的键量
# # for key in sorted(repo_dict.keys()):
# #     print(key)
# # print("\nSelect information from first repository:")
# print('Name:', repo_dict['name'])
# print('Owner:', repo_dict['owner']['login'])
# print('Stars:', repo_dict['stargazers_count'])
# print('Repository', repo_dict['html_url'])
# # print('Created:', repo_dict['created_at'])
# # print('Updated:', repo_dict['updated_at'])
# print('Description:', repo_dict['description'])
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    plot_dict = {
        'value': repo_dict['stargazers_count'],
        # 'label': repo_dict['description'],
        # 'xlink': repo_dict['html_url'],
    }  # 自定义工具提示标签
    plot_dicts.append(plot_dict)

# 绘制可视化界面
my_style = LS(base_style=LCS())  # 使用该类定义样式，并将其基色设置为深蓝色，第二个实参用于使用另一个类Light Colorized Style

# 配置样式
my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.title_font_size = 24
my_config.label_font_size = 14
my_config.major_label_font_size = 18
my_config.truncate_label = 15  # 将较长的标签名缩短为15字符
my_config.show_y_guides = False  # 隐藏图上水平线
my_config.width = 1000

# 绘图
chart = pygal.Bar(my_config, style=my_style)
# chart = pygal.Bar(style=my_style, x_label_rotation=45, show_legend=False)  # 使用Bar()创建一个条形图，x_label_rotation参数是标签旋转45， show_legend参数来隐藏图例
chart.title = 'Most-Starred Python Projects on Github'
chart.x_labels = names

chart.add('', plot_dicts)
chart.render_to_file('repos_requests.svg')

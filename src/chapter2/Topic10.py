"""
编程计算平台上两点之间的距离

"""
point_1 = {'x': 15, 'y': 10}
point_2 = {'x': 10, 'y': 5}
print('点a为:({0},{1})\n点b为({2},{3})'.format(point_1['x'], point_1['y'], point_2['x'], point_2['y']))
print('两点这间相差:({0},{1})'.format(abs(point_1['x'] - point_2['x']), abs(point_1['y'] - point_2['y'])))

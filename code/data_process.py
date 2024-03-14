def max30102_getSpO2(ir_input_data, red_input_data, cache_nums):
    ir_max = max(ir_input_data)
    ir_min = min(ir_input_data)
    red_max = max(red_input_data)
    red_min = min(red_input_data)
    R = ((ir_max + ir_min) * (red_max - red_min)) / ((red_max + red_min) * (ir_max - ir_min))
    SpO2 = (-45.060) * R * R + 30.354 * R + 94.845
    return SpO2


# 示例数据
ir_input_data = [100634, 100628, 100611, 100568]  # 红外ADC采样数据
red_input_data = [82355, 82346, 82322, 82308]  # 近红外ADC采样数据
cache_nums = len(ir_input_data)

# 计算血氧饱和度
SpO2 = max30102_getSpO2(ir_input_data, red_input_data, cache_nums)
print("血氧饱和度: {:.2f}%".format(SpO2))

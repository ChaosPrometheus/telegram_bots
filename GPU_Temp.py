import pynvml
import time

pynvml.nvmlInit()
device_count = pynvml.nvmlDeviceGetCount()

while True:
    for i in range(device_count):
        handle = pynvml.nvmlDeviceGetHandleByIndex(i)
        gpu_name = pynvml.nvmlDeviceGetName(handle)
        gpu_utilization = pynvml.nvmlDeviceGetUtilizationRates(handle).gpu
        gpu_temperature = pynvml.nvmlDeviceGetTemperature(handle, pynvml.NVML_TEMPERATURE_GPU)
        print(f"Видеокарта {i+1}: {gpu_name}")
        print(f"Загрузка видеокарты: {gpu_utilization}%")
        print(f"Температура видеокарты: {gpu_temperature}°C")
    
    time.sleep(5)  # Задержка в секундах (в данном случае 5 секунд)
    print("-----")  # Разделитель между обновлениями

pynvml.nvmlShutdown()

#information = ("Видеокарта "+ gpu_name + "\n" 
#               + "Загрузка видеокарты: " + str(gpu_utilization) + "%" + "\n" 
#               + "Температура видеокарты: " + str(gpu_temperature) + "%" )

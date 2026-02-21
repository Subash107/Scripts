import psutil
import logging

def check_disk(threshold):
    partitions = psutil.disk_partitions()
    alerts = []

    for partition in partitions:
        usage = psutil.disk_usage(partition.mountpoint)
        if usage.percent > threshold:
            message = f"Disk usage high on {partition.mountpoint}: {usage.percent}%"
            logging.warning(message)
            alerts.append(message)

    return alerts

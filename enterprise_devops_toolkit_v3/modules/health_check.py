import psutil
import logging

def check_service(service_name):
    for service in psutil.win_service_iter():
        if service.name().lower() == service_name.lower():
            status = service.status()
            logging.info(f"Service {service_name} status: {status}")
            return status
    logging.warning(f"Service {service_name} not found")
    return "Not Found"

import win32serviceutil
import win32service
import win32event
import servicemanager
import time
import sys
import os

# Add parent folder to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import run_toolkit

class DevOpsService(win32serviceutil.ServiceFramework):
    _svc_name_ = "EnterpriseDevOpsToolkitService"
    _svc_display_name_ = "Enterprise DevOps Toolkit Service"
    _svc_description_ = "Runs DevOps monitoring toolkit every 5 minutes."

    def __init__(self, args):
        win32serviceutil.ServiceFramework.__init__(self, args)
        self.stop_event = win32event.CreateEvent(None, 0, 0, None)
        self.running = True

    def SvcStop(self):
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        self.running = False
        win32event.SetEvent(self.stop_event)

    def SvcDoRun(self):
        servicemanager.LogInfoMsg("DevOps Toolkit Service Started")
        while self.running:
            run_toolkit()
            time.sleep(300)  # 5 minutes

if __name__ == '__main__':
    win32serviceutil.HandleCommandLine(DevOpsService)

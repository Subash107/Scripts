# Enterprise DevOps Automation Toolkit (v3)

Now includes:
- Windows Service Mode
- Task Scheduler Script
- Interval Loop Mode

## Install
pip install -r requirements.txt

## Run Manual
python main.py

## Run Loop Mode
python main.py --interval 5

## Install Windows Service (Run as Administrator)
cd windows_service
python devops_service.py install
python devops_service.py start

## Stop Service
python devops_service.py stop

## Remove Service
python devops_service.py remove

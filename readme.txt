Home to Control cockpit automation

Steps to use the framework:
1. Install requirements from command prompt: pip install -r requirements.txt
2. For reporting:
	a. install scoop using powershell as Administrator:
	step 1: iex (new-object net.webclient).downloadstring('https://get.scoop.sh')
	Step 2: scoop install allure
	b.Run test using allure in root folder of framework:
		Run in command prompt: py.test --alluredir ./Reports
	C. To generate report using allure:
		go to: {Framework Root}/Reports
		Run:0_Report_Launcher.bat

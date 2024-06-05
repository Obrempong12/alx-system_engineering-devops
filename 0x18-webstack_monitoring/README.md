## 0x18. Webstack monitoring
---
![image](https://github.com/Obrempong12/alx-system_engineering-devops/assets/144380171/2ca9e5ba-8be7-44ff-8d85-a4d77a480041)

# Background Context
“You cannot fix or improve what you cannot measure” is a famous saying in the Tech industry. In the age of the data-ism, monitoring how our Software systems are doing is an important thing. In this project, we will implement one of many tools to measure what is going on our servers.
![image](https://github.com/Obrempong12/alx-system_engineering-devops/assets/144380171/717f4199-1e3b-40aa-b21b-decb6ae11ff1)

Web stack monitoring can be broken down into 2 categories:
* Application monitoring: getting data about your running software and making sure it is behaving as expected
* Server monitoring: getting data about your virtual or physical server and making sure they are not overloaded (could be CPU, memory, disk or network overload)

## Tasks
0. Sign up for Datadog and install datadog-agent
![image](https://github.com/Obrempong12/alx-system_engineering-devops/assets/144380171/39628fe3-2616-4283-8d59-42fc55b4b54b)
For this task head to https://www.datadoghq.com/ and sign up for a free Datadog account. When signing up, you’ll have the option of selecting statistics from your current stack that Datadog can monitor for you. Once you have an account set up, follow the instructions given on the website to install the Datadog agent.
1. Monitor some metrics
![image](https://github.com/Obrempong12/alx-system_engineering-devops/assets/144380171/caf8e37b-bbbd-4a6a-bb22-46c840833f3d)
Among the litany of data your monitoring service can report to you are system metrics. You can use these metrics to determine statistics such as reads/writes per second, which can help your company determine if/how they should scale. Set up some monitors within the Datadog dashboard to monitor and alert you of a few. You can read about the various system metrics that you can monitor here: System Check.
2. Create a dashboard
Now create a dashboard with different metrics displayed in order to get a few different visualizations.
* Create a new dashboard
* Add at least 4 widgets to your dashboard. They can be of any type and monitor whatever you’d like
* Create the answer file 2-setup_datadog which has the dashboard_id on the first line. Note: in order to get the id of your dashboard, you may need to use Datadog’s API

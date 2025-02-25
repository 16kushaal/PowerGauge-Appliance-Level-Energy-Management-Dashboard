# PowerGauge-Appliance-Level-Energy-Management-Dashboard

## 📌 Introduction  
In the face of increasing energy demand and climate change concerns, **PowerGauge** provides an **appliance-level energy tracking solution** to help Indian households **optimize energy consumption** and reduce wastage. With real-time insights and interactive visualizations, users can identify high-energy-consuming appliances and take informed actions.

## 🎯 Objective  
- **Appliance-Specific Monitoring**: Track energy consumption at the appliance level.  
- **Energy Efficiency**: Reduce household energy wastage by up to **20%**.  
- **Interactive Dashboard**: PyQt6-based UI with **Matplotlib** visualizations.  
- **Scalable Data Management**: Uses **MySQL** for structured data storage.  
- **Historical Analysis**: Detect seasonal variations and inefficiencies over time.  
- **Sustainability Focus**: Aligns with India’s energy efficiency and carbon reduction goals.  

## 🚀 Features  
### ✅ Appliance-Specific Insights  
- Identify high-energy-consuming appliances.  
- Optimize usage to lower electricity costs.
- Daily energy predcition from past data.

### 📊 Interactive Dashboard  
- Built using **PyQt6** for seamless user experience.  
- Dynamic visualizations using **Matplotlib** (line charts, bar graphs, pie charts).  

### 💾 Scalable Data Management  
- **MySQL-based** structured data storage.  
- Fast and secure access to appliance-level consumption data.  

### 📈 Energy Analysis & Reporting  
- Generate real-time reports on energy usage.  
- Filter data by time periods and consumption patterns.  

### 🌍 Sustainability & Environmental Impact  
- Helps users **reduce carbon footprints** and energy costs.  
- Supports **India’s national sustainability** goals.  


## 📌 Features
- Real-time appliance-level energy monitoring
- Interactive dashboard for energy consumption analysis
- Predictive analytics for power optimization
- User-friendly interface for data visualization

## 🏗 Technologies Used
- Frontend: PyQt6
- Data Visualization: Matplotlib
- Database: MySQL
- Backend: Python
- Predictions: Prophet

## 🔷 Data Flow Diagram
 ![](https://github.com/16kushaal/PowerGauge-Appliance-Level-Energy-Management-Dashboard/blob/master/images/DFD0.png)
 DFD Level 0 (or Context Diagram), represents the system as a single process. Figure shows high-level inputs and outputs interacting with external entities. The primary external entity here is the User, who provides inputs such as Username and Password to access the system. The system, represented as a single process named Powergauge, processes this information and delivers outputs like Visualization and Analytics to the user. 

![](https://github.com/16kushaal/PowerGauge-Appliance-Level-Energy-Management-Dashboard/blob/master/images/DFD%201.png)
The Level 1 Data Flow Diagram (DFD), provides a detailed decomposition of the system into three primary subprocesses: Login, Device Management, and Visual Generations. These subprocesses illustrate how the system processes data and interacts with the user to achieve its objectives. The Login subprocess handles the authentication of users by validating their credentials. The user provides inputs such as username and password, and the system verifies them against stored data to grant access. This ensures secure access to the system while maintaining user-specific operations. The Device Management subprocess manages the interaction between users and their associated devices. It allows users to input, update, or query device-related data. The system processes and stores details about devices, enabling efficient tracking and management of user-specific devices. The Visual Generations subprocess focuses on creating visual outputs for the user. Based on the data from devices and user interactions, the system generates insights, analytics, or reports in a visually comprehensible format. 

![](https://github.com/16kushaal/PowerGauge-Appliance-Level-Energy-Management-Dashboard/blob/master/images/DFD%202.1.png)
The Login process is designed to authenticate existing users securely. The user provides their Username and Password, which are passed to the system for validation. The system verifies these credentials against the stored user data in the database. If the credentials match, access is granted, and the user is directed to the main system functionalities.

![](https://github.com/16kushaal/PowerGauge-Appliance-Level-Energy-Management-Dashboard/blob/master/images/DFD%202.2.png)
Provides a detailed breakdown of how energy consumption is monitored, managed, and mapped for efficient user 
interaction. At the core of the system is the Device Initialization & Selection (Process 2.1), where users begin by registering their devices and selecting which ones to track. This step ensures that all relevant devices are appropriately configured within the system, forming the foundation for subsequent operations. Once the devices are initialized, the Usage Calculation (Process 2.2) process comes into play, where the system processes real-time data from connected meters and devices to compute energy consumption metrics. This process provides critical insights into energy usage patterns, allowing users to make informed decisions about their energy consumption behavior. 

![](https://github.com/16kushaal/PowerGauge-Appliance-Level-Energy-Management-Dashboard/blob/master/images/DFD%202.3.png)
This Level 3 Data Flow Diagram (DFD) expands upon the processes related to the visualization and usage monitoring aspects of the system as shown . At its core, the diagram highlights three interrelated processes 
aimed at providing detailed insights and an intuitive user experience. 

## 🛠 Installation  
To install **PowerGauge**, run the following commands:  
```bash
git clone https://github.com/16kushaal/PowerGauge-Appliance-Level-Energy-Management-Dashboard
cd PowerGauge
pip install -r requirements.txt
```

## ⚡ Running the Application
After installation, run the following command to start the application:
```bash
python src\main.py
```

## PowerGauge-Appliance-Level-Energy-Management-Dashboard
├── 📂 db/                         # Database-related files
│   ├── 📄 online_db.sql           # SQL schema for online database setup
│   └── 📄 energy.sql              # Data to populate the local database
│
├── 📂 images                      # Image assets for project(Data Flow Diagrams)
│
├── 📂 src/                        # Source code for the application
│   ├── 📂 helpers/                # Backend logic and API
│   │   ├── 📄 DatabaseHelper.py    # DB Helper
│   │   ├── 📄 GraphHelper.py       # Visuals generator and helper
│   │   ├── 📄 UIHelper.py          # User Interface Helper
│   │
│   ├── 📂 resources/               # Frontend application
│   │   ├── 📂 images              # Project Logo and image dependencies
│   │   ├── 📂 ui                  # Dashboard UI components
│   │
│   └── 📄 main.py                  # Main running file
│   └── 📄 prophet_model.py         # Energy Predicition model
│
├── 📄 .gitignore                  # Git ignore file
├── 📄 README.md                   # Project documentation
└── 📄 requirements.txt            # Python dependencies


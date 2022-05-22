import pyodbc

# Some other example server values are
# server = 'localhost\sqlexpress' # for a named instance
# server = 'myserver,port' # to specify an alternate port
# instance version: Microsoft SQL Server 2019 (RTM-GDR) (KB4583458) - 15.0.2080.9 (X64)   Nov  6 2020 16:50:01   Copyright (C) 2019 Microsoft Corporation  Express Edition (64-bit) on Windows 10 Home 10.0 <X64> (Build 19044:) 

def CreateConnection():
    # 下列範例提供指定 Azure Active Directory 互動式驗證的 ODBC 連接字串：
    # server=Server;database=Database;UID=UserName;Authentication=ActiveDirectoryInteractive;
    server = '.\SQLExpress' 
    database = 'Northwind' 
    username = 'mento' 
    password = 'P@ssW0rd' 
    return pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)


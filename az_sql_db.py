import sqlite3

def create_db():
    # Create Database
    connection = sqlite3.connect("Azure_Board.db")
    crsr = connection.cursor()

    # SQL command to create a table in the database
    sql_command_us = """CREATE TABLE UserStory ( 
    workItemId INT(100), 
    System_Title VARCHAR(500),
    displayName VARCHAR(500),
    name VARCHAR(500),
    revisedDate VARCHAR(500),
    System_State VARCHAR(20), 
    System_Reason VARCHAR(30), 
    System_AreaPath VARCHAR(100), 
    System_IterationPath VARCHAR(100),
    Story_Points VARCHAR(100),
    Requirement_ID VARCHAR(100),
    Microsoft_VSTS_Common_Priority VARCHAR(100),
    Microsoft_VSTS_Common_ValueArea VARCHAR(100),
    System_Description VARCHAR(20000),
    Microsoft_VSTS_Common_AcceptanceCriteria VARCHAR(20000)
    );"""
    sql_command_epic = """CREATE TABLE Epic ( 
    workItemId INT(100), 
    System_Title VARCHAR(500),
    name VARCHAR(500),
    displayName VARCHAR(500),
    revisedDate VARCHAR(500),
    System_State VARCHAR(20), 
    System_Reason VARCHAR(30), 
    System_AreaPath VARCHAR(100), 
    System_IterationPath VARCHAR(100),
    Microsoft_VSTS_Common_Priority VARCHAR(100),
    System_Description VARCHAR(20000)

    );"""
    sql_command_rel = """CREATE TABLE WI_Relations(
        workItemId INT(100), 
        name VARCHAR(100),
        rel_id VARCHAR(20),
        System_WorkItemType VARCHAR(100)
        );"""
    sql_command_revs = """CREATE TABLE Revisions(
        workItemId INT(100),
        rev INT(100),
        System_RevisedBy VARCHAR(1000),
        System_ChangedDate VARCHAR(1000),
        Field VARCHAR(1000),
        Operation VARCHAR(1000),
        new_value VARCHAR(100000) 
        );"""
    sql_command_bug = """CREATE TABLE Bug ( 
    workItemId INT(100), 
    System_Title VARCHAR(500),
    displayName VARCHAR(500),
    name VARCHAR(500),
    revisedDate VARCHAR(500),
    System_State VARCHAR(20), 
    System_Reason VARCHAR(30), 
    System_AreaPath VARCHAR(100), 
    System_IterationPath VARCHAR(100),
    Microsoft_VSTS_Common_Priority VARCHAR(100),
    Microsoft_VSTS_Common_Severity VARCHAR(10),
    Defect_ID VARCHAR(100),
    System_Description VARCHAR(20000),
    Microsoft_VSTS_TCM_ReproSteps VARCHAR(20000)
    );"""
    sql_command_pbi = """CREATE TABLE Product_Backlog_Item ( 
    workItemId INT(100), 
    System_Title VARCHAR(500),
    displayName VARCHAR(500),
    name VARCHAR(500),
    revisedDate VARCHAR(500),
    System_State VARCHAR(20), 
    System_Reason VARCHAR(30), 
    System_AreaPath VARCHAR(100), 
    System_IterationPath VARCHAR(100),
    Microsoft_VSTS_Common_Priority VARCHAR(100),
    Microsoft_VSTS_Common_ValueArea VARCHAR(100),
    System_Description VARCHAR(20000),
    Microsoft_VSTS_Common_AcceptanceCriteria VARCHAR(20000)
    );"""
    sql_command_tcase = """CREATE TABLE TestCase ( 
    workItemId INT(100), 
    System_Title VARCHAR(500),
    displayName VARCHAR(500),
    name VARCHAR(500),
    revisedDate VARCHAR(500),
    System_State VARCHAR(20), 
    System_Reason VARCHAR(30), 
    System_AreaPath VARCHAR(100), 
    System_IterationPath VARCHAR(100),
    Microsoft_VSTS_Common_Priority VARCHAR(100),
    Microsoft_VSTS_Common_ValueArea VARCHAR(100),
    Steps VARCHAR(20000),
    Automation VARCHAR(1000)
    );"""
    sql_command_task = """CREATE TABLE Task ( 
    workItemId INT(100), 
    System_Title VARCHAR(500),
    displayName VARCHAR(500),
    name VARCHAR(500),
    revisedDate VARCHAR(500),
    System_State VARCHAR(20), 
    System_Reason VARCHAR(30), 
    System_AreaPath VARCHAR(100), 
    System_IterationPath VARCHAR(100),
    Microsoft_VSTS_Common_Priority VARCHAR(100),
    System_Description VARCHAR(20000)
    );"""
    sql_command_issue = """CREATE TABLE Issue ( 
    workItemId INT(100), 
    System_Title VARCHAR(500),
    displayName VARCHAR(500),
    name VARCHAR(500),
    revisedDate VARCHAR(500),
    System_State VARCHAR(20), 
    System_Reason VARCHAR(30), 
    System_AreaPath VARCHAR(100), 
    System_IterationPath VARCHAR(100),
    Microsoft_VSTS_Common_Priority VARCHAR(100),
    System_Description VARCHAR(20000)
    );"""
    sql_command_feature = """CREATE TABLE Feature ( 
    workItemId INT(100), 
    System_Title VARCHAR(500),
    displayName VARCHAR(500),
    name VARCHAR(500),
    revisedDate VARCHAR(500),
    System_State VARCHAR(20), 
    System_Reason VARCHAR(30), 
    System_AreaPath VARCHAR(100), 
    System_IterationPath VARCHAR(100),
    Microsoft_VSTS_Common_Priority VARCHAR(100),
    Module_ID VARCHAR(100),
    Microsoft_VSTS_Common_ValueArea VARCHAR(100),
    System_Description VARCHAR(20000),
    Microsoft_VSTS_Common_AcceptanceCriteria VARCHAR(20000)
    );"""
    # execute the statement
    crsr.execute(sql_command_feature)
    crsr.execute(sql_command_task)
    crsr.execute(sql_command_tcase)
    crsr.execute(sql_command_pbi)
    crsr.execute(sql_command_bug)
    crsr.execute(sql_command_epic)
    crsr.execute(sql_command_us)
    crsr.execute(sql_command_issue)
    crsr.execute(sql_command_rel)
    crsr.execute(sql_command_revs)
    connection.commit()
        








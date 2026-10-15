-- =============================================
-- Author:		Compylo Ed-Tech Private Limited
-- Create date: February 2023
-- Description:	COMPYLO SQL Interview Questions
-- =============================================

-- Scenario 1
Select * from dbo.Max_Value_From_Table_1

SELECT Student_Name,
  (SELECT Avg(PC) FROM (VALUES (PC_Semester_1), (PC_Semester_2), (PC_Semester_3), (PC_Semester_4), 
   (PC_Semester_5), (PC_Semester_6)) AS value(PC)) as Maximum_Obtained_Percent
FROM dbo.Max_Value_From_Table_1


--Order by Maximum_Obtained_Percent DESC
--Can we take average of marks? yes!!!, use AVG

-------------------------------------------------------------------------------

-- Scenario 2 
---When All the items got delivered to each consumer? -- Use Max
-- When First Item was delivered to each consumer? -- Use Min

Select * from dbo.Max_Value_From_Table_2

SELECT Consumer_Name,
  (SELECT Max(Delivery_Date) FROM (VALUES (Date_Of_Delivery_iPhone), (Date_Of_Delivery_Laptop), (Date_Of_Delivery_SmartWatch))
  AS value(Delivery_Date)) as Delivery_Date
FROM dbo.Max_Value_From_Table_2

-- What if I use AVG() function? Error 
-- It shows that Average aggregation can't be used with this data type
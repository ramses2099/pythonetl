-- Create a new database called 'DatabaseName'
-- Connect to the 'master' database to run this snippet
USE master
GO
-- Create the new database if it does not exist already
IF NOT EXISTS (
    SELECT [name]
        FROM sys.databases
        WHERE [name] = N'ETL_DB'
)
CREATE DATABASE ETL_DB
GO

-- Connect to the newly created database
USE ETL_DB
GO

-- Connect to the newly created database
USE ETL_DB
GO

-- Date,Product_Category,Price,Discount,Customer_Segment,Marketing_Spend,Units_Sold

-- Create a new table called '[EcommerceSales]' in schema '[dbo]'
-- Drop the table if it already exists
IF OBJECT_ID('[dbo].[EcommerceSales]', 'U') IS NOT NULL
DROP TABLE [dbo].[EcommerceSales]
GO
-- Create the table in the specified schema
CREATE TABLE [dbo].[EcommerceSales]
(
    [Id] INT NOT NULL IDENTITY(1,1) PRIMARY KEY, -- Primary Key column
    [Date] VARCHAR(12) NOT NULL,
    [Product_Category] NVARCHAR(500) NOT NULL,
    [Price] DECIMAL(18,2) NOT NULL,
    [Discount] DECIMAL(18,2) NOT NULL,
    [Customer_Segment] NVARCHAR(500) NOT NULL,
    [Marketing_Spend] DECIMAL(18,2) NOT NULL,
    [Units_Sold] INT NOT NULL,
    [Total] DECIMAL(18,2) NOT NULL
    -- Specify more columns here
);
GO

SELECT COUNT(*) TOTAL FROM DBO.EcommerceSales;
SELECT * FROM dbo.EcommerceSales;
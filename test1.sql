-- Create a new table called 'booger_aids ' in schema 'SchemaName'
-- Drop the table if it already exists
IF OBJECT_ID('SchemaName.booger_aids ', 'U') IS NOT NULL
DROP TABLE SchemaName.booger_aids 
GO
-- Create the table in the specified schema
CREATE TABLE SchemaName.booger_aids 
(
    booger_aids Id INT NOT NULL PRIMARY KEY, -- primary key column
    Column1 [NVARCHAR](50) NOT NULL,
    Column2 [NVARCHAR](50) NOT NULL
    -- specify more columns here
);
GO
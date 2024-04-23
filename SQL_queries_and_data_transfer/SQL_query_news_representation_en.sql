SELECT * FROM final_project_ironhack.news_data_en_cleaned;

-- Creating new column
ALTER TABLE news_data_en_cleaned
ADD COLUMN female_mentions INT DEFAULT 0;

-- Checking there are entries containing the target keywords
SELECT *
FROM news_data_en_cleaned
WHERE 
    Title LIKE '%women%' OR
    Title LIKE '%woman%' OR
    Title LIKE '%ladies%' OR
    Title LIKE '%girl%' OR
    Title LIKE '%girls%' OR
    Title LIKE '%her%' OR
    Title LIKE '%she%' OR
    `Article Content` LIKE '%women%' OR
    `Article Content` LIKE '%woman%' OR
    `Article Content` LIKE '%ladies%' OR
    `Article Content` LIKE '%girl%' OR
    `Article Content` LIKE '%girls%' OR
    `Article Content` LIKE '%her%' OR
    `Article Content` LIKE '%she%' OR
    `Article Description` LIKE '%women%' OR
    `Article Description` LIKE '%woman%' OR
    `Article Description` LIKE '%ladies%' OR
    `Article Description` LIKE '%girl%' OR
    `Article Description` LIKE '%girls%' OR
    `Article Description` LIKE '%her%' OR
    `Article Description` LIKE '%she%';

-- Disabling MySQL safe update mode because we don't have a specific KEY column to use in the WHERE clause
SET SQL_SAFE_UPDATES = 0;

-- Update the new column with the count of female mentions
UPDATE news_data_en_cleaned
SET female_mentions = 
    (CASE 
        WHEN Title LIKE '%women%' THEN 1 ELSE 0 END +
    CASE 
        WHEN Title LIKE '%woman%' THEN 1 ELSE 0 END +
    CASE 
        WHEN Title LIKE '%ladies%' THEN 1 ELSE 0 END +
    CASE 
        WHEN Title LIKE '%girl%' THEN 1 ELSE 0 END +
    CASE 
        WHEN Title LIKE '%girls%' THEN 1 ELSE 0 END +
    CASE 
        WHEN Title LIKE '%her%' THEN 1 ELSE 0 END +
    CASE 
        WHEN Title LIKE '%she%' THEN 1 ELSE 0 END +
    CASE 
        WHEN `Article Content` LIKE '%women%' THEN 1 ELSE 0 END +
    CASE 
        WHEN `Article Content` LIKE '%woman%' THEN 1 ELSE 0 END +
    CASE 
        WHEN `Article Content` LIKE '%ladies%' THEN 1 ELSE 0 END +
    CASE 
        WHEN `Article Content` LIKE '%girl%' THEN 1 ELSE 0 END +
    CASE 
        WHEN `Article Content` LIKE '%girls%' THEN 1 ELSE 0 END +
    CASE 
        WHEN `Article Content` LIKE '%her%' THEN 1 ELSE 0 END +
    CASE 
        WHEN `Article Content` LIKE '%she%' THEN 1 ELSE 0 END +
    CASE 
        WHEN `Article Description` LIKE '%women%' THEN 1 ELSE 0 END +
    CASE 
        WHEN `Article Description` LIKE '%woman%' THEN 1 ELSE 0 END +
    CASE 
        WHEN `Article Description` LIKE '%ladies%' THEN 1 ELSE 0 END +
    CASE 
        WHEN `Article Description` LIKE '%girl%' THEN 1 ELSE 0 END +
    CASE 
        WHEN `Article Description` LIKE '%girls%' THEN 1 ELSE 0 END +
    CASE 
        WHEN `Article Description` LIKE '%her%' THEN 1 ELSE 0 END +
    CASE 
        WHEN `Article Description` LIKE '%she%' THEN 1 ELSE 0 END
    );

-- Verify the update
SELECT * FROM news_data_en_cleaned;

-- Creating new column
ALTER TABLE news_data_en_cleaned
ADD COLUMN male_mentions INT DEFAULT 0;

-- Update the new column with the count of male mentions
UPDATE news_data_en_cleaned 
SET male_mentions = (
    CASE WHEN Title LIKE '%men%' THEN 1 ELSE 0 END +
    CASE WHEN Title LIKE '%man%' THEN 1 ELSE 0 END +
    CASE WHEN Title LIKE '%guy%' THEN 1 ELSE 0 END +
    CASE WHEN Title LIKE '%he%' THEN 1 ELSE 0 END +
    CASE WHEN Title LIKE '%him%' THEN 1 ELSE 0 END +
    CASE WHEN Title LIKE '%his%' THEN 1 ELSE 0 END +
    CASE WHEN `Article Content` LIKE '%men%' THEN 1 ELSE 0 END +
    CASE WHEN `Article Content` LIKE '%man%' THEN 1 ELSE 0 END +
    CASE WHEN `Article Content` LIKE '%guy%' THEN 1 ELSE 0 END +
    CASE WHEN `Article Content` LIKE '%he%' THEN 1 ELSE 0 END +
    CASE WHEN `Article Content` LIKE '%him%' THEN 1 ELSE 0 END +
    CASE WHEN `Article Content` LIKE '%his%' THEN 1 ELSE 0 END +
    CASE WHEN `Article Description` LIKE '%men%' THEN 1 ELSE 0 END +
    CASE WHEN `Article Description` LIKE '%man%' THEN 1 ELSE 0 END +
    CASE WHEN `Article Description` LIKE '%guy%' THEN 1 ELSE 0 END +
    CASE WHEN `Article Description` LIKE '%he%' THEN 1 ELSE 0 END +
    CASE WHEN `Article Description` LIKE '%him%' THEN 1 ELSE 0 END +
    CASE WHEN `Article Description` LIKE '%his%' THEN 1 ELSE 0 END
);

-- Verify the update
SELECT * FROM news_data_en_cleaned;

-- Creating new column
ALTER TABLE news_data_en_cleaned
ADD COLUMN representation TEXT;

-- Update the new column with analysis of whether each article contains more male references, more female references, or an equal amount of male & female references.
UPDATE news_data_en_cleaned 
SET representation = (
    CASE 
        WHEN male_mentions > female_mentions THEN 'male'
        WHEN male_mentions < female_mentions THEN 'female'
        ELSE 'equal'
    END
);

-- Verify the update
SELECT * FROM news_data_en_cleaned;

SELECT * FROM final_project_ironhack.news_data_fr_cleaned;

-- Disabling MySQL safe update mode because we don't 
-- have a specific KEY column to use in the WHERE clause
SET SQL_SAFE_UPDATES = 0;

-- Creating new column
ALTER TABLE news_data_fr_cleaned
ADD COLUMN female_mentions INT DEFAULT 0;

-- Update the new column with the count of female mentions
UPDATE news_data_fr_cleaned
SET female_mentions = (
    CASE 
        WHEN Title LIKE '%femme%' THEN 1 ELSE 0 
    END +
    CASE 
        WHEN Title LIKE '%femmes%' THEN 1 ELSE 0 
    END +
    CASE 
        WHEN Title LIKE '%filles%' THEN 1 ELSE 0 
    END +
    CASE 
        WHEN Title LIKE '%fille%' THEN 1 ELSE 0 
    END +
    CASE 
        WHEN Title LIKE '%elle%' THEN 1 ELSE 0 
    END +
    CASE 
        WHEN `Article Content` LIKE '%femme%' THEN 1 ELSE 0 
    END +
    CASE 
        WHEN `Article Content` LIKE '%femmes%' THEN 1 ELSE 0 
    END +
    CASE 
        WHEN `Article Content` LIKE '%filles%' THEN 1 ELSE 0 
    END +
    CASE 
        WHEN `Article Content` LIKE '%fille%' THEN 1 ELSE 0 
    END +
    CASE 
        WHEN `Article Content` LIKE '%elle%' THEN 1 ELSE 0 
    END +
    CASE 
        WHEN `Article Description` LIKE '%femme%' THEN 1 ELSE 0 
    END +
    CASE 
        WHEN `Article Description` LIKE '%femmes%' THEN 1 ELSE 0 
    END +
    CASE 
        WHEN `Article Description` LIKE '%filles%' THEN 1 ELSE 0 
    END +
    CASE 
        WHEN `Article Description` LIKE '%fille%' THEN 1 ELSE 0 
    END +
    CASE 
        WHEN `Article Description` LIKE '%elle%' THEN 1 ELSE 0 
    END
);

-- Verify the update
SELECT * FROM news_data_fr_cleaned;

-- Creating new column
ALTER TABLE news_data_fr_cleaned
ADD COLUMN male_mentions INT DEFAULT 0;

-- Update the new column with the count of female mentions
UPDATE news_data_fr_cleaned
SET male_mentions = (
    CASE 
        WHEN Title LIKE '%homme%' THEN 1 ELSE 0 
    END +
    CASE 
        WHEN Title LIKE '%hommes%' THEN 1 ELSE 0 
    END +
    CASE 
        WHEN Title LIKE '%mec%' THEN 1 ELSE 0 
    END +
    CASE 
        WHEN Title LIKE '%lui%' THEN 1 ELSE 0 
    END +
    CASE 
        WHEN Title LIKE '%il%' THEN 1 ELSE 0 
    END +
    CASE 
        WHEN `Article Content` LIKE '%homme%' THEN 1 ELSE 0 
    END +
    CASE 
        WHEN `Article Content` LIKE '%hommes%' THEN 1 ELSE 0 
    END +
    CASE 
        WHEN `Article Content` LIKE '%mec%' THEN 1 ELSE 0 
    END +
    CASE 
        WHEN `Article Content` LIKE '%lui%' THEN 1 ELSE 0 
    END +
    CASE 
        WHEN `Article Content` LIKE '%il%' THEN 1 ELSE 0 
    END +
    CASE 
        WHEN `Article Description` LIKE '%homme%' THEN 1 ELSE 0 
    END +
    CASE 
        WHEN `Article Description` LIKE '%hommes%' THEN 1 ELSE 0 
    END +
    CASE 
        WHEN `Article Description` LIKE '%mec%' THEN 1 ELSE 0 
    END +
    CASE 
        WHEN `Article Description` LIKE '%lui%' THEN 1 ELSE 0 
    END +
    CASE 
        WHEN `Article Description` LIKE '%il%' THEN 1 ELSE 0 
    END
);

-- Verify the update
SELECT * FROM news_data_fr_cleaned;

-- Creating new column
ALTER TABLE news_data_fr_cleaned
ADD COLUMN representation TEXT;

-- Update the new column with analysis of whether each article contains more male 
-- references, more female references, or an equal amount of male & female references.
UPDATE news_data_fr_cleaned 
SET representation = (
    CASE 
        WHEN male_mentions > female_mentions THEN 'male'
        WHEN male_mentions < female_mentions THEN 'female'
        ELSE 'equal'
    END
);

-- Verify the update
SELECT * FROM news_data_en_cleaned;

-- Add the new column without a default value
ALTER TABLE bike_info_women
ADD COLUMN gender TEXT;

-- Update all existing rows with the default value 'male'
UPDATE bike_info_women
SET gender = 'female';

SELECT * FROM bike_info_women;

SELECT * FROM final_project_ironhack.bike_info_men;

-- Add the new column without a default value
ALTER TABLE bike_info_men
ADD COLUMN gender TEXT;

UPDATE bike_info_men
SET gender = 'male';

SELECT * FROM bike_info_men;

-- Commit the changes to the database
COMMIT;
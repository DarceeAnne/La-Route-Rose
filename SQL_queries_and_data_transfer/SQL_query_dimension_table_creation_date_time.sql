-- Create dim_jour
CREATE TABLE final_project_ironhack.dim_jour (
    jour INT PRIMARY KEY
);

-- Populate dim_jour
INSERT INTO final_project_ironhack.dim_jour (jour)
SELECT DISTINCT jour
FROM (
    SELECT jour FROM caracteristiques_2019
    UNION ALL
    SELECT jour FROM caracteristiques_2020
    UNION ALL
    SELECT jour FROM caracteristiques_2021
    UNION ALL
    SELECT jour FROM caracteristiques_2022
) AS jours;

-- Create dim_mois
CREATE TABLE final_project_ironhack.dim_mois (
    mois INT PRIMARY KEY
);

-- Populate dim_mois
INSERT INTO final_project_ironhack.dim_mois (mois)
SELECT DISTINCT mois
FROM (
    SELECT mois FROM caracteristiques_2019
    UNION ALL
    SELECT mois FROM caracteristiques_2020
    UNION ALL
    SELECT mois FROM caracteristiques_2021
    UNION ALL
    SELECT mois FROM caracteristiques_2022
) AS mois;

-- Create dim_year
CREATE TABLE final_project_ironhack.dim_year (
    an YEAR PRIMARY KEY
);

-- Populate dim_year
INSERT INTO final_project_ironhack.dim_year (an)
SELECT DISTINCT an
FROM (
    SELECT an FROM caracteristiques_2019
    UNION ALL
    SELECT an FROM caracteristiques_2020
    UNION ALL
    SELECT an FROM caracteristiques_2021
    UNION ALL
    SELECT an FROM caracteristiques_2022
) AS an;

-- Create dim_hhmm
CREATE TABLE final_project_ironhack.dim_hhmm (
    hhmm TIME PRIMARY KEY
);

-- Populate dim_hhmm
INSERT INTO final_project_ironhack.dim_hhmm (hhmm)
SELECT DISTINCT hrmn AS hhmm
FROM (
    SELECT hrmn FROM caracteristiques_2019
    UNION ALL
    SELECT hrmn FROM caracteristiques_2020
    UNION ALL
    SELECT hrmn FROM caracteristiques_2021
    UNION ALL
    SELECT hrmn FROM caracteristiques_2022
) AS hhmm;

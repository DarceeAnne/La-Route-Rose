
CREATE TABLE final_project_ironhack.dim_accident_id (
    Num_Acc BIGINT PRIMARY KEY
);
INSERT INTO final_project_ironhack.dim_accident_id (Num_Acc) 
SELECT Num_Acc 
FROM (
    SELECT Num_Acc FROM caracteristiques_2019
    UNION ALL
    SELECT Num_Acc FROM caracteristiques_2020
    UNION ALL
    SELECT Num_Acc FROM caracteristiques_2021
    UNION ALL
    SELECT Accident_Id AS Num_Acc FROM caracteristiques_2022
) AS combined_data;






SELECT * FROM final_project_ironhack.comptage_velo_donnees_compteurs;

SELECT `Identifiant du site de comptage`, `Nom du site de comptage`, SUM(`Comptage horaire`) AS total_comptage
FROM comptage_velo_donnees_compteurs
GROUP BY `Identifiant du site de comptage`, `Nom du site de comptage`
ORDER BY total_comptage DESC;



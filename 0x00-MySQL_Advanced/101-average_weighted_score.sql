--SQL script that creates a stored procedure ComputeAverageWeightedScoreForUsers
--that computes and store the average weighted score for all students.
DELIMITER //

CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
    UPDATE users u
    JOIN (
        SELECT c.user_id, SUM(c.score * p.weight) / SUM(p.weight) AS avg_weighted_score
        FROM corrections c
        JOIN projects p ON c.project_id = p.id
        GROUP BY c.user_id
    ) AS temp ON u.id = temp.user_id
    SET u.average_score = temp.avg_weighted_score;
END //

DELIMITER ;

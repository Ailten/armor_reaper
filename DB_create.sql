

USE `armor_reaper`;

DROP TABLE IF EXISTS `users`;
CREATE TABLE `users` (
    `id` int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `e_mail` varchar(100) NOT NULL unique,
    `password` varchar(255) NOT NULL,
    `pseudo` varchar(100) NOT NULL DEFAULT "Anon"
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

INSERT INTO `users` (`e_mail`, `password`, `pseudo`) VALUES 
("ailten@hotmail.com", "test1234", "Ailten");
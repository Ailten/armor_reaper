

USE `armor_reaper`;

DROP TABLE IF EXISTS `users`;
CREATE TABLE `users` (
    `id` int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `e_mail` varchar(100) NOT NULL unique,
    `password` char(60) NOT NULL,  -- 60 for bcrypt.
    `pseudo` varchar(100) NOT NULL DEFAULT "Anon"
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

INSERT INTO `users` (`e_mail`, `password`, `pseudo`) VALUES 
("ailten@hotmail.com", "$2b$12$Q2uSukmD2EHI.d1/xbryOeJ1Rh8GBVf1DXawwROWTnxH9QAVelFd2", "Ailten");  -- password raw = "test".
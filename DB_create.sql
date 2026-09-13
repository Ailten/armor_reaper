

USE `armor_reaper`;

DROP TABLE IF EXISTS `users`;
CREATE TABLE `users` (
    `id` int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `e_mail` varchar(100) NOT NULL unique,
    `password` char(60) NOT NULL,  -- 60 for bcrypt.
    `pseudo` varchar(100) NOT NULL unique,

    `adventurer_allow` int not null default 3,
    `gold` int not null default 0,
    `energy` TINYINT not null default 10,
    `energy_max` TINYINT not null default 10
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

INSERT INTO `users` (`e_mail`, `password`, `pseudo`) VALUES 
("ailten@hotmail.com", "$2b$12$Q2uSukmD2EHI.d1/xbryOeJ1Rh8GBVf1DXawwROWTnxH9QAVelFd2", "Ailten");  -- password raw = "test".


DROP TABLE IF EXISTS `adventurers`;
CREATE TABLE `adventurers` (
    `id` int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `id_user` int(11) not null,
    CONSTRAINT `fk_user`
        FOREIGN KEY (`id_user`)
        REFERENCES `users`(`id`)
        ON DELETE CASCADE,
    `pseudo` varchar(100) NOT NULL unique
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

INSERT INTO `adventurers` (`id_user`, `pseudo`) VALUES 
("1", "Ailten");

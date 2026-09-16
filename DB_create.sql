

USE `armor_reaper`;

DROP TABLE IF EXISTS `join_adventurer_tree_skills`;
DROP TABLE IF EXISTS `adventurers`;
DROP TABLE IF EXISTS `users`;
DROP TABLE IF EXISTS `tree_skills`;

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

INSERT INTO `users` (`id`, `e_mail`, `password`, `pseudo`) VALUES 
("1", "ailten@hotmail.com", "$2b$12$Q2uSukmD2EHI.d1/xbryOeJ1Rh8GBVf1DXawwROWTnxH9QAVelFd2", "Ailten");  -- password raw = "test".


CREATE TABLE `tree_skills` (
    `id` int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `name` varchar(100) NOT NULL unique
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

INSERT INTO `tree_skills` (`id`, `name`) VALUES 
("1", "Mercenary"),
("2", "Mage"),
("3", "Meka");


CREATE TABLE `adventurers` (
    `id` int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `id_user` int(11) not null,
    CONSTRAINT `fk_user`
        FOREIGN KEY (`id_user`)
        REFERENCES `users`(`id`)
        ON DELETE CASCADE,
    `pseudo` varchar(100) NOT NULL unique,

    `lvl` int not null default 1,
    `xp` smallint not null default 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

INSERT INTO `adventurers` (`id`, `id_user`, `pseudo`) VALUES 
("1", "1", "Ailten");


CREATE TABLE `join_adventurer_tree_skills` (
    `id_adventurer` int(11) not null,
    `id_tree_skill` int(11) not null,
    CONSTRAINT `fk_adv`
        FOREIGN KEY (`id_adventurer`)
        REFERENCES `adventurers`(`id`)
        ON DELETE CASCADE,
    CONSTRAINT `fk_tree_skill`
        FOREIGN KEY (`id_tree_skill`)
        REFERENCES `tree_skills`(`id`)
        ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

INSERT INTO `join_adventurer_tree_skills` (`id_adventurer`, `id_tree_skill`) VALUES 
("1", "1");


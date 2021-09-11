/*
SQLyog Ultimate v12.5.0 (64 bit)
MySQL - 8.0.16 : Database - python
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
USE `python`;

/*Table structure for table `all_ssqdata` */

DROP TABLE IF EXISTS `all_ssqdata`;

CREATE TABLE `all_ssqdata` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `red01` int(11) DEFAULT NULL,
  `red02` int(11) DEFAULT NULL,
  `red03` int(11) DEFAULT NULL,
  `red04` int(11) DEFAULT NULL,
  `red05` int(11) DEFAULT NULL,
  `red06` int(11) DEFAULT NULL,
  `blue01` int(11) DEFAULT NULL,
  `allNum` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`),
  FULLTEXT KEY `ALLNUM` (`allNum`)
) ENGINE=InnoDB AUTO_INCREMENT=18300621 DEFAULT CHARSET=utf8 COMMENT='双色球全数据表';

/*Table structure for table `analyze_index` */

DROP TABLE IF EXISTS `analyze_index`;

CREATE TABLE `analyze_index` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '主键',
  `all_ssq_id` int(11) DEFAULT NULL COMMENT '双色球全数据表ID',
  `odd_even_ratio` float(5,2) DEFAULT NULL COMMENT '奇偶比',
  `big_small_ratio` float(5,2) DEFAULT NULL COMMENT '大小比',
  `prime_number_count` int(2) DEFAULT NULL COMMENT '质数个数',
  `sum_value` int(3) DEFAULT NULL COMMENT '和值',
  `loose_value` int(2) DEFAULT NULL COMMENT '散度值',
  `ac_value` int(11) DEFAULT NULL COMMENT 'AC值',
  `one_section` int(2) DEFAULT NULL COMMENT '一区间个数',
  `two_section` int(2) DEFAULT NULL COMMENT '二区间个数',
  `three_section` int(2) DEFAULT NULL COMMENT '三区间个数',
  `consective_num_index` int(4) DEFAULT NULL COMMENT '连号类型(无连号为0；1组2连号12；1组3连号13；1组4连号14；1组5连号15；1组6连号16；2组2连号22；2组3连号23；3组2连号32；1组2连号+1组3连号1213；1组2连号+1组4连号1214)',
  `all_num` varchar(30) DEFAULT NULL COMMENT '所有号码以逗号连接',
  PRIMARY KEY (`id`),
  KEY `PK_ALL_ID` (`all_ssq_id`),
  KEY `con_odd_event` (`odd_even_ratio`),
  KEY `con_big_small` (`big_small_ratio`),
  KEY `con_prime` (`prime_number_count`),
  KEY `con_sum` (`sum_value`),
  KEY `con_loose` (`loose_value`),
  KEY `con_ac` (`ac_value`),
  KEY `con_one_section` (`one_section`),
  KEY `con_two_section` (`two_section`),
  KEY `con_three_section` (`three_section`),
  KEY `con_consective_num_index` (`consective_num_index`),
  CONSTRAINT `PK_ALL_ID` FOREIGN KEY (`all_ssq_id`) REFERENCES `all_ssqdata` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=17846139 DEFAULT CHARSET=utf8 COMMENT='分析指标表';

/*Table structure for table `analyze_index_section` */

DROP TABLE IF EXISTS `analyze_index_section`;

CREATE TABLE `analyze_index_section` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `one_section` int(2) DEFAULT NULL COMMENT '一区间个数',
  `two_section` int(2) DEFAULT NULL COMMENT '二区间个数',
  `three_section` int(2) DEFAULT NULL COMMENT '三区间个数',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Table structure for table `auth_group` */

DROP TABLE IF EXISTS `auth_group`;

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Table structure for table `auth_group_permissions` */

DROP TABLE IF EXISTS `auth_group_permissions`;

CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Table structure for table `auth_permission` */

DROP TABLE IF EXISTS `auth_permission`;

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Table structure for table `auth_user` */

DROP TABLE IF EXISTS `auth_user`;

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Table structure for table `auth_user_groups` */

DROP TABLE IF EXISTS `auth_user_groups`;

CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Table structure for table `auth_user_user_permissions` */

DROP TABLE IF EXISTS `auth_user_user_permissions`;

CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Table structure for table `blue_losing_lottery` */

DROP TABLE IF EXISTS `blue_losing_lottery`;

CREATE TABLE `blue_losing_lottery` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `termnum` char(8) DEFAULT NULL,
  `num_01` int(2) DEFAULT NULL,
  `num_02` int(2) DEFAULT NULL,
  `num_03` int(2) DEFAULT NULL,
  `num_04` int(2) DEFAULT NULL,
  `num_05` int(2) DEFAULT NULL,
  `num_06` int(2) DEFAULT NULL,
  `num_07` int(2) DEFAULT NULL,
  `num_08` int(2) DEFAULT NULL,
  `num_09` int(2) DEFAULT NULL,
  `num_10` int(2) DEFAULT NULL,
  `num_11` int(2) DEFAULT NULL,
  `num_12` int(2) DEFAULT NULL,
  `num_13` int(2) DEFAULT NULL,
  `num_14` int(2) DEFAULT NULL,
  `num_15` int(2) DEFAULT NULL,
  `num_16` int(2) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2748 DEFAULT CHARSET=utf8;

/*Table structure for table `blue_occur_num` */

DROP TABLE IF EXISTS `blue_occur_num`;

CREATE TABLE `blue_occur_num` (
  `id` int(2) NOT NULL,
  `num` int(5) DEFAULT NULL,
  `amount` int(5) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Table structure for table `django_admin_log` */

DROP TABLE IF EXISTS `django_admin_log`;

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Table structure for table `django_content_type` */

DROP TABLE IF EXISTS `django_content_type`;

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Table structure for table `django_migrations` */

DROP TABLE IF EXISTS `django_migrations`;

CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Table structure for table `long_dhr` */

DROP TABLE IF EXISTS `long_dhr`;

CREATE TABLE `long_dhr` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `num` int(2) DEFAULT NULL,
  `appear_1` int(4) DEFAULT NULL COMMENT '连续出现1期',
  `appear_2` int(4) DEFAULT NULL COMMENT '连续出现2期',
  `appear_3` int(4) DEFAULT NULL COMMENT '连续出现3期',
  `appear_4` int(4) DEFAULT NULL COMMENT '连续出现4期',
  `appear_5` int(4) DEFAULT NULL COMMENT '连续出现5期',
  `dhr` float(3,2) DEFAULT NULL COMMENT '出现一期的次数/两期以上的次数',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=34 DEFAULT CHARSET=utf8;

/*Table structure for table `mid_all_ssqdata` */

DROP TABLE IF EXISTS `mid_all_ssqdata`;

CREATE TABLE `mid_all_ssqdata` (
  `id` int(11) DEFAULT NULL,
  `num` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Table structure for table `pair_num` */

DROP TABLE IF EXISTS `pair_num`;

CREATE TABLE `pair_num` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `pair_num` varchar(10) DEFAULT NULL COMMENT '成对号',
  `pair_count` int(11) DEFAULT NULL COMMENT '出现次数',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=529 DEFAULT CHARSET=utf8;

/*Table structure for table `red_losing_lottery` */

DROP TABLE IF EXISTS `red_losing_lottery`;

CREATE TABLE `red_losing_lottery` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `termnum` char(8) DEFAULT NULL,
  `num_01` int(2) DEFAULT NULL,
  `num_02` int(2) DEFAULT NULL,
  `num_03` int(2) DEFAULT NULL,
  `num_04` int(2) DEFAULT NULL,
  `num_05` int(2) DEFAULT NULL,
  `num_06` int(2) DEFAULT NULL,
  `num_07` int(2) DEFAULT NULL,
  `num_08` int(2) DEFAULT NULL,
  `num_09` int(2) DEFAULT NULL,
  `num_10` int(2) DEFAULT NULL,
  `num_11` int(2) DEFAULT NULL,
  `num_12` int(2) DEFAULT NULL,
  `num_13` int(2) DEFAULT NULL,
  `num_14` int(2) DEFAULT NULL,
  `num_15` int(2) DEFAULT NULL,
  `num_16` int(2) DEFAULT NULL,
  `num_17` int(2) DEFAULT NULL,
  `num_18` int(2) DEFAULT NULL,
  `num_19` int(2) DEFAULT NULL,
  `num_20` int(2) DEFAULT NULL,
  `num_21` int(2) DEFAULT NULL,
  `num_22` int(2) DEFAULT NULL,
  `num_23` int(2) DEFAULT NULL,
  `num_24` int(2) DEFAULT NULL,
  `num_25` int(2) DEFAULT NULL,
  `num_26` int(2) DEFAULT NULL,
  `num_27` int(2) DEFAULT NULL,
  `num_28` int(2) DEFAULT NULL,
  `num_29` int(2) DEFAULT NULL,
  `num_30` int(2) DEFAULT NULL,
  `num_31` int(2) DEFAULT NULL,
  `num_32` int(2) DEFAULT NULL,
  `num_33` int(2) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2748 DEFAULT CHARSET=utf8;

/*Table structure for table `selected_ssqdata` */

DROP TABLE IF EXISTS `selected_ssqdata`;

CREATE TABLE `selected_ssqdata` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `red01` int(11) DEFAULT NULL,
  `red02` int(11) DEFAULT NULL,
  `red03` int(11) DEFAULT NULL,
  `red04` int(11) DEFAULT NULL,
  `red05` int(11) DEFAULT NULL,
  `red06` int(11) DEFAULT NULL,
  `blue01` int(11) DEFAULT NULL,
  `termnum` int(10) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=108 DEFAULT CHARSET=utf8 COMMENT='双色球已选号数据表';

/*Table structure for table `selected_ssqdata_history` */

DROP TABLE IF EXISTS `selected_ssqdata_history`;

CREATE TABLE `selected_ssqdata_history` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `red01` int(11) DEFAULT NULL,
  `red02` int(11) DEFAULT NULL,
  `red03` int(11) DEFAULT NULL,
  `red04` int(11) DEFAULT NULL,
  `red05` int(11) DEFAULT NULL,
  `red06` int(11) DEFAULT NULL,
  `blue01` int(11) DEFAULT NULL,
  `data_flg` char(1) DEFAULT NULL COMMENT '1:当期数据,0:往期数据',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='双色球已选号数据表历史';

/*Table structure for table `ssqdata` */

DROP TABLE IF EXISTS `ssqdata`;

CREATE TABLE `ssqdata` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `openDate` date DEFAULT NULL COMMENT '开奖日期',
  `termNum` varchar(10) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL COMMENT '期号',
  `red01` int(11) DEFAULT NULL,
  `red02` int(11) DEFAULT NULL,
  `red03` int(11) DEFAULT NULL,
  `red04` int(11) DEFAULT NULL,
  `red05` int(11) DEFAULT NULL,
  `red06` int(11) DEFAULT NULL,
  `blue01` int(11) DEFAULT NULL,
  `hashcode` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `HASHCODE_KEY` (`hashcode`)
) ENGINE=InnoDB AUTO_INCREMENT=2748 DEFAULT CHARSET=utf8 COMMENT='双色球开奖数据表';

/*Table structure for table `thriple_num` */

DROP TABLE IF EXISTS `thriple_num`;

CREATE TABLE `thriple_num` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `thriple_num` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL COMMENT '一组三个号码',
  `thriple_count` int(10) DEFAULT NULL COMMENT '出现次数',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5457 DEFAULT CHARSET=utf8;

/* Procedure structure for procedure `insertMidAllSSQData` */

/*!50003 DROP PROCEDURE IF EXISTS  `insertMidAllSSQData` */;

DELIMITER $$

/*!50003 CREATE DEFINER=`root`@`localhost` PROCEDURE `insertMidAllSSQData`()
BEGIN
		
		DECLARE i INT DEFAULT 1;
		WHILE i<=17721088 DO
			INSERT INTO `analyze_index` (all_num) SELECT concat('#',red01,'#',red02,'#',red03,'#',red04,'#',red05,'#',red06) FROM `all_ssqdata` WHERE  id = i;
			
		    SET i=i+1;
		END WHILE;
	END */$$
DELIMITER ;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

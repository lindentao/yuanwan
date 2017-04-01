/*
 Navicat Premium Data Transfer

 Source Server         : 14.215.135.16
 Source Server Type    : MySQL
 Source Server Version : 50612
 Source Host           : 14.215.135.16
 Source Database       : yuanwan_db

 Target Server Type    : MySQL
 Target Server Version : 50612
 File Encoding         : utf-8

 Date: 03/31/2017 15:12:49 PM
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
--  Table structure for `t_article_info`
-- ----------------------------
DROP TABLE IF EXISTS `t_article_info`;
CREATE TABLE `t_article_info` (
	`id` int(11) UNSIGNED NOT NULL AUTO_INCREMENT,
	`name` varchar(32) NOT NULL DEFAULT '' COMMENT '文章名',
	`body` text NOT NULL COMMENT '正文',
	`status` tinyint(2) UNSIGNED NOT NULL DEFAULT 0 COMMENT '状态',
	`ctime` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
	`mtime` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '修改时间',
	PRIMARY KEY (`id`),
	UNIQUE `name` (`name`) comment ''
) ENGINE=`InnoDB` AUTO_INCREMENT=1 DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci ROW_FORMAT=COMPACT COMMENT='' CHECKSUM=0 DELAY_KEY_WRITE=0;

-- ----------------------------
--  Table structure for `t_category_info`
-- ----------------------------
DROP TABLE IF EXISTS `t_category_info`;
CREATE TABLE `t_category_info` (
	`id` int(11) UNSIGNED NOT NULL AUTO_INCREMENT,
	`name` varchar(32) NOT NULL DEFAULT '' COMMENT '分类名',
	`ctime` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
	PRIMARY KEY (`id`),
	UNIQUE `name` (`name`) comment ''
) ENGINE=`InnoDB` AUTO_INCREMENT=1 DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci ROW_FORMAT=COMPACT COMMENT='' CHECKSUM=0 DELAY_KEY_WRITE=0;

-- ----------------------------
--  Table structure for `t_goods_image`
-- ----------------------------
DROP TABLE IF EXISTS `t_goods_image`;
CREATE TABLE `t_goods_image` (
	`id` int(11) UNSIGNED NOT NULL AUTO_INCREMENT,
	`goods_id` int(11) NOT NULL COMMENT '商品ID',
	`image_id` int(11) NOT NULL COMMENT '图片ID',
	PRIMARY KEY (`id`)
) ENGINE=`InnoDB` AUTO_INCREMENT=1 DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci ROW_FORMAT=COMPACT COMMENT='' CHECKSUM=0 DELAY_KEY_WRITE=0;

-- ----------------------------
--  Table structure for `t_goods_info`
-- ----------------------------
DROP TABLE IF EXISTS `t_goods_info`;
CREATE TABLE `t_goods_info` (
	`id` int(11) UNSIGNED NOT NULL AUTO_INCREMENT,
	`category_id` int(11) UNSIGNED NOT NULL COMMENT '类别ID',
	`name` varchar(32) NOT NULL DEFAULT '' COMMENT '名字',
	`origin` varchar(32) DEFAULT '' COMMENT '来源',
	`color` varchar(32) DEFAULT '' COMMENT '颜色',
	`material` varchar(32) DEFAULT '' COMMENT '材料',
	`size` varchar(32) DEFAULT '' COMMENT '尺寸',
	`ctime` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
	`mtime` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '修改时间',
	PRIMARY KEY (`id`),
	CONSTRAINT `t_goods_info_ibfk_1` FOREIGN KEY (`category_id`) REFERENCES `t_category_info` (`id`),
	UNIQUE `name` (`name`) comment '',
	UNIQUE `category_id` (`category_id`) comment ''
) ENGINE=`InnoDB` AUTO_INCREMENT=1 DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci ROW_FORMAT=COMPACT COMMENT='' CHECKSUM=0 DELAY_KEY_WRITE=0;

-- ----------------------------
--  Table structure for `t_image_info`
-- ----------------------------
DROP TABLE IF EXISTS `t_image_info`;
CREATE TABLE `t_image_info` (
	`id` int(11) UNSIGNED NOT NULL AUTO_INCREMENT,
	`name` varchar(32) NOT NULL DEFAULT '' COMMENT '名字',
	`path` varchar(64) NOT NULL DEFAULT '' COMMENT '路径',
	PRIMARY KEY (`id`)
) ENGINE=`InnoDB` AUTO_INCREMENT=1 DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci ROW_FORMAT=COMPACT COMMENT='' CHECKSUM=0 DELAY_KEY_WRITE=0;

SET FOREIGN_KEY_CHECKS = 1;

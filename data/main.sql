/*
Navicat SQLite Data Transfer

Source Server         : yzcyjc
Source Server Version : 30808
Source Host           : :0

Target Server Type    : SQLite
Target Server Version : 30808
File Encoding         : 65001

Date: 2022-07-30 18:59:23
*/

PRAGMA foreign_keys = OFF;

-- ----------------------------
-- Table structure for AV
-- ----------------------------
DROP TABLE IF EXISTS "main"."AV";
CREATE TABLE "AV" (
"ID"  INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
"NAME"  TEXT(10) NOT NULL,
"SHA256"  TEXT(256) NOT NULL,
UNIQUE ("SHA256" ASC)
);

-- ----------------------------
-- Records of AV
-- ----------------------------

-- ----------------------------
-- Table structure for sqlite_sequence
-- ----------------------------
DROP TABLE IF EXISTS "main"."sqlite_sequence";
CREATE TABLE sqlite_sequence(name,seq);

-- ----------------------------
-- Records of sqlite_sequence
-- ----------------------------
INSERT INTO "main"."sqlite_sequence" VALUES ('AV', null);

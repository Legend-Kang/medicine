BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "pill_detection_pillinformation" (
	"id"	INTEGER PRIMARY KEY AUTOINCREMENT,
	"name"	varchar(100) NOT NULL,
	"corporation"	varchar(100) NOT NULL,
	"effect"	varchar(700) NOT NULL,
	"dosage"	varchar(100) NOT NULL,
	"shape"	varchar(50),
	"char"	varchar(50),
	"color"	varchar(50)
);
INSERT INTO "pill_detection_pillinformation" VALUES (1,'다우제큐정','미래제약','소화불량, 식욕감퇴(식욕부진), 과식, 체함, 소화촉진, 소화불량으로 인한 위부팽만감','만 15세 이상 및 성인 : 1회 2정, 1일 3회 식후에 복용한다. ','circle','mDUR','green');
COMMIT;


1	다우제큐정	미래제약	소화불량, 식욕감퇴(식욕부진), 과식, 체함, 소화촉진, 소화불량으로 인한 위부팽만감	만 15세 이상 및 성인 : 1회 2정, 1일 3회 식후에 복용한다. 	circle	mDUR	green
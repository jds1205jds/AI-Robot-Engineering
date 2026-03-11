-- Person 테이블 생성
CREATE TABLE "Person" (
	"ID"	INTEGER NOT NULL,
	"Name"	TEXT NOT NULL,
	"Birthday"	TEXT,
	PRIMARY KEY("ID" AUTOINCREMENT)
);

-- 검색
SELECT * FROM Person;

INSERT INTO Person
VALUES (2, '강호동', '2000-08-08' );

-- 삽입
INSERT INTO Person (ID, Name, Birthday)
VALUES (3, '유재석', '1999-01-01')

-- 조회
SELECT * FROM Person;

-- 오름차순 조회
SELECT Name, Birthday FROM Person
ORDER BY Birthday ASC;

-- 역순출력
SELECT Name FROM Person ORDER BY Name DESC; 

-- 삭제
DELETE FROM Person
WHERE ID = 1;
DELETE FROM Person WHERE Name='신동엽';


-- 업데이트
UPDATE Person SET Name='강감찬' WHERE ID=2;
UPDATE Person SET Name = '김혜리'
WHERE Name = '이혜리'

-- 집게함수
SELECT count(Height), 
	max(Height), 
	min(Height), 
	avg(Height),
	sum(Height) 
FROM Person;


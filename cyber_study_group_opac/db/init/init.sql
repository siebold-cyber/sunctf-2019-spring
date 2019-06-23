SET CHARSET UTF8;

DROP SCHEMA IF EXISTS opac;
CREATE SCHEMA opac DEFAULT CHARACTER SET utf8;
USE opac;

DROP TABLE IF EXISTS books;
CREATE TABLE books
(
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(128) NOT NULL,
  `author` varchar(64) NOT NULL,
  `ISBN` char(17) NOT NULL,
  PRIMARY KEY (`id`)
);

SET CHARACTER_SET_CLIENT = utf8;
SET CHARACTER_SET_CONNECTION = utf8;

INSERT INTO books (name, author, ISBN) VALUES
  ("Angularアプリケーションプログラミング", "山田祥寛", "978-4-7741-9130-0"),
  ("Docker/Kubernetes 実践コンテナ開発入門", "山田明憲", "978-4-297-10033-9"),
  ("Python セキュリティプログラミング", "森幹太", "978-4-8399-6850-2"),
  ("Vue.js 入門", "川口和也", "978-4-2971-0091-9"),
  ("安全なWebアプリケーションの作り方", "徳丸浩", "978-4-7973-9316-3"),
  ("OpenStack 実践ガイド", "古賀政純", "978-4-8443-8126-6"),
  ("Ansible実践ガイド", "北山晋吾", "978-4-2950-0327-4"),
  ("基礎からわかる Elm", "鳥居陽介", "978-4-8635-4222-8"),
  ("分散システムデザインパターン", "Brendan Burns", "978-4-8731-1875-8"),
  ("Go言語によるWebアプリケーション開発", "Mat Ryer", "978-4-8731-1752-2"),
  ("入門 監視", "Mike Julian", "978-4-8731-1864-2"),
  ("AWSによるサーバーレスアーキテクチャ", "Peter Sbarski", "978-4-7981-5516-6");

DROP TABLE IF EXISTS flags;
CREATE TABLE flags
(
  `flag` varchar(128) NOT NULL
);

INSERT INTO flags (flag) VALUES ("SUNCTF{b3_c4r3fu1_s91_p4r4m373rs}");

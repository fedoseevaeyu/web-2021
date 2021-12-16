USE Applications;

CREATE TABLE dbo.App
(
	ID_app INT IDENTITY(1, 1) CONSTRAINT pk_app PRIMARY KEY,
	Application_name NVARCHAR(100),
	Developer NVARCHAR(100),
	ID_language INT
);

CREATE TABLE dbo.Prog_language
(
	ID_language INT IDENTITY(1, 1) CONSTRAINT pk_language PRIMARY KEY,
	Language_name NVARCHAR(100),
	Descript NVARCHAR(1000),
	Creation_year INT
);

ALTER TABLE dbo.App
ADD CONSTRAINT fk_app_lang
FOREIGN KEY (ID_language) REFERENCES Prog_language(ID_language)

INSERT INTO dbo.Prog_language SELECT 'C++', 'C++ is the best programming language!', 1983 UNION ALL SELECT 'Python', 'Python is often ised for machine learning.', 1991
INSERT INTO dbo.App SELECT 'Adobe Photoshop', 'Adobe', 1 UNION ALL SELECT 'Instagram', 'Meta', 2

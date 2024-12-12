CREATE DATABASE Video_games;
USE video_games;
SELECT *
FROM videogames_final_projects
WHERE genre = "action" AND platform LIKE "ps%";

SELECT *
FROM videogames_final_projects
WHERE publisher = "activision" AND genre = "shooter";

SELECT name, platform, genre, year, publisher, global_sales
FROM videogames_final_projects
WHERE year = 2014
AND global_sales = (SELECT MAX(global_sales) AS max_sales
FROM videogames_final_projects
WHERE year =  2014);

SELECT name, platform, genre, year, publisher, global_sales
FROM videogames_final_projects
WHERE genre = "shooter"
AND global_sales = (SELECT MAX(global_sales) AS max_sales
FROM videogames_final_projects
WHERE genre = "shooter");

SELECT name, platform, genre, year, publisher, global_sales
FROM videogames_final_projects
WHERE genre = "action"
AND global_sales = (SELECT MIN(global_sales) AS max_sales
FROM videogames_final_projects
WHERE genre = "action");

SELECT *
FROM videogames_final_projects 
WHERE genre = "shooter"
AND `%_sales_Global` = (SELECT MAX(`%_sales_global`)
FROM videogames_final_projects
WHERE genre = "shooter");

SELECT *
FROM videogames_final_projects 
WHERE `%_sales_Global` = (SELECT MAX(`%_sales_Global`)
FROM videogames_final_projects);



SELECT * 
FROM videogames_final_projects
WHERE publisher IN (
    SELECT publisher
    FROM videogames_final_projects
    GROUP BY publisher
    HAVING COUNT(publisher) = 1
);

SELECT * 
FROM videogames_final_projects
WHERE publisher IN ("Yumedia",
"Xing Entertainment",
"Wizard Video Games",
"White Park Bay Software",
"Westwood Studios",
"WayForward Technologies",
"Warp",
"Wargaming.net",
"Warashi",
"Visco",
"Vap",
"Valve",
"Universal Gamex",
"UEP Systems",
"Type-Moon",
"TYO",
"Tryfirst",
"Tripwire Interactive",
"TOHO",
"The Learning Company",
"Tetris Online",
"TechnoSoft",
"Technos Japan Corporation",
"Team17 Software",
"TalonSoft",
"Takuyo",
"T&E Soft",
"Sunflowers",
"Summitsoft",
"Strategy First",
"Starpath Corp.",
"SSI",
"Square EA",
"SPS",
"Sony Music Entertainment",
"Societa",
"Simon & Schuster Interactive",
"Seventh Chord",
"SCS Software",
"Saurus",
"Riverhillsoft",
"Revolution (Japan)",
"RED Entertainment",
"Rain Games",
"Quintet",
"Quest",
"Quelle",
"Pow",
"PopTop Software",
"Pony Canyon",
"PM Studios",
"Plenty",
"Playmore",
"Playmates",
"Piacci",
"Phoenix Games",
"Phantom EFX",
"Phantagram",
"Paon Corporation",
"Panther Software",
"Palcom",
"Pack In Soft",
"Pacific Century Cyber Works",
"Otomate",
"Origin Systems",
"Ongakukan",
"On Demand",
"Number None",
"Nippon Amuse",
"Nichibutsu",
"Nexon",
"New World Computing",
"New",
"NDA Productions",
"Naxat Soft",
"Navarre Corp",
"Mystique",
"Mycom",
"Monte Christo Multimedia",
"mixi, Inc",
"Mitsui",
"Mirai Shounen",
"Milestone",
"Michaelsoft",
"Merscom LLC",
"Men-A-Vision",
"MediaQuest",
"Media Entertainment",
"Maximum Family Games",
"Max Five",
"Masque Publishing",
"Marvelous Games",
"Marvel Entertainment",
"Magical Company",
"Locus",
"Lighthouse Interactive",
"Legacy Interactive",
"KSS",
"Kool Kizz",
"Kokopeli Digital Studios",
"King Records",
"Kids Station",
"Karin Entertainment",
"Kando Games",
"Kamui",
"Just Flight",
"iWin",
"Ivolgamus",
"ITT Family Games",
"inXile Entertainment",
"Interworks Unlimited, Inc.",
"Interplay Productions",
"Intergrow",
"Interchannel-Holon",
"Imax",
"Imageworks",
"Image Epoch",
"Imadio",
"Illusion Softworks",
"id Software",
"Her Interactive",
"Hearty Robin",
"Headup Games",
"Havas Interactive",
"HAL Laboratory",
"Griffin International",
"Graphsim Entertainment",
"Grand Prix Games",
"GOA",
"Glams",
"Giza10",
"Giga",
"Genterprise",
"General Entertainment",
"GameTek",
"Gameloft",
"Game Arts",
"Gaga",
"FuRyu Corporation",
"FunSoft",
"Fuji",
"Fortyfive",
"fonfun",
"Fields",
"Extreme Entertainment Group",
"Evolution Games",
"Ertain",
"EON Digital Entertainment",
"Enjoy Gaming ltd.",
"Elite",
"Ecole",
"EA Games",
"DreamWorks Interactive",
"DigiCube",
"Detn8 Games",
"Cygames",
"Culture Publishers",
"CPG Products",
"Commseed",
"CokeM Interactive",
"Codemasters Online",
"CCP",
"CBS Electronics",
"BushiRoad",
"Boost On",
"Bomb",
"Bohemia Interactive",
"Black Label Games",
"Berkeley",
"Axela",
"ASK",
"Ascaron Entertainment",
"Aria",
"Aques",
"Answer Software",
"American Softworks",
"Altron",
"Adeline Software",
"Activision Blizzard",
"Abylight",
"989 Sports",
"49Games",
"2D Boy"
);

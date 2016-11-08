INSERT INTO "USER_MEAL_LINK"(
            "user", meal, amount, meal_date_time)
    VALUES (1,
		(
		SELECT "meal_id"
		FROM "MEAL"
		WHERE "name" LIKE 'Riсe'
		LIMIT 1
		),
		200, '2016-11-07 11:15:00');

INSERT INTO "USER_MEAL_LINK"(
            "user", meal, amount, meal_date_time)
    VALUES (1,
		(
		SELECT "meal_id"
		FROM "MEAL"
		WHERE "name" LIKE 'Boiled chicken'
		LIMIT 1
		),
		150, '2016-11-07 17:30:00');

INSERT INTO "USER_MEAL_LINK"(
            "user", meal, amount, meal_date_time)
    VALUES (1,
		(
		SELECT "meal_id"
		FROM "MEAL"
		WHERE "name" LIKE 'Egg'
		LIMIT 1
		),
		120, '2016-11-08 09:00:00');

--SELECT *
--FROM "USER_MEAL_LINK" uml
--	JOIN "auth_user" au ON uml.user = au.id


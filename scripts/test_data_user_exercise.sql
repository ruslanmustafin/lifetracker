INSERT INTO public."USER_EXERCISE_LINK"(
            "user", exercise, value)
    VALUES (1,
		(
		SELECT exercise_id
		FROM "EXERCISE"
		WHERE name = 'squat'
		LIMIT 1
		),
		50);

INSERT INTO public."USER_EXERCISE_LINK"(
            "user", exercise, value)
    VALUES (1,
		(
		SELECT exercise_id
		FROM "EXERCISE"
		WHERE name = 'jogging'
		LIMIT 1
		),
		100);

INSERT INTO public."USER_EXERCISE_LINK"(
            "user", exercise, value)
    VALUES (1,
		(
		SELECT exercise_id
		FROM "EXERCISE"
		WHERE name = 'pull up'
		LIMIT 1
		),
		20);

--SELECT *
--FROM "USER_EXERCISE_LINK" uel
--	JOIN "EXERCISE" ex ON uel.exercise = ex.exercise_id
--	JOIN "EXERCISE_TYPE" type ON ex.type = type.exercise_type_id

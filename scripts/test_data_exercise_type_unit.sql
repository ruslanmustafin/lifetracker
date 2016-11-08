-- units
INSERT INTO "UNIT"(name)
    VALUES ('repetition');

INSERT INTO "UNIT"(name)
    VALUES ('minute');

-- types
INSERT INTO "EXERCISE_TYPE"(name, unit)
    VALUES ('strength',
		(
		SELECT DISTINCT "unit_id"
		FROM "UNIT"
		WHERE "name" = 'repetition')
		);

INSERT INTO "EXERCISE_TYPE"(name, unit)
    VALUES ('cardio',
		(
		SELECT DISTINCT "unit_id"
		FROM "UNIT"
		WHERE "name" = 'minute')
		);

-- exercises
INSERT INTO public."EXERCISE"(
            name, type)
    VALUES ('squat',
		(
		SELECT DISTINCT "exercise_type_id"
		FROM "EXERCISE_TYPE"
		WHERE "name" = 'strength')
		);

INSERT INTO public."EXERCISE"(
            name, type)
    VALUES ('pull up',
		(
		SELECT DISTINCT "exercise_type_id"
		FROM "EXERCISE_TYPE"
		WHERE "name" = 'strength')
		);

INSERT INTO public."EXERCISE"(
            name, type)
    VALUES ('jogging',
		(
		SELECT DISTINCT "exercise_type_id"
		FROM "EXERCISE_TYPE"
		WHERE "name" = 'cardio')
		);

INSERT INTO public."EXERCISE"(
            name, type)
    VALUES ('push up',
		(
		SELECT DISTINCT "exercise_type_id"
		FROM "EXERCISE_TYPE"
		WHERE "name" = 'strength')
		);

--SELECT *
--FROM "EXERCISE"
--	JOIN "EXERCISE_TYPE" ON "EXERCISE"."type" = "EXERCISE_TYPE"."exercise_type_id"
--	JOIN "UNIT" ON "EXERCISE_TYPE"."unit" = "UNIT"."unit_id"

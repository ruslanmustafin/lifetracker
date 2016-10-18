-- CREATE TABLE "USER" (
-- 	"user_id" serial NOT NULL,
-- 	"email" VARCHAR(255) NOT NULL UNIQUE,
-- 	"password" VARCHAR(32) NOT NULL,
-- 	"last_name" VARCHAR(255),
-- 	"first_name" VARCHAR(255) NOT NULL,
-- 	CONSTRAINT USER_pk PRIMARY KEY ("user_id")
-- ) WITH (
--   OIDS=FALSE
-- );



CREATE TABLE "MEAL" (
	"meal_id" serial NOT NULL,
	"name" VARCHAR(255) NOT NULL,
	"type" integer NOT NULL,
	"calories" integer,
	"protein" integer,
	"fat" integer,
	"carbs" integer,
	CONSTRAINT MEAL_pk PRIMARY KEY ("meal_id")
) WITH (
  OIDS=FALSE
);



CREATE TABLE "USER_MEAL_LINK" (
	"user_meal_link_id" serial NOT NULL,
	"user" integer NOT NULL,
	"meal" integer NOT NULL,
	"amount" integer,
	"meal_date_time" TIMESTAMP NOT NULL,
	CONSTRAINT USER_MEAL_LINK_pk PRIMARY KEY ("user_meal_link_id")
) WITH (
  OIDS=FALSE
);



CREATE TABLE "EXERCISE" (
	"exercise_id" serial NOT NULL,
	"name" VARCHAR(255) NOT NULL,
	"type" integer NOT NULL,
	CONSTRAINT EXERCISE_pk PRIMARY KEY ("exercise_id")
) WITH (
  OIDS=FALSE
);



CREATE TABLE "EXERCISE_TYPE" (
	"exercise_type_id" serial NOT NULL,
	"name" VARCHAR(255) NOT NULL,
	"unit" integer NOT NULL,
	CONSTRAINT EXERCISE_TYPE_pk PRIMARY KEY ("exercise_type_id")
) WITH (
  OIDS=FALSE
);



CREATE TABLE "UNIT" (
	"unit_id" serial NOT NULL,
	"name" VARCHAR(255) NOT NULL,
	CONSTRAINT UNIT_pk PRIMARY KEY ("unit_id")
) WITH (
  OIDS=FALSE
);



CREATE TABLE "USER_EXERCISE_LINK" (
	"user_exercise_link_id" serial NOT NULL,
	"user" integer NOT NULL,
	"exercise" integer NOT NULL,
	CONSTRAINT USER_EXERCISE_LINK_pk PRIMARY KEY ("user_exercise_link_id")
) WITH (
  OIDS=FALSE
);



CREATE TABLE "PHOTO" (
	"file_id" serial NOT NULL,
	"user" integer NOT NULL,
	"full_file_name" VARCHAR(255) NOT NULL UNIQUE,
	"upload_date_time" TIMESTAMP NOT NULL,
	CONSTRAINT PHOTO_pk PRIMARY KEY ("file_id")
) WITH (
  OIDS=FALSE
);



CREATE TABLE "GOAL" (
	"goal_id" serial NOT NULL,
	"user" integer NOT NULL,
	"type" integer NOT NULL,
	"amount" integer NOT NULL,
	"deadline_date" TIMESTAMP NOT NULL,
	CONSTRAINT GOAL_pk PRIMARY KEY ("goal_id")
) WITH (
  OIDS=FALSE
);





-- ALTER TABLE "USER_MEAL_LINK" ADD CONSTRAINT "USER_MEAL_LINK_fk0" FOREIGN KEY ("user") REFERENCES "USER"("user_id");
ALTER TABLE "USER_MEAL_LINK" ADD CONSTRAINT "USER_MEAL_LINK_fk1" FOREIGN KEY ("meal") REFERENCES "MEAL"("meal_id");

ALTER TABLE "EXERCISE" ADD CONSTRAINT "EXERCISE_fk0" FOREIGN KEY ("type") REFERENCES "EXERCISE_TYPE"("exercise_type_id");

ALTER TABLE "EXERCISE_TYPE" ADD CONSTRAINT "EXERCISE_TYPE_fk0" FOREIGN KEY ("unit") REFERENCES "UNIT"("unit_id");


-- ALTER TABLE "USER_EXERCISE_LINK" ADD CONSTRAINT "USER_EXERCISE_LINK_fk0" FOREIGN KEY ("user") REFERENCES "USER"("user_id");
ALTER TABLE "USER_EXERCISE_LINK" ADD CONSTRAINT "USER_EXERCISE_LINK_fk1" FOREIGN KEY ("exercise") REFERENCES "EXERCISE"("exercise_id");

-- ALTER TABLE "PHOTO" ADD CONSTRAINT "PHOTO_fk0" FOREIGN KEY ("user") REFERENCES "USER"("user_id");

-- ALTER TABLE "GOAL" ADD CONSTRAINT "GOAL_fk0" FOREIGN KEY ("user") REFERENCES "USER"("user_id");
 
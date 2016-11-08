-- exercises
ALTER TABLE "USER_EXERCISE_LINK"
DROP CONSTRAINT "USER_EXERCISE_LINK_fk0";

ALTER TABLE "USER_EXERCISE_LINK"
ADD CONSTRAINT USER_EXERCISE_LINK_fk0
FOREIGN KEY ("user")
REFERENCES "auth_user"(id);

-- meals
ALTER TABLE "USER_MEAL_LINK"
DROP CONSTRAINT "USER_MEAL_LINK_fk0";

ALTER TABLE "USER_MEAL_LINK"
ADD CONSTRAINT USER_MEAL_LINK_fk0
FOREIGN KEY ("user")
REFERENCES "auth_user"(id);

-- weight
ALTER TABLE "WEIGHT"
DROP CONSTRAINT "WEIGHT_fk0";

ALTER TABLE "WEIGHT"
ADD CONSTRAINT WEIGHT_fk0
FOREIGN KEY ("user")
REFERENCES "auth_user"(id);
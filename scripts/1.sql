CREATE TABLE "WEIGHT" (
	"weight_id" serial NOT NULL,
	"user" integer NOT NULL,
	"weight_date_time" TIMESTAMP NOT NULL,
	CONSTRAINT WEIGHT_pk PRIMARY KEY ("weight_id")
) WITH (
  OIDS=FALSE
);


ALTER TABLE "WEIGHT" ADD CONSTRAINT "WEIGHT_fk0" FOREIGN KEY ("user") REFERENCES "USER"("user_id");
-- create catalog IF NOT EXISTS ncat WITH (
--   'type'='iceberg',
--   'catalog-type'='hive',
--   'uri'='thrift://host.docker.internal:9083',
--   'clients'='5',
--   'property-version'='1',
--   'warehouse'='s3a://warehouse/wh'
-- );

CREATE database IF NOT EXISTS `ncat`.`idb`;

CREATE TABLE IF NOT EXISTS ncat.idb.ai_messages (
        id STRING,
        lead_id STRING,
        question_id STRING,
        from_who STRING,
        employee_id STRING,
        to_user_id STRING,
        from_admin STRING,
        req_language_id STRING,
        res_language_id STRING,
        delivery_type STRING,
        webhook_req_id STRING,    
        units STRING,
        answer_text STRING,
        entities STRING,
        read STRING,
        use_ai STRING,
        media_url STRING,
        mime_type STRING,
        sid STRING,
        media_thumb STRING,
        is_profile STRING,
        MessageUUID STRING,
        qtext STRING,
        is_multiparts STRING,
        ip STRING,
        status STRING,
        msg_type STRING,
        is_smart_alerted STRING,
        smart_alert_users STRING,
        data STRING,
        created_at STRING,
        updated_at STRING
);


CREATE TEMPORARY VIEW ai_messages
USING csv 
OPTIONS (
  path '/opt/spark/code/data/many_to_many/1000000_ai_messages.csv',
  header true
);

INSERT INTO ncat.idb.ai_messages SELECT * FROM ai_messages;


CREATE TABLE IF NOT EXISTS ncat.idb.ai_message_note (
        x_id STRING,
        message_id STRING,
        note_id STRING
);


CREATE TEMPORARY VIEW ai_message_note
USING csv 
OPTIONS (
  path '/opt/spark/code/data/many_to_many/1000000_ai_message_note.csv',
  header true
);

INSERT INTO ncat.idb.ai_message_note SELECT * FROM ai_message_note;

CREATE TABLE IF NOT EXISTS ncat.idb.ai_interviews (
    id STRING,
    uuid STRING,
    user_id STRING,
    company_id STRING,
    candidate_id STRING,
    sub_itv_id STRING,
    interview_duration STRING,
    interview_type STRING,
    interview_jobloc_id STRING,
    primary_id STRING,
    cal_event_id STRING,
    status STRING,
    deprecated_interview_type STRING,
    users_calendar_data STRING,
    created_at STRING
);


CREATE TEMPORARY VIEW ai_interviews
USING csv 
OPTIONS (
  path '/opt/spark/fakedata/1000000_ai_interviews.csv',
  header true
);

INSERT INTO ncat.idb.ai_interviews SELECT * FROM ai_interviews;


CREATE TABLE IF NOT EXISTS ncat.idb.ai_lead_sub_itvs (
  id STRING,
  lead_id STRING,
  created_at STRING,
  updated_at STRING,
  order STRING,
  name STRING,
  job_loc_room_id STRING,
  interview_type STRING,
  itv_location_string STRING,
  interview_jobloc_id STRING,
  interview_duration STRING,
  pre_attendees STRING,
  interviewer_ids STRING,
  scheduled_at STRING,
  any_avail_room STRING,
  deprecated_interview_type STRING,
  deleted_at STRING,
  deleted_by STRING,
  is_deleted STRING,
  _user_chosen_slots STRING
);


CREATE TEMPORARY VIEW ai_lead_sub_itvs
USING csv 
OPTIONS (
  path '/opt/spark/fakedata/1000000_ai_lead_sub_itvs.csv',
  header true
);

INSERT INTO ncat.idb.ai_lead_sub_itvs SELECT * FROM ai_lead_sub_itvs;


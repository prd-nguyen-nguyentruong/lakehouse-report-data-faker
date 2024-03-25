from mimesis.schema import Field, Fieldset
from mimesis.locales import Locale
import datetime


field = Field(Locale.EN, seed=0xff)
fieldset = Fieldset(Locale.EN, seed=0xff)
nowww = datetime.datetime.now()

start_id_range = 1
end_id_range = 1000000000
rand_id = False

def increment_counter(start):
    global start_id_range
    start_id_range += 1
    return start_id_range

ai_messages = lambda: {
    "id": field("integer_number", start=start_id_range, end=end_id_range) if rand_id else field("increment", accumulator="a"),
    "lead_id": field("integer_number", start=start_id_range, end=end_id_range) if rand_id else field("increment", accumulator="b"),
    "question_id": field("integer_number", start=start_id_range, end=end_id_range) if rand_id else field("increment", accumulator="c"),
    "from_who": field("integer_number", start=start_id_range, end=end_id_range),
    "employee_id": field("integer_number", start=start_id_range, end=end_id_range),
    "to_user_id": field("integer_number", start=start_id_range, end=end_id_range),
    "from_admin": field("integer_number", start=start_id_range, end=end_id_range),
    "req_language_id": field("integer_number", start=start_id_range, end=end_id_range),
    "res_language_id": field("integer_number", start=start_id_range, end=end_id_range),
    "delivery_type": field("integer_number", start=start_id_range, end=end_id_range),
    "webhook_req_id": field("integer_number", start=start_id_range, end=end_id_range),
    "units": field("integer_number", start=1, end=10),
    "answer_text": field("text.sentence"),
    "entities": field("text.sentence"),
    "read": field("integer_number", start=0, end=1),
    "use_ai": field("integer_number", start=0, end=1),
    "media_url": field("internet.stock_image_url"),
    "mime_type": field("text.word"),
    "sid": field("text.word"),
    "media_thumb": field("internet.stock_image_url"),
    "is_profile": field("integer_number", start=0, end=1),
    "MessageUUID": field("uuid"),
    "qtext": field("text.sentence"),
    "is_multiparts": field("integer_number", start=1, end=10),
    "ip": field("internet.ip_v4"),
    "status": field("integer_number", start=1, end=10),
    "msg_type": field("integer_number", start=1, end=10),
    "is_smart_alerted": field("integer_number", start=1, end=10),
    "smart_alert_users": field("text.sentence"),
    "data": field("text.sentence"),
    "created_at": nowww,
    "updated_at": nowww   
}

ai_message_note = lambda: {
    "id": field("integer_number", start=start_id_range, end=end_id_range) if rand_id else field("increment", accumulator="a"),
    "message_id": field("integer_number", start=start_id_range, end=end_id_range) if rand_id else field("increment", accumulator="b"),
    "note_id": field("integer_number", start=1, end=1000000000),
}

ai_recorded_interview_messages = lambda: {
    "id": field("integer_number", start=start_id_range, end=end_id_range) if rand_id else field("increment"),
    "uuid": field("integer_number", start=start_id_range, end=end_id_range) if rand_id else field("increment"),
    "created_at": nowww,
    "updated_at": nowww,
    "message_type": field("integer_number", start=1, end=1000000000),
    "message_id": field("integer_number", start=1, end=1000000000),
    "recorded_itv_candidate_id": field("integer_number", start=1, end=1000000000),
    "max_video_length": field("integer_number", start=1, end=1000000000),
    "media_type": field("integer_number", start=1, end=1000000000),
}

ai_interviews = lambda: {
    "id": field("integer_number", start=start_id_range, end=end_id_range) if rand_id else field("increment"),
    "uuid": field("integer_number", start=start_id_range, end=end_id_range) if rand_id else field("increment"),
    "user_id": field("integer_number", start=start_id_range, end=end_id_range) if rand_id else field("increment"),
    "company_id": field("integer_number", start=start_id_range, end=end_id_range) if rand_id else field("increment"),
    "candidate_id": field("integer_number", start=start_id_range, end=end_id_range) if rand_id else field("increment"),
    "sub_itv_id": field("integer_number", start=start_id_range, end=end_id_range) if rand_id else field("increment"),
    "interview_duration": field("integer_number", start=1, end=100),
    "interview_type": field("integer_number", start=1, end=100),
    "interview_jobloc_id": field("integer_number", start=1, end=100),
    "primary_id": field("integer_number", start=1, end=100),
    "status": field("integer_number", start=1, end=100),
    "cal_event_id": field("integer_number", start=1, end=100),
    "status": field("integer_number", start=1, end=100),
    "deprecated_interview_type": field("integer_number", start=1, end=100),
    "users_calendar_data": field("integer_number", start=1, end=100),
}

ai_lead_sub_itvs = lambda: {
    "id": field("integer_number", start=start_id_range, end=end_id_range) if rand_id else field("increment"),
    "lead_id": field("integer_number", start=start_id_range, end=end_id_range) if rand_id else field("increment"),
    "lead_id": field("integer_number", start=start_id_range, end=end_id_range) if rand_id else field("increment"),
    "created_at": nowww,
    "updated_at": nowww,
    "order": field("integer_number", start=1, end=100),
    "name": field("integer_number", start=1, end=100),
    "job_loc_room_id": field("integer_number", start=1, end=100),
    "interview_type": field("integer_number", start=1, end=100),
    "itv_location_string": field("integer_number", start=1, end=100),
    "interview_jobloc_id": field("integer_number", start=1, end=100),
    "interview_duration": field("integer_number", start=1, end=100),
    "pre_attendees": field("integer_number", start=1, end=100),
    "interviewr_ids": field("integer_number", start=1, end=100),
    "scheduled_at": nowww,
    "any_avail_room": field("integer_number", start=1, end=100),
    "deprecated_interview_type": field("integer_number", start=1, end=100),
    "deleted_at": nowww,
    "deleted_by": field("integer_number", start=1, end=100),
    "is_deleted": field("integer_number", start=1, end=100),
    "_user_chosen_slots": field("integer_number", start=1, end=100),
}

ai_leads = lambda: {

}

schemas = {
    "ai_messages": ai_messages,
    "ai_message_note": ai_message_note,
    "ai_recorded_interview_messages": ai_recorded_interview_messages,
    "ai_interviews": ai_interviews,
    "ai_lead_sub_itvs": ai_lead_sub_itvs
}

def get_schema(input_str):
    schema = schemas.get(input_str)
    
    if schema:
        return schema
    else:
        print("Schema not found")

def set_start_id_range(num):
    global start_id_range
    start_id_range = num

def set_end_id_range(num):
    global end_id_range
    end_id_range = num

def set_id_random(rand):
    global rand_id
    rand_id = rand
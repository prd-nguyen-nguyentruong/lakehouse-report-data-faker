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
    "id": field("integer_number", start=start_id_range, end=end_id_range) if rand_id else field("increment"),
    "lead_id": field("integer_number", start=start_id_range, end=end_id_range) if rand_id else field("increment"),
    "question_id": field("integer_number", start=start_id_range, end=end_id_range) if rand_id else field("increment"),
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
    "x_id": field("integer_number", start=start_id_range, end=end_id_range) if rand_id else field("increment"),
    "message_id": field("integer_number", start=start_id_range, end=end_id_range) if rand_id else field("increment"),
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

schemas = {
    "ai_messages": ai_messages,
    "ai_message_note": ai_message_note,
    "ai_recorded_interview_messages": ai_recorded_interview_messages,
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
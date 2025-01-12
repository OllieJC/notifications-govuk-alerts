from datetime import datetime

import pytz
from notifications_utils.serialised_model import SerialisedModel

from lib.alert_date import AlertDate


class Alert(SerialisedModel):
    ALLOWED_PROPERTIES = {
        'identifier',
        'message_type',
        'starts',
        'sent',
        'expires',
        'headline',
        'description',
        'static_map_png',
        'area_names',
    }

    @property
    def starts_date(self):
        return AlertDate(self.starts)

    @property
    def sent_date(self):
        return AlertDate(self.sent)

    @property
    def expires_date(self):
        return AlertDate(self.expires)

    @property
    def is_expired(self):
        now = datetime.now(pytz.utc)
        return self.expires_date.as_utc_datetime < now

    @property
    def is_current(self):
        now = datetime.now(pytz.utc)

        return (
            self.expires_date.as_utc_datetime >= now and
            self.sent_date.as_utc_datetime <= now
        )

# apps/sync/api_clients.py

import time
from datetime import datetime


class BaseClient:
    def __init__(self, config):
        self.config = config

    def fetch_updated_leads(self, since: datetime):
        """Return list of dicts: {external_id, provider, data, last_updated}"""
        raise NotImplementedError

    def push_lead(self, lead):
        """Push local lead to remote provider. Return remote representation (external_id, last_updated)"""
        raise NotImplementedError

    # Similar for campaigns


class GoogleAnalyticsClient(BaseClient):
    def fetch_updated_leads(self, since):
        # use Measurement Protocol / GA4 Data API
        return []

    def push_lead(self, lead):
        # GA is typically not a lead storage; this is for examples
        return {'external_id': lead.external_id, 'last_updated': datetime.utcnow()}

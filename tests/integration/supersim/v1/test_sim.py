# coding=utf-8
r"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from tests import IntegrationTestCase
from tests.holodeck import Request
from twilio.base.exceptions import TwilioException
from twilio.http.response import Response


class SimTestCase(IntegrationTestCase):

    def test_create_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.supersim.v1.sims.create(iccid="iccid", registration_code="registration_code")

        values = {'Iccid': "iccid", 'RegistrationCode': "registration_code", }

        self.holodeck.assert_has_request(Request(
            'post',
            'https://supersim.twilio.com/v1/Sims',
            data=values,
        ))

    def test_create_response(self):
        self.holodeck.mock(Response(
            201,
            '''
            {
                "sid": "HSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "unique_name": "",
                "status": "new",
                "fleet_sid": null,
                "iccid": "89883070000123456789",
                "date_created": "2015-07-30T20:00:00Z",
                "date_updated": "2015-07-30T20:00:00Z",
                "url": "https://supersim.twilio.com/v1/Sims/HSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
            }
            '''
        ))

        actual = self.client.supersim.v1.sims.create(iccid="iccid", registration_code="registration_code")

        self.assertIsNotNone(actual)

    def test_fetch_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.supersim.v1.sims("HSXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").fetch()

        self.holodeck.assert_has_request(Request(
            'get',
            'https://supersim.twilio.com/v1/Sims/HSXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
        ))

    def test_fetch_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "sid": "HSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "unique_name": "My SIM",
                "status": "new",
                "fleet_sid": null,
                "iccid": "89883070000123456789",
                "date_created": "2015-07-30T20:00:00Z",
                "date_updated": "2015-07-30T20:00:00Z",
                "url": "https://supersim.twilio.com/v1/Sims/HSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
            }
            '''
        ))

        actual = self.client.supersim.v1.sims("HSXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").fetch()

        self.assertIsNotNone(actual)

    def test_update_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.supersim.v1.sims("HSXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").update()

        self.holodeck.assert_has_request(Request(
            'post',
            'https://supersim.twilio.com/v1/Sims/HSXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
        ))

    def test_update_unique_name_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "sid": "HSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "unique_name": "MySIM",
                "status": "new",
                "fleet_sid": null,
                "iccid": "89883070000123456789",
                "date_created": "2015-07-30T20:00:00Z",
                "date_updated": "2015-07-30T20:00:00Z",
                "url": "https://supersim.twilio.com/v1/Sims/HSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
            }
            '''
        ))

        actual = self.client.supersim.v1.sims("HSXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").update()

        self.assertIsNotNone(actual)

    def test_update_status_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "sid": "HSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "unique_name": null,
                "status": "scheduled",
                "fleet_sid": null,
                "iccid": "89883070000123456789",
                "date_created": "2015-07-30T20:00:00Z",
                "date_updated": "2015-07-30T20:00:00Z",
                "url": "https://supersim.twilio.com/v1/Sims/HSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
            }
            '''
        ))

        actual = self.client.supersim.v1.sims("HSXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").update()

        self.assertIsNotNone(actual)

    def test_update_fleet_with_sid_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "sid": "HSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "unique_name": null,
                "status": "new",
                "fleet_sid": "HFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "iccid": "89883070000123456789",
                "date_created": "2015-07-30T20:00:00Z",
                "date_updated": "2015-07-30T20:00:00Z",
                "url": "https://supersim.twilio.com/v1/Sims/HSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
            }
            '''
        ))

        actual = self.client.supersim.v1.sims("HSXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").update()

        self.assertIsNotNone(actual)

    def test_update_fleet_with_unique_name_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "sid": "HSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "unique_name": null,
                "status": "new",
                "fleet_sid": "HFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "iccid": "89883070000123456789",
                "date_created": "2015-07-30T20:00:00Z",
                "date_updated": "2015-07-30T20:00:00Z",
                "url": "https://supersim.twilio.com/v1/Sims/HSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
            }
            '''
        ))

        actual = self.client.supersim.v1.sims("HSXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").update()

        self.assertIsNotNone(actual)

    def test_transfer_sim_to_another_account_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "sid": "HSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "account_sid": "ACbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb",
                "unique_name": null,
                "status": "new",
                "fleet_sid": "HFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "iccid": "89883070000123456789",
                "date_created": "2015-07-30T20:00:00Z",
                "date_updated": "2015-07-30T20:00:00Z",
                "url": "https://supersim.twilio.com/v1/Sims/HSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
            }
            '''
        ))

        actual = self.client.supersim.v1.sims("HSXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").update()

        self.assertIsNotNone(actual)

    def test_list_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.supersim.v1.sims.list()

        self.holodeck.assert_has_request(Request(
            'get',
            'https://supersim.twilio.com/v1/Sims',
        ))

    def test_read_empty_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "sims": [],
                "meta": {
                    "first_page_url": "https://supersim.twilio.com/v1/Sims?Status=new&Fleet=HFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa&PageSize=50&Page=0",
                    "key": "sims",
                    "next_page_url": null,
                    "page": 0,
                    "page_size": 50,
                    "previous_page_url": null,
                    "url": "https://supersim.twilio.com/v1/Sims?Status=new&Fleet=HFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa&PageSize=50&Page=0"
                }
            }
            '''
        ))

        actual = self.client.supersim.v1.sims.list()

        self.assertIsNotNone(actual)

    def test_read_full_by_fleet_sid_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "meta": {
                    "first_page_url": "https://supersim.twilio.com/v1/Sims?Status=new&Fleet=HFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa&PageSize=50&Page=0",
                    "key": "sims",
                    "next_page_url": null,
                    "page": 0,
                    "page_size": 50,
                    "previous_page_url": null,
                    "url": "https://supersim.twilio.com/v1/Sims?Status=new&Fleet=HFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa&PageSize=50&Page=0"
                },
                "sims": [
                    {
                        "sid": "HSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "unique_name": "My SIM",
                        "status": "new",
                        "fleet_sid": "HFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "iccid": "89883070000123456789",
                        "date_created": "2015-07-30T20:00:00Z",
                        "date_updated": "2015-07-30T20:00:00Z",
                        "url": "https://supersim.twilio.com/v1/Sims/HSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                    }
                ]
            }
            '''
        ))

        actual = self.client.supersim.v1.sims.list()

        self.assertIsNotNone(actual)

    def test_read_full_by_fleet_name_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "meta": {
                    "first_page_url": "https://supersim.twilio.com/v1/Sims?Status=new&Fleet=MyFleet&PageSize=50&Page=0",
                    "key": "sims",
                    "next_page_url": null,
                    "page": 0,
                    "page_size": 50,
                    "previous_page_url": null,
                    "url": "https://supersim.twilio.com/v1/Sims?Status=new&Fleet=MyFleet&PageSize=50&Page=0"
                },
                "sims": [
                    {
                        "sid": "HSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "unique_name": "My SIM",
                        "status": "new",
                        "fleet_sid": "HFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "iccid": "89883070000123456789",
                        "date_created": "2015-07-30T20:00:00Z",
                        "date_updated": "2015-07-30T20:00:00Z",
                        "url": "https://supersim.twilio.com/v1/Sims/HSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                    }
                ]
            }
            '''
        ))

        actual = self.client.supersim.v1.sims.list()

        self.assertIsNotNone(actual)

    def test_read_by_iccid_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "meta": {
                    "first_page_url": "https://supersim.twilio.com/v1/Sims?Iccid=89883070000123456789&PageSize=50&Page=0",
                    "key": "sims",
                    "next_page_url": null,
                    "page": 0,
                    "page_size": 50,
                    "previous_page_url": null,
                    "url": "https://supersim.twilio.com/v1/Sims?Iccid=89883070000123456789&PageSize=50&Page=0"
                },
                "sims": [
                    {
                        "sid": "HSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "unique_name": "My SIM",
                        "status": "new",
                        "fleet_sid": null,
                        "iccid": "89883070000123456789",
                        "date_created": "2015-07-30T20:00:00Z",
                        "date_updated": "2015-07-30T20:00:00Z",
                        "url": "https://supersim.twilio.com/v1/Sims/HSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                    }
                ]
            }
            '''
        ))

        actual = self.client.supersim.v1.sims.list()

        self.assertIsNotNone(actual)

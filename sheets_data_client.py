"""
Shows basic usage of the Sheets API. Prints values from a Google Spreadsheet.
"""
from __future__ import print_function
from apiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools

class DataClient:

    def __init__(self):
        # Setup the Sheets API
        SCOPES = 'https://www.googleapis.com/auth/spreadsheets'
        store = file.Storage('credentials.json')
        creds = store.get()
        if not creds or creds.invalid:
            flow = client.flow_from_clientsecrets('client_secret.json', SCOPES)
            creds = tools.run_flow(flow, store)
        self.service = build('sheets', 'v4', http=creds.authorize(Http()))

        # Call the Sheets API
        self.SPREADSHEET_ID = '1n38sIq_3rCaGiGTQhlL2M9igDEDBoagAhJHkVWCkrT8'
    
    def get_filter_values(self):
        """
        Retrieve the filter values
        """
        if not self.service:
            return False
        
        FILTER_RANGE='Filters!A:A'
        result = self.service.spreadsheets().values().get(spreadsheetId=self.SPREADSHEET_ID,
                                                    range=FILTER_RANGE).execute()
        filter_values = result.get('values', [])
        if not filter_values:
            print('No data found.')
            return []
        else:
            # Filters are all lower cased items from the 1st column of the Filters-sheet.
            filters = [value[0].lower() for value in filter_values]
            return filters

    def append_values(self, sheet, data):
        """
        Store the data in the sheet. If append is set to true, the data will be added below the rest.

        :param sheet:
        :param data:
        :param append:
        :return:
        """
        storage_range = sheet
        result = self.service.spreadsheets().values().append(spreadsheetId=self.SPREADSHEET_ID,
                                                                 valueInputOption=data)

    def get_sheet_names(self):
        sheet_metadata = self.service.spreadsheets().get(spreadsheetId=self.SPREADSHEET_ID).execute()
        sheet_names = [item['properties']['title'] for item in sheet_metadata['sheets']]

        return sheet_names



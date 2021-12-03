class XLHEADERS():
    COUNTRY = 'country'
    CITY = 'city'
    STATION_EOI_CODE = 'stationeoicode'
    STATION_NAME = 'stationname'
    AIR_POLLUTANT = 'airpollutant'
    AIR_POLLUTION_LEVEL = 'airpollutionlevel'
    TYPE = 'type'
    AREA = 'area'
    LONGITUDE = 'longitude'
    LATITUDE = 'latitude'
    ALTITUDE = 'altitude'

    choices = [COUNTRY, CITY, STATION_EOI_CODE, STATION_NAME, AIR_POLLUTANT, AIR_POLLUTION_LEVEL, TYPE, AREA, LONGITUDE, LATITUDE, ALTITUDE]



def get_headers_and_units(ws):

    # Initialize the results data
    headers_row = None
    headers = {}
    units = ''

    # Get headers row
    for row in range(ws.max_row + 1):
        # check if A column has the word Country as a value
        cell = ws['A'][row].value
        """ look at column A and rows 0,1,2,3..."""
        if isinstance(cell, str) and 'country' in cell.lower():
            headers_row = row
            break
        """ check if the cell is a string
        cell.lower() -> put word in lower case
        """

    # if nothing found
    if headers_row is None:
        return None, None, None
    """ If nothing found, return None 3 times. Because
    in views.py we put headers_row, header, units = get_headers_and_units(ws)"""

    # Remember headers positions
    for i in range(ws.max_column):
        column = chr(i + 65)
        """ Loop through all the columns
        if index is 0 -> 0 + 65 = 65 -> letter 'A' in ASCII
        if index is 1 -> 1 + 65 = 66 -> letter 'B' in ASCII """
        header = ws[column][headers_row].value

        #clean header

        header = header.strip().replace('_', '').lower()
        """strip removes blank spaces
        ex: header = strip(' abc ') -> return 'abc' without space
         ('_', '') -> remove _
         .lower() -> lowercase"""

        # Get units
        if 'm3' in header:
            units_index = header.find('(') + 1
            """ units_index -> where in the header string AirPollutionLevel (µg/m3)
            the unit 'm3' start
             find('(') + 1 -> start 1 unit after '('
              """
            for index in range(units_index, units_index + 20):
                """ collect btw this unit_index and closing ')'
                 -> from 'µ' to ')' """
                if header[index] == ')':
                    break
                """ break loop if it finds ')' """
                units += header[index]
                """ add each character from the header that we
                iterate"""
            continue
            """ don't break from the for loop, but 
            skip this step. If there is 'm3', go back to 
            for i in range(ws.max_column)
            and check for the next header """

        # get info from the cells below header for 2016
        elif 'unit' in header:
            units = ws[column][headers_row + 1].value
            """ 2016 units is column UnitOfAirpollutionLevel and 1 row below"""
            continue

        # Map headers with their indices
        for choice in XLHEADERS.choices:
            if choice in header:
                headers[choice] = i
                """ There are 2 ways to use Excel worksheet :
                1) get column value : A, B, C... and row value : 1, 2, 3...
                2) iterate through the ws using rows index. Each row is 
                a list of values."""

    return headers_row, headers, units










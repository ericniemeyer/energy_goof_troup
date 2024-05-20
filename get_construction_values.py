import pandas as pd
import pprint


def read_climate_zone_data(df):
    # Initialize dictionary to store data for each climate zone
    climate_data = {}
    climate_zone = None

    # Iterate over the rows of the DataFrame
    for index, row in df.iterrows():
        list_of_row_values = row.tolist()

        # Check if the first cell starts with "Table 5.5-"
        if str(row[0]).startswith(f"Table 5.5-"):
            # Get climate zone number from the table header.
            climate_zone = str(row[0]).split()[1].split("-")[1]
            climate_data[climate_zone] = {}
        else:
            if climate_zone is not None:
                envelope_parameter = list_of_row_values[0]
                if envelope_parameter not in climate_data[climate_zone].keys():
                    climate_data[climate_zone][envelope_parameter] = list_of_row_values[1:]
                # else:
                #     climate_data[climate_zone][envelope_parameter + '2'] = list_of_row_values[1:]

    return climate_data


def get_construction_values(file_path, climate_zone):
    df = pd.read_csv(file_path)

    climate_data = read_climate_zone_data(df)
    # pprint.pprint(climate_data[climate_zone])
    return climate_data[climate_zone]


def reformat_construction_values(file_path, climate_zone):
    construction_values = get_construction_values(file_path, climate_zone)

    surface_type_labels = {
        'Roof': {
            'Insulation entirely above deck': 'Ins. Above Roof Deck',
            'Metal buildinga': 'Metal Roof',
            'Attic and other': 'Attic + Other',
        },
        'Wall': {
            'Mass': 'Mass',
            'Metal building': 'Metal',
            'Steel-framed': 'Metal Frame',
            'Wood-framed and other': 'Wood Frame',
            'Below-grade wall': 'Below Grade',
        }
    }

    # data = [['tom', 10], ['nick', 15], ['juli', 14]]
    data = []

    for surface_category, surface_types in surface_type_labels.items():
        for csv_label, display_label in surface_types.items():
            df_label = f"{surface_category} - {display_label}"
            r_value = construction_values[csv_label][1]
            u_value = construction_values[csv_label][0]
            data.append([df_label, r_value, u_value])

    # Create the pandas DataFrame
    df = pd.DataFrame(data, columns=['Surface Type', 'R-Value', 'U-Value'])
    pprint.pprint(df)
    return df


# file_path = r'C:\Users\ENIEMEYER\Documents\GitHub\energy_goof_troup\ASHRAE 90.1-2019.csv'
# reformat_construction_values(file_path, '2')

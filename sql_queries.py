import sqlite3
from datetime import datetime


def create_table(c):
    try:
        c.execute('''
        CREATE TABLE NEO_DATA (
            ID NUMBER PRIMARY KEY, 
            NEO_DATE date,
            LINKS  VARCHAR2(1000),
            NEO_REFERENCE_ID NUMBER,
            NAME VARCHAR2(100) ,
            nasa_jpl_url VARCHAR2(1000),
            absolute_magnitude_h  number,
            estimated_diameter_miles_min number, 
            estimated_diameter_miles_max number, 
            estimated_diameter_feet_min number,
            estimated_diameter_feet_max number,
            is_potentially_hazardous_asteroid varchar2(100),
            close_approach_date data,
            close_approach_date_full date,
            epoch_date_close_approach date,
            relative_velocity_mph number, 
            miss_distance_miles number, 
            orbiting_body varchar2(100),
            is_sentry_object varcahr2(100) 
            );
                  ''')
    except sqlite3.OperationalError as e:
        c.execute('''DROP TABLE NEO_DATA ''')

        c.execute('''
               CREATE TABLE NEO_DATA (
                   ID NUMBER PRIMARY KEY, 
                   NEO_DATE date,
                   LINKS  VARCHAR2(1000),
                   NEO_REFERENCE_ID NUMBER,
                   NAME VARCHAR2(100) ,
                   nasa_jpl_url VARCHAR2(1000),
                   absolute_magnitude_h  number,
                   estimated_diameter_miles_min number, 
                   estimated_diameter_miles_max number, 
                   estimated_diameter_feet_min number,
                   estimated_diameter_feet_max number,
                   is_potentially_hazardous_asteroid varchar2(100),
                   close_approach_date data,
                   close_approach_date_full date,
                   epoch_date_close_approach date,
                   relative_velocity_mph number, 
                   miss_distance_miles number, 
                   orbiting_body varchar2(100),
                   is_sentry_object varcahr2(100) 
                   );
                         ''')


def create_error_log(c):
    try:
        c.execute('''
            CREATE TABLE ERROR_LOG (
            ERROR_DATE date,
            ERROR_MESSAGE varchar2(1000)
            );
                      ''')
    except sqlite3.OperationalError:
        pass
    except Exception as e:
        print(e)


def log_error(c, e, conn):
    time_now = datetime.now().strftime('%m-%d-%Y %H:%M:%S')
    c.execute(f''' 
                INSERT INTO ERROR_LOG 
                (ERROR_DATE, ERROR_MESSAGE)
                VALUES
                ( '{time_now}','{e}');
                ''')
    conn.commit()


def neo_insert(response, c, conn):

    for i1 in response['near_earth_objects']:
        date = i1
        for i2 in range(len(response['near_earth_objects'][i1])):
            json_res = response['near_earth_objects'][i1][i2]
            links = json_res['links']['self']
            id = json_res['id']
            neo_reference_id = json_res['neo_reference_id']
            neo_reference_id = neo_reference_id[-4:]
            name = json_res['name']
            nasa_jpl_url = json_res['nasa_jpl_url']
            absolute_magnitude_h = json_res['absolute_magnitude_h']
            estimated_diameter_miles_min = json_res['estimated_diameter']['miles']['estimated_diameter_min']
            estimated_diameter_miles_max = json_res['estimated_diameter']['miles']['estimated_diameter_max']
            estimated_diameter_feet_min = json_res['estimated_diameter']['feet']['estimated_diameter_min']
            estimated_diameter_feet_max = json_res['estimated_diameter']['feet']['estimated_diameter_max']
            is_potentially_hazardous_asteroid = json_res['is_potentially_hazardous_asteroid']
            close_approach_date = json_res['close_approach_data'][0]['close_approach_date']
            close_approach_date_full = json_res['close_approach_data'][0]['close_approach_date_full']
            epoch_date_close_approach = json_res['close_approach_data'][0]['epoch_date_close_approach']
            epoch_date_close_approach = datetime.utcfromtimestamp(epoch_date_close_approach/1000).isoformat()
            relative_velocity_mph = json_res['close_approach_data'][0]['relative_velocity']['miles_per_hour']
            miss_distance_miles = json_res['close_approach_data'][0]['miss_distance']['miles']
            orbiting_body = json_res['close_approach_data'][0]['orbiting_body']
            is_sentry_object = json_res['is_sentry_object']


            c.execute(f"""
            INSERT INTO NEO_DATA VALUES 
              ( {id}, 
               '{date}',
               '{links}',
               {neo_reference_id},
               '{name}' ,
               '{nasa_jpl_url}',
               {absolute_magnitude_h},
               {estimated_diameter_miles_min}, 
               {estimated_diameter_miles_max}, 
               {estimated_diameter_feet_min},
               {estimated_diameter_feet_max},
               {is_potentially_hazardous_asteroid},
               '{close_approach_date}',
               '{close_approach_date_full}',
               '{epoch_date_close_approach}',
               {relative_velocity_mph}, 
               {miss_distance_miles}, 
               '{orbiting_body}',
               {is_sentry_object} ) ; 
            
            """)
    conn.commit()

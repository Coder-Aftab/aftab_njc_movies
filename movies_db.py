import psycopg2
from configparser import ConfigParser

#establishing connection to database

def config(filename='database.ini', section='postgresql'):
    parser = ConfigParser()
    parser.read(filename)

    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))

    return db

def estDBConn():
    conn = None
    try:
        params = config()

        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)
		
        cur = conn.cursor()

        return cur, conn
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        return -1, -1

def commitConn(conn):
    conn.commit()

def closeDBConn(conn, cursor):
    cursor.close()
    conn.close()

#Data fetching queries

#this will return all the movies in which actor has appeared
def getMoviesNameForActor(actorName, cur, conn):
    query="""
    SELECT cd.cast_lead_actor ,mv.mv_name
    FROM movies_details mv
    INNER JOIN
    cast_details cd
    ON
    cd.cast_lead_actor = '{a_name}'
	AND
	cd.cast_mv_id = mv.mv_id
    """.format(a_name= actorName)

    try:
        cur.execute(query)
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
        return -1

    return cur.fetchall()

#this will return the director name for a particular movie
def getDirectorNameForMovie(movie_name, cur, conn):
    
    query="""
    SELECT dd.dir_name, mv_name, mv.mv_rel_dt
    FROM
    dir_details dd 
    INNER JOIN
    movies_details mv
    ON
    mv.mv_name = '{mv_name}' and
    dir_id = mv_dir_id
    """.format(mv_name= movie_name)
    
    
    try:
        cur.execute(query)
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
        return -1

    return cur.fetchall()
#!/usr/bin/env python3
from movies_db import *

def main():

    cursor, conn=estDBConn()

    if(cursor == -1 or conn == -1):
        print("Failed to Establish Connection with Database")
        exit(0)


    print("Enter Actor Name:")
    actor_name= input().lower()

    print("Enter movie Name:")
    movie_name= input().lower()

    #regarding actor detials
    actor_details=getMoviesNameForActor(actor_name, cursor, conn)
    
    if(actor_details == -1):
        print("No data available for given actor name")
        return
    
    print("actor detials:\n",actor_details)

    #regarding movie details

    movie_details= getDirectorNameForMovie(movie_name, cursor, conn)

    if(movie_details == -1):
        print("No data available for given movie name")
        return
    
    print("movie detials:\n",movie_details)


if __name__ == '__main__':
    main()
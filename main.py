import pipeline.pipeline as pl

def main():
    # Connecting to database
    conn = pl.get_connection()

    # Pipeline Flow
    pl.create_tables(conn)
    pl.extraction(conn)
    pl.transformation(conn)
    pl.segment_creation(conn)

    # Closing database connection
    pl.close_connection(conn)

if __name__ == '__main__':
    main()
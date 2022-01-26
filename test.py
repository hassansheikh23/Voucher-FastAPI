import unittest
import db.database as db
import pipeline.pipeline as pl

class Testing(unittest.TestCase):

    def test_connection(self):
        conn = db.connect()
        self.assertNotEqual(conn, 1)
        curr = db.execute_query(conn, "Select version()")
        val = curr.fetchall()
        self.assertTrue(False if not val else True)
        curr.close()
        db.disconnect(conn)


    def test_segment_value(self):

        self.assertTrue(
            pl.check_segment(
                'frequent_segment', 
                {
                    'frequent_segment': 1,
                    'recency_segment' : 2
                }
            )
        )

        self.assertTrue(
            pl.check_segment(
                'RecencY_SeGment', 
                {
                    'frequent_segment': 1,
                    'recency_segment' : 2
                }
            )
        )

        self.assertFalse(
            pl.check_segment(
                'recent_segment', 
                {
                    'frequent_segment': 1,
                    'recency_segment' : 2
                }
            )
        )

    def test_range_function(self):
        self.assertTrue(
            pl.value_in_range(2, '0-3')
        )

        self.assertFalse(
            pl.value_in_range(5, '0-3')
        )


if __name__ == '__main__':
    unittest.main()
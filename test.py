import unittest
import database
import sys

class TestDatabase(unittest.TestCase):
    # pg 2
    def test1(self):
        db = database.database()
        
        db.set('a', 10)
        self.assertEqual(10, db.get('a'))
        db.delete('a')
        self.assertEqual('NULL', db.get('a'))

    def test1_str(self):
        db = database.database()

        db.run_command("SET a 10")
        self.assertEqual(10, db.run_command("GET a"))
        db.run_command('DELETE a')
        self.assertEqual('NULL', db.run_command("GET a"))

    # pg 3
    def test2(self):
        db = database.database()

        db.set('a', 10)
        db.set('b', 10)
        self.assertEqual(2, db.count(10))
        self.assertEqual(0, db.count(20))
        db.delete('a')
        self.assertEqual(1, db.count(10))
        db.set('b', 30)
        self.assertEqual(0, db.count(10))

    def test2_str(self):
        db = database.database()

        db.run_command("SET a 10")
        db.run_command("SET b 10")
        self.assertEqual(2, db.run_command("COUNT 10"))
        self.assertEqual(0, db.run_command("COUNT 20"))
        db.run_command('DELETE a')
        self.assertEqual(1, db.run_command("COUNT 10"))
        db.run_command('SET b 30')
        self.assertEqual(0, db.run_command("COUNT 10"))

#    def test3_transaction(self):
#        db = database.database()
#        db.begin()
#        db.run_command("SET a 10")
#        print(db.transactions)
#        db.rollback()
#        print(db.transactions)
#        print(db.run_command("GET a"))
##        db.begin()
##        db.run_command("SET b 20")
##        db.commit()
##        print(db.data)
##        sys.exit(1)

if __name__ == "__main__":
    unittest.main()

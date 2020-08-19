import unittest
import sys
sys.path.append('../src')
import user_sync

class TestUserSync(unittest.TestCase):
    def test_fetch_org_member(self):
        user_login_list = user_sync.fetch_org_member("FHDA")
        self.assertTrue('kis87988' in user_login_list)
        self.assertTrue('randomuser' not in user_login_list)

    def test_fetch_user_public_key(self):
        user_key_list = user_sync.fetch_user_public_key("kis87988")
        self.assertTrue("ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCv+EiGtK44IM4PHw9LrbpCq1yDFfevZgOhU4vJJ1tTaQe8bRH33ZlvPZdLp61HFjtFfsFZWQR8C7SE3iI2deQbH4HYEvJ3vfO7GBbw611ctvlPOBYcTpZ55B1lVW9tlcKTjBWAMR/WvbNRrsyM+EDgR6kh5uf8As8zxubQSaW3r01zuSSTBGCi+Fe1CkIhoQSsqXjw1LBSH87pbMwnChSeKNxRn+8z6Smaj/vPl254H2WyYWAEM4d1onMKaPgB28SQZHymHUDBpRqNc7rRDZPTnxNG4HEg9Syh+avd+mFhewRLHbfGowWB+AOar7OA1ryJfvzgVRCU/ZObNkELU+L5" in user_key_list)
        self.assertTrue('randomkey' not in user_key_list)

if __name__ == '__main__':
    unittest.main()
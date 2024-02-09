from unittest import TestCase, main

from ci_demo.main import Service

class MyUnitTests(TestCase):

    def test_sth(self):
        srv = Service()
        self.assertEqual(2, srv.plus_two(0))



if __name__ == "__main__":
    main()

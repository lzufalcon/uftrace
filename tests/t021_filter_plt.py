#!/usr/bin/env python

from runtest import TestBase

class TestCase(TestBase):
    def __init__(self):
        TestBase.__init__(self, 'getids', """
# DURATION    TID     FUNCTION
            [18130] | main() {
   1.811 us [18130] |   getpid();
   1.776 us [18130] |   getsid();
   1.289 us [18130] |   getuid();
   1.043 us [18130] |   getgid();
  98.632 us [18130] | } /* main */
""")

    def runcmd(self):
        return '%s -F "get.?id@plt" %s' % (TestBase.ftrace, 't-getids')

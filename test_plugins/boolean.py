# MIT License
#
# Copyright (c) 2020 Andre Lehmann
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


class TestModule(object):

    def tests(self):
        return {
            'boolean': self.is_boolean,
        }

    def is_boolean(self, value):
        """Test if a value is of type boolean.

        Jinja2 >= 2.11 comes a built-in boolean test, but most systems will ship
        an older version. Until Ansible adopts the new Jinja2 version, this test
        can be used as an alternative.

        Args:
            value: A value, that shall be type tested

        Returns:
            bool: True, if value is of type boolean, False otherwise.
        """
        return isinstance(value, bool)
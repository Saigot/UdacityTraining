#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import A01
import A02
import A03
import handler

class MainHandler(handler.Handler):
    def get(self):
        self.render("main.html")
#----------------------End Stuff----------------------#
app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/A01ROT13', A01.Assignment01),
    ('/A02SignUp', A02.Assignment02),('/A02SignUp/Welcome', A02.Welcome),
    ('/A03Blog',A03.Assignment03), ('/A03Blog/newpost',A03.NewPost),(r'/A03Blog/(\d+)',A03.PostHandler), 
    ], debug=True)

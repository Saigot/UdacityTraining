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
import cgi
formMain="""<form method="get">
        <p> <a href="/A01ROT13"> Assignmnt 1:Rot13 </a></p>
        <p> <a href="/A02SignUp"> Assignmnt 2:Signup </a></p>
        </form>"""
formA01="""<form method="post">
	<p> Enter some Text in ROT13 </p>
	<textarea name="text">%(text)s</textarea>
	<input type="submit" name="submit">
	<p> <a href="/"> Home </a></p>
</form>"""

formA02 = """<form method="post">
            <p><b>Sign Up</b></p>
            <p><input type="text" name = "username"></p>
            <p><input type="password" name = "password"></p>
            <p><input type="password" name = "verify"></p>
            <p><input type="text" name = "email"></p>
            <p> <a href="/"> Home </a></p>
            </form>"""
class MainHandler(webapp2.RequestHandler):
    def get(self):
        string = ""
        self.response.write(formMain)
        
    def post(self):
        Text = self.request.get("text")
        self.response.write(formMain)


#----------------Assignment01--------------------#
class Assignment01(webapp2.RequestHandler):
    def get(self):
        string = ""
        self.response.write(formA01 %{"text":string})
    def Rot13(self,text):
        newstring =""
        i =0
        while i < len(text):
            if((ord(text[i]) <= ord('z') - 13 and ord(text[i]) >= ord('a')) or (ord(text[i]) <= ord('Z') - 13 and ord(text[i]) >= ord('A'))):
                newstring += chr(ord(text[i]) + 13)
            elif (ord(text[i]) in range(ord('z') - 12, ord('z') +1)):
                newstring += chr(ord('a') + (12 - (ord('z') - ord(text[i]))))
            elif (ord(text[i]) in range(ord('Z') - 12, ord('Z')+1)):
                newstring += chr(ord('A') + (12 - (ord('Z') - ord(text[i]))))
            else:
                newstring += text[i]
            i = i+1
        return cgi.escape(newstring)
    
    def post(self):
        Text = self.request.get("text")
        Text = self.Rot13(Text)
        self.response.write(formA01 %{"text":Text})
                            
    
#----------------Assignment02--------------------#

#----------------------End Stuff----------------------#
app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/A01ROT13', Assignment01)
    ], debug=True)

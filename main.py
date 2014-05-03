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
import re
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
        
formA02 = """<form method="post">
            <p><b>Sign Up</b></p>
            <p>User:<input type="text" name = "username" value=%(usr)s><font color=\"red\">%(usrEr)s</font></p>
            <p>Pswd:<input type="password" name = "password"><font color=\"red\">%(pswdEr)s</font></p>
            <p>Verify:<input type="password" name = "verify"></p>
            <p>Email:<input type="text" name = "email" value=%(email)s><font color=\"red\">%(emailEr)s</font></p>
            <p><input type="Submit" name="Submit"></p>
            <p> <a href="/"> Home </a></p>
            </form>"""
USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
PSWD_RE = re.compile(r"^.{3,20}$")
EMAIL_RE = re.compile(r"^[\S]+@[\S]+\.[\S]+$")
class Assignment02(webapp2.RequestHandler):
    def get(self):
        self.response.write(formA02 %{"usr":"","email":"","pswdEr":""
                                      ,"emailEr":"","usrEr":""})
    def post(self):
        usr = self.request.get("username")
        pwd1 = self.request.get("password")
        pwd2 = self.request.get("verify")
        email = self.request.get("email")
        e = self.EmailCheck(email)
        p = self.PswdCheck(pwd1,pwd2)
        u = self.UsrCheck(usr)
        if(e == "" and p == "" and u == ""):
            self.redirect("/A02SignUp/Welcome?Usr=%s" %usr)
        else:
            self.response.write(formA02 %{"usr":usr,"email":email,
                                          "pswdEr":p, "emailEr":e,"usrEr":u})
    def EmailCheck(self,text):
        if(EMAIL_RE.match(text) or text == ""):
            return ""
        else:
            return "Sorry the email is bad"
    def PswdCheck(self, pswd, ver):
        if(PSWD_RE.match(pswd) and pswd == ver):
            return ""
        else:
            return "Sorry, Password is not Valid or does not match"
    def UsrCheck(self,text):
        if(USER_RE.match(text)):
            return ""
        else:
            return "Sorry, that's not a valid User"
class A02Welcome(webapp2.RequestHandler):
    def get(self):
        name=self.request.get("Usr")
        self.response.write("Welcome %s" %name)
#----------------------End Stuff----------------------#
app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/A01ROT13', Assignment01),
    ('/A02SignUp', Assignment02),('/A02SignUp/Welcome', A02Welcome)
    ], debug=True)

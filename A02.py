import webapp2
import cgi
import re
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
class Welcome(webapp2.RequestHandler):
    def get(self):
        name=self.request.get("Usr")
        self.response.write("Welcome %s" %name)

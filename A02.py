import handler
import cgi
import re
#----------------Assignment02--------------------#

USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
PSWD_RE = re.compile(r"^.{3,20}$")
EMAIL_RE = re.compile(r"^[\S]+@[\S]+\.[\S]+$")
class Assignment02(handler.Handler):
    def renderFront(self, usr="",email="",pswdEr="",usrEr="",emailEr=""):
        self.render("A02.html",usr = usr, email=email,
                    usrEr=usrEr, emailEr=emailEr, pswdEr = pswdEr)
    def get(self):
        self.renderFront()
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
            self.renderFront(usr,email,p,u,e)
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
class Welcome(handler.Handler):
    def get(self):
        name=self.request.get("Usr")
        self.response.write("Welcome %s" %name)

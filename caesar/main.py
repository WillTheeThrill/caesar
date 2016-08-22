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
from caesar import encrypt

header_block = """
<!DOCTYPE html>
<html>
  <head>
    <title>The One and The Only</title>
    <style type='text/css'>
     body {
     background-color:#ccc;
     }

    </style>
  </head>

<body>
 """
footer_block = """
</body>
</html>

 """
class MainHandler(webapp2.RequestHandler):
    def get(self):

        getUserText = self.request.get('user_T')
        getUserNumber = self.request.get('user_N')
        intro = "<div id='intro'>Go ahead and encrypt a message. Don't worry, Noone will know what it means."
        intro += "<img src='eyemoji.png' />"

        intro +="</div>"
        userInput = """
             <form method='get' action='/'>
             <label>State a number of arrangement</lable>
             <input type='text' name='user_N' /></br>
             <textarea type='password' name='user_T' value='"""+getUserText+"""' ></textarea>
             <input type='submit' value='Excrypt It!' />
             </form>
        """

        answer = encrypt(getUserText, getUserNumber)
        page = header_block + intro + userInput +  answer + footer_block
        self.response.write(page)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)

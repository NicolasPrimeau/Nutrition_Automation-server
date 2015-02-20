#!/usr/bin/env python

import alert

msg = dict()
msg['plain'] = "Hello world"
msg['html'] = "<p style=\"color:red\">Hello World</p>"

alert.send_email("nicolas.primeau@gmail.com", "test", msg)






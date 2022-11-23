# module = a file containing python code.May contain function, classes, etc
# used with modular programming, which is to separate program into parts

import messages

messages.hello()
messages.bye()

import messages as msg  # (alias or nickname)

msg.hello()
msg.bye()

from messages import hello,bye #(this only calls functions that we want)
hello()
bye()

# from messages import * (this imports all the functions)

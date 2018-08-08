from gmail import GMail,Message
gmail = GMail('trungkienbb1812@gmail.com','Ythgnqd171819')
html_content="""
<p style="text-align: center;">Cộng h&ograve;a x&atilde; hội chủ nghĩa Vệt Nam</p>
<p style="text-align: center;"><span style="text-decoration: underline;">Độc Lập - Tự Do - Hạnh Ph&uacute;c</span></p>
<p style="text-align: center;">&nbsp;</p>
<p style="text-align: center;"><strong>ĐƠN XIN NGHỈ HỌC</strong></p>
<p style="text-align: left;">T&ecirc;n em l&agrave;: Nguyễn Ch&iacute; Trung Ki&ecirc;n</p>
<p style="text-align: left;">H&ocirc;m nay em viết đơn n&agrave;y để xin thầy cho em nghi học v&igrave; {{sickness}}.</p>
<p style="text-align: left;">&nbsp;</p>
<p style="text-align: left;">Em xin ch&acirc;n th&agrave;nh cảm ơn!</p>
<p style="text-align: left;">Học sinh</p>
<p style="text-align: left;">Nguyễn Ch&iacute; Trung Ki&ecirc;n</p>
<p style="text-align: left;">&nbsp;</p>
"""

import random as rand
from datetime import datetime

from random import *
random=[
    "em bị đau bụng",
    "em bị ốm",
    "em bận đưa gấu đi start-up",
    "em bận đưa mẹ đi shopping"
]
send_email = True

current_time = str(datetime.time(datetime.now()))
current_hour = current_time[:5]

while current_hour > '07:00' and send_email:
    choice = rand.choice(random)
    html_content = html_content.replace('{{sickness}}',choice)
    msg = Message( 'Test message', to = 'trungkienbb1812@gmail.com', html = html_content )
    gmail.send(msg)
    send_email = False
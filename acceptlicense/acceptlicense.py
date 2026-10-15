import os
import pytz
from datetime import datetime
from .Apache_2_0 import Apache_2_0
from .GNU_GPL_3_0 import GNU_GPL_3_0
from .CC_BY_SA_4_0 import CC_BY_SA_4_0

now_utc = datetime.now(pytz.UTC)

MIT = ""
LICENSE_FILE = ".license"

LICENSE_TYPES = {
    "MIT": MIT,
    "GNU GPL 3.0": GNU_GPL_3_0,
    "Apache 2.0" : Apache_2_0,
    "CC-BY-SA 4.0": CC_BY_SA_4_0
    }

LICENSE_TYPE = ""
year = ""
name = ""

if name == "":
    name = input("What's your name ? >>> ")

if year == "":
    while True:
        try:
            year = int(input("What is the publication year of your software ? >>> "))
            break
        except ValueError:
            print("Enter an integer.")

if LICENSE_TYPE == "":
    while True:
        LICENSE_TYPE_TRY = input("Enter your license type >>> ")

        if LICENSE_TYPE_TRY in LICENSE_TYPES:
            LICENSE_TYPE = LICENSE_TYPE_TRY
            break
        else:
            print(f"Not in licenses types. {LICENSE_TYPES}")

MIT = """
The MIT License (MIT)

Copyright (c) {year}-present {name}

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""

def acceptlicense(type:str, year:int=datetime.now().year, name:str, affmessages:bool=True) -> bool:
    if os.path.exists(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".license")):
        return True
    else:
        if LICENSE_TYPE == "MIT":
            MIT = """
            The MIT License (MIT)

            Copyright (c) {year} - present {name}

            Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

            The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

            THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
            """

        print(LICENSE_TYPES[LICENSE_TYPE])
        acceptlicense = input("Do you accept the software license ? (yes/no)").strip().lower()
        if acceptlicense == "yes":
            with open(LICENSE_FILE, "w", encoding="utf-8") as f:
                f.write(f"{LICENSE_TYPE} accepted on {now_utc.strftime("%d/%m/%Y %H:%M:%S UTC+0")}")
            if affmessages:
                print("You can access the software.")
            return True
        else:
            if affmessages:
                print("You cannot access the software.")
            return False
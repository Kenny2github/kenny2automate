import os
os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from AutoAbyx import done, run

try:
    run()
except KeyboardInterrupt:
    pass
finally:
    done()
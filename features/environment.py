from splinter import Browser


BEHAVE_DEBUG_ON_ERROR = False

def setup_debug_on_error(userdata):
    global BEHAVE_DEBUG_ON_ERROR
    BEHAVE_DEBUG_ON_ERROR = userdata.getbool("pdb")


def before_all(context):
    print(context.config.userdata)
    setup_debug_on_error(context.config.userdata)
    if context.config.userdata.get('chrome', False):
        context.browser = Browser('chrome')
    context.browser = Browser('phantomjs')
    context.server_url = 'http://localhost:8000'


def after_step(context, step):
    if BEHAVE_DEBUG_ON_ERROR and step.status == "failed":
        import ipdb
        ipdb.post_mortem(step.exc_traceback)


def after_all(context):
    context.browser.quit()

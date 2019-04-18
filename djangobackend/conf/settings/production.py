from .base import *


WEBPACK_LOADER = {
    'DEFAULT': {
        'BUNDLE_DIR_NAME': 'bundles/',
        'STATS_FILE': os.path.join(
            WEBPACK_STATS_DIR, 'webpack-stats.prod.json'),
    }
}

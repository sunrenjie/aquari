#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.


import os
from six.moves import xrange

from os import walk, path

MODULE_EXT = '.module.js'
MOCK_EXT = '.mock.js'
SPEC_EXT = '.spec.js'


import xstatic.main
import xstatic.pkg.angular
import xstatic.pkg.angular_bootstrap
import xstatic.pkg.angular_fileupload
import xstatic.pkg.angular_gettext
import xstatic.pkg.angular_lrdragndrop
import xstatic.pkg.angular_smart_table
import xstatic.pkg.bootstrap_datepicker
import xstatic.pkg.bootstrap_scss
import xstatic.pkg.bootswatch
import xstatic.pkg.d3
import xstatic.pkg.font_awesome
import xstatic.pkg.hogan
import xstatic.pkg.jasmine
import xstatic.pkg.jquery
import xstatic.pkg.jquery_migrate
import xstatic.pkg.jquery_quicksearch
import xstatic.pkg.jquery_tablesorter
import xstatic.pkg.jquery_ui
import xstatic.pkg.jsencrypt
import xstatic.pkg.mdi
import xstatic.pkg.rickshaw
import xstatic.pkg.roboto_fontface
import xstatic.pkg.spin
import xstatic.pkg.termjs


def collect_bower_static_libs(bower_prefix, static_prefix):
    dirs = []
    for d in ['angular', 'angular-cookies', 'angular-route', 'bootstrap', 'bootstrap-material-design', 'jquery',
              'ng-dialog', 'tether', 'underscore']:
        dirs.append(('%s/lib/%s' % (static_prefix, d),
             os.path.abspath(os.path.join(bower_prefix, d))))
    return dirs


def collect_static_lib_dirs(webroot='/'):
    prefix = 'aquari'
    dirs = [
        ('%s/lib/angular' % prefix,
            xstatic.main.XStatic(xstatic.pkg.angular,
                                 root_url=webroot).base_dir),
        ('%s/lib/angular' % prefix,
            xstatic.main.XStatic(xstatic.pkg.angular_bootstrap,
                                 root_url=webroot).base_dir),
        ('%s/lib/angular' % prefix,
            xstatic.main.XStatic(xstatic.pkg.angular_fileupload,
                                 root_url=webroot).base_dir),
        ('%s/lib/angular' % prefix,
            xstatic.main.XStatic(xstatic.pkg.angular_gettext,
                                 root_url=webroot).base_dir),
        ('%s/lib/angular' % prefix,
            xstatic.main.XStatic(xstatic.pkg.angular_lrdragndrop,
                                 root_url=webroot).base_dir),
        ('%s/lib/angular' % prefix,
            xstatic.main.XStatic(xstatic.pkg.angular_smart_table,
                                 root_url=webroot).base_dir),
        ('%s/lib/bootstrap_datepicker' % prefix,
            xstatic.main.XStatic(xstatic.pkg.bootstrap_datepicker,
                                 root_url=webroot).base_dir),
        ('%s/lib/bootstrap' % prefix,
            xstatic.main.XStatic(xstatic.pkg.bootstrap_scss,
                                 root_url=webroot).base_dir),
        ('%s/lib/bootswatch' % prefix,
         xstatic.main.XStatic(xstatic.pkg.bootswatch,
                              root_url=webroot).base_dir),
        ('%s/lib' % prefix,
            xstatic.main.XStatic(xstatic.pkg.d3,
                                 root_url=webroot).base_dir),
        ('%s/lib' % prefix,
            xstatic.main.XStatic(xstatic.pkg.hogan,
                                 root_url=webroot).base_dir),
        ('%s/lib/font-awesome' % prefix,
            xstatic.main.XStatic(xstatic.pkg.font_awesome,
                                 root_url=webroot).base_dir),
        ('%s/lib/jasmine' % prefix,
            xstatic.main.XStatic(xstatic.pkg.jasmine,
                                 root_url=webroot).base_dir),
        ('%s/lib/jquery' % prefix,
            xstatic.main.XStatic(xstatic.pkg.jquery,
                                 root_url=webroot).base_dir),
        ('%s/lib/jquery' % prefix,
            xstatic.main.XStatic(xstatic.pkg.jquery_migrate,
                                 root_url=webroot).base_dir),
        ('%s/lib/jquery' % prefix,
            xstatic.main.XStatic(xstatic.pkg.jquery_quicksearch,
                                 root_url=webroot).base_dir),
        ('%s/lib/jquery' % prefix,
            xstatic.main.XStatic(xstatic.pkg.jquery_tablesorter,
                                 root_url=webroot).base_dir),
        ('%s/lib/jsencrypt' % prefix,
            xstatic.main.XStatic(xstatic.pkg.jsencrypt,
                                 root_url=webroot).base_dir),
        ('%s/lib/mdi' % prefix,
         xstatic.main.XStatic(xstatic.pkg.mdi,
                              root_url=webroot).base_dir),
        ('%s/lib' % prefix,
            xstatic.main.XStatic(xstatic.pkg.rickshaw,
                                 root_url=webroot).base_dir),
        ('%s/lib/roboto_fontface' % prefix,
         xstatic.main.XStatic(xstatic.pkg.roboto_fontface,
                              root_url=webroot).base_dir),
        ('%s/lib' % prefix,
            xstatic.main.XStatic(xstatic.pkg.spin,
                                 root_url=webroot).base_dir),
        ('%s/lib' % prefix,
         xstatic.main.XStatic(xstatic.pkg.termjs,
                              root_url=webroot).base_dir),
        ('%s/lib/jquery-ui/ui' % prefix,
         xstatic.main.XStatic(xstatic.pkg.jquery_ui,
                              root_url=webroot).base_dir)
    ]

    return dirs


def populate_config_with_static_files(config, paths):
    cats = ['js_sources', 'js_mocks', 'js_specs', 'html_templates']
    for c in cats:
        if c not in config:
            config[c] = []
    for p in paths:
        r = list(collect_static_files(p))
        for i in xrange(0, len(cats)):
            config[cats[i]].extend(r[i])


def collect_static_files(prefix):
    js_files = collect_files(prefix, ext='.js', relative=True)
    srcs, mocks, specs = sort_js_files(js_files)
    html_files = collect_files(prefix, ext='.html', relative=True)
    return srcs, mocks, specs, html_files


def collect_files(prefix, ext='', relative=False):
    if not prefix.endswith('/'):
        prefix += '/'
    file_list = []

    for root, dirs, files in walk(prefix):
        if relative:
            root = root.replace(prefix, '', 1)
        file_list.extend([path.join(root, f)
                          for f in files if f.endswith(ext)])
    return sorted(file_list)


def sort_js_files(js_files):
    """Sorts JavaScript files in `js_files` into source files, mock files
    and spec files based on file extension.

    Output:

    * sources: source files for production.  The order of source files
      is significant and should be listed in the below order:

      - First, all the that defines the other application's angular module.
        Those files have extension of `.module.js`.  The order among them is
        not significant.

      - Followed by all other source code files.  The order among them
        is not significant.

    * mocks: mock files provide mock data/services for tests.  They have
      extension of `.mock.js`. The order among them is not significant.

    * specs: spec files for testing.  They have extension of `.spec.js`.
      The order among them is not significant.

    """
    modules = [f for f in js_files if f.endswith(MODULE_EXT)]
    mocks = [f for f in js_files if f.endswith(MOCK_EXT)]
    specs = [f for f in js_files if f.endswith(SPEC_EXT)]

    other_sources = [f for f in js_files if
                     not f.endswith(MODULE_EXT)
                     and not f.endswith(MOCK_EXT)
                     and not f.endswith(SPEC_EXT)]

    sources = modules + other_sources
    return sources, mocks, specs

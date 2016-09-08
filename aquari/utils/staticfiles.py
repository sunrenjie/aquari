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
